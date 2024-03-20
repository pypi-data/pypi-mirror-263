import requests
import logging
from typing import Literal
from dataclasses import dataclass
from flask import Flask, request
from markupsafe import Markup


@dataclass
class EventResult:
    allow: bool
    outcome: Literal["allow", "allow_review", "block", "block_review", "review"] 
    country: str
    timezone: str
    address_valid: bool
    address: str
    email_valid: bool
    email: str
    phone_valid: bool
    phone: str
    ip: str
    data: dict


class NotFlaskApp(Exception):
    pass


class BaseConfig:
    event_url = "https://app.usedanger.com/api/v1/event"
    script_url = "https://js.usedanger.com/v1/api.js"
    timeout = 8
    fallback_allow = True
    fallback_country = "US"
    fallback_timezone = "UTC"


class Danger(BaseConfig):
    site_key = None
    secret_key = None

    def __init__(self, app: Flask = None):
        if app is not None:
            if not isinstance(app, Flask):
                raise NotFlaskApp(f"Object {app} not a Flask instance.")
            self.init_app(app)

    def init_app(self, app: Flask):
        """
        Initialize the Danger extension to the given app object.

        Args:
            app: Flask object
        """
        self.event_url = app.config.get("DANGER_EVENT_URL", self.event_url)
        self.script_url = app.config.get("DANGER_SCRIPT_URL", self.script_url)
        self.site_key = app.config.get("DANGER_SITE_KEY")
        self.secret_key = app.config.get("DANGER_SECRET_KEY")
        self.timeout = app.config.get("DANGER_TIMEOUT", self.timeout)
        self.fallback_allow = app.config.get("DANGER_FALLBACK_ALLOW", self.fallback_allow)
        self.fallback_country = app.config.get("DANGER_FALLBACK_COUNTRY", self.fallback_country)
        self.fallback_timezone = app.config.get("DANGER_FALLBACK_TIMEZONE", self.fallback_timezone)

        @app.context_processor
        def app_context_processor():
            return { "danger": self.get_html() }

    def get_html(self):
        """
        Create the HTML to include in the client side HTML form. Use inside a template using Jinja
        syntax {{ danger }}. Add this anywhere within your form.
        """
        return Markup(
            f'<script src="{self.script_url}" async defer></script>\n' +
            f'<input type="hidden" name="danger-bundle" data-sitekey="{self.site_key}">'
        )

    def event(self, type: str = "new_user", name: str = None, email: str = None, phone: str = None, address: dict = None, bundle: str = None, ip: str = None, external_id: str = None):
        """
        Register the event with Danger. Pass in the user's data (email, phone, etc.) along with the
        bundle that is sent in the 'danger-bundle' field on your form.

        Args:
            type: str: (Optional) Event type, either "new_user" (default) or "login"
            name: str: (Optional) Person's name
            email: str: Person's email address
            phone: str: (Optional) Person's phone number
            address: dict: (Optional) Person's address, a dict with keys address1, address2, city, state, country, postal_code
            bundle: str: The 'bundle' that Danger added to the form in the hidden field 'danger-bundle'
            ip: str: (Optional) The remote IP address, i.e. that of the person's connection. Defaults to `request.remote_addr`.
            external_id: str: (Optional) An external identifier for this person, i.e. your app's database ID

        Returns:
            Result object with an 'allow' property (boolean), the full Danger result in 'data', and convenience
            properties for resolving the person's timezone, country, email, phone number, and address.
        
        Raises:
            ValueError: For implementation or authentication errors. All other errors and exceptions result in a
            fallback result object (so the app can 'fail open') with a log.error via the app's default logger.
        """

        data = {
            "type": type,
            "ip": ip or request.remote_addr,
            "secret_key": self.secret_key
        }
        
        for property, value in {"name": name, "email": email, "phone": phone, "address": address, "bundle": bundle, "timeout": self.timeout, "external_id": external_id}.items():
            if value is not None:
                data[property] = value
        
        # Set HTTP read timeout to be 3 seconds longer than
        # the Danger timeout, then we're sure to have a
        # result back by then.
        # Set connect timeout to 3 seconds.
        http_timeout = (5, self.timeout + 3)
        
        # Create a result instance with default/fallback values
        # Either return this directly, or augment with actual result if possible
        result = EventResult(
            allow=self.fallback_allow,
            outcome=None,
            country=self.fallback_country,
            timezone=self.fallback_timezone,
            address_valid=None,
            address=address,
            email_valid=None,
            email=email,
            phone_valid=None,
            phone=phone,
            ip=request.remote_addr,
            data={}
        )

        try:
            response = requests.post(self.event_url, json=data, timeout=http_timeout)
        except requests.exceptions.ConnectionError:
            return result
        except requests.exceptions.Timeout:
            return result
        except requests.exceptions.RequestException:
            return result
        else:
            try:
                json = response.json()
            except requests.exceptions.JSONDecodeError:
                json = {}
            
            if response.status_code == 400 or response.status_code == 401:
                # Bad request or unauthorized (implementation errors)
                raise ValueError("Flask-Danger: " + json.get("message", f"Received HTTP status code {response.status_code} from Danger."))
            elif response.status_code != 200:
                # Likely temporary errors such as rate limited or service unavailable
                # Return the default result in this case, to fail open
                # Don't raise an exception, but log the error
                logging.error("Flask-Danger: There was an error logging an event, but Danger responded with the fallback result. " + json.get("message", f"Received HTTP status code {response.status_code}."))
                return result

            result.data = json
            result.outcome = json["outcome"]

            if "block" in json["outcome"]:
                result.allow = False
            else:
                result.allow = True

            if "ip" in json and json["ip"]["success"]:
                result.ip = json["ip"]["ip"]
                if json["ip"]["country_code"]:
                    result.country = json["ip"]["country_code"]
                if json["ip"]["timezone"]:
                    result.timezone = json["ip"]["timezone"]

            if "address" in json and json["address"]["success"]:
                result.address_valid = json["address"]["valid"]
                if json["address"]["valid"]:
                    result.address = {
                        "address1": json["address"]["address1"],
                        "address2": json["address"]["address2"],
                        "city": json["address"]["city"],
                        "state": json["address"]["state"],
                        "country": json["address"]["country_name"],
                        "postal_code": json["address"]["postal_code"],
                    }

            if "email" in json and json["email"]["success"]:
                result.email_valid = json["email"]["valid"]
                if json["email"]["valid"]:
                    result.email = json["email"]["email"]

            if "phone" in json and json["phone"]["success"]:
                result.phone_valid = json["phone"]["valid"]
                if json["phone"]["valid"]:
                    result.phone = json["phone"]["phone"]

            return result