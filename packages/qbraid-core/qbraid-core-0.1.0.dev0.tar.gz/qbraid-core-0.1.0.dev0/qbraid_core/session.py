# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Module for making requests to the qBraid API.

"""
import configparser
import datetime
import logging
import os
from typing import Any, Optional

from requests import RequestException, Response, Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .exceptions import AuthError, ConfigError, RequestsApiError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEFAULT_ENDPOINT_URL = "https://api.qbraid.com/api"
DEFAULT_CONFIG_PATH = os.path.join(os.path.expanduser("~"), ".qbraid", "qbraidrc")
DEFAULT_CONFIG_SECTION = "default"

STATUS_FORCELIST = (
    500,  # General server error
    502,  # Bad Gateway
    503,  # Service Unavailable
    504,  # Gateway Timeout
    520,  # Cloudflare general error
    522,  # Cloudflare connection timeout
    524,  # Cloudflare Timeout
)


class PostForcelistRetry(Retry):
    """Custom :py:class:`urllib3.Retry` class that performs retry on ``POST`` errors in the
    force list. Retrying of ``POST`` requests are allowed *only* when the status code returned
    is on the :py:const:`~qbraid.api.session.STATUS_FORCELIST`. While ``POST`` requests are
    recommended not to be retried due to not being idempotent, retrying on specific 5xx errors
    through the qBraid API is safe.
    """

    def increment(  # type: ignore[no-untyped-def]
        self,
        method=None,
        url=None,
        response=None,
        error=None,
        _pool=None,
        _stacktrace=None,
    ):
        """Overwrites parent class increment method for logging."""
        if logger.getEffectiveLevel() is logging.DEBUG:
            # coverage: ignore
            status = data = headers = None
            if response:
                status = response.status
                data = response.data
                headers = response.headers
            logger.debug(
                "Retrying method=%s, url=%s, status=%s, error=%s, data=%s, headers=%s",
                method,
                url,
                status,
                error,
                data,
                headers,
            )
        return super().increment(
            method=method,
            url=url,
            response=response,
            error=error,
            _pool=_pool,
            _stacktrace=_stacktrace,
        )

    def is_retry(self, method: str, status_code: int, has_retry_after: bool = False) -> bool:
        """Indicate whether the request should be retried.

        Args:
            method: Request method.
            status_code: Status code.
            has_retry_after: Whether retry has been done before.

        Returns:
            ``True`` if the request should be retried, ``False`` otherwise.
        """
        if method.upper() == "POST" and status_code in self.status_forcelist:
            return True

        return super().is_retry(method, status_code, has_retry_after)


class QbraidSession(Session):  # pylint: disable=too-many-instance-attributes
    """Custom session with handling of request urls and authentication.

    This is a child class of :py:class:`requests.Session`. It handles qbraid
    authentication with custom headers, has SSL verification disabled
    for compatibility with lab, and returns all responses as jsons for
    convenience in the sdk.

    Args:
        user_email: qBraid / JupyterHub User.
        api_key: Authenticated qBraid API key.
        refresh_token: Authenticated qBraid refresh-token.
        id_token: Authenticated qBraid id-token.
        base_url: Base URL for the session's requests.
        retries_total: Number of total retries for the requests.
        retries_connect: Number of connect retries for the requests.
        backoff_factor: Backoff factor between retry attempts.

    """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        user_email: Optional[str] = None,
        api_key: Optional[str] = None,
        refresh_token: Optional[str] = None,
        id_token: Optional[str] = None,
        base_url: Optional[str] = None,
        retries_total: int = 3,
        retries_connect: int = 2,
        backoff_factor: float = 0.5,
    ) -> None:
        super().__init__()

        self.user_email = user_email
        self.api_key = api_key
        self.refresh_token = refresh_token
        self.id_token = id_token
        self.base_url = base_url
        self.verify = False
        self.headers.update({"domain": "qbraid"})

        self._initialize_retry(retries_total, retries_connect, backoff_factor)

    def __del__(self) -> None:
        """qbraid session destructor. Closes the session."""
        self.close()

    @property
    def base_url(self) -> Optional[str]:
        """Return the qbraid api url."""
        return self._base_url

    @base_url.setter
    def base_url(self, value: Optional[str]) -> None:
        """Set the qbraid api url."""
        url = value or self.get_config_variable("url")
        self._base_url = url or DEFAULT_ENDPOINT_URL

    @property
    def user_email(self) -> Optional[str]:
        """Return the session user email."""
        return self._user_email

    @user_email.setter
    def user_email(self, value: Optional[str]) -> None:
        """Set the session user email."""
        user_email = value or self.get_config_variable("email")
        self._user_email = user_email or os.getenv("JUPYTERHUB_USER")
        if user_email:
            self.headers.update({"email": user_email})  # type: ignore[attr-defined]

    @property
    def api_key(self) -> Optional[str]:
        """Return the api key."""
        return self._api_key

    @api_key.setter
    def api_key(self, value: Optional[str]) -> None:
        """Set the api key."""
        api_key = value or self.get_config_variable("api-key")
        self._api_key = api_key or os.getenv("QBRAID_API_KEY")
        if api_key:
            self.headers.update({"api-key": api_key})  # type: ignore[attr-defined]

    @property
    def refresh_token(self) -> Optional[str]:
        """Return the session refresh token."""
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, value: Optional[str]) -> None:
        """Set the session refresh token."""
        refresh_token = value or self.get_config_variable("refresh-token")
        self._refresh_token = refresh_token or os.getenv(
            "QBRAID_REFRESH_TOKEN", os.getenv("REFRESH")
        )  # keep REFRESH for backwards compatibility
        if refresh_token:
            self.headers.update({"refresh-token": refresh_token})  # type: ignore[attr-defined]

    @property
    def id_token(self) -> Optional[str]:
        """Return the session id token."""
        return self._id_token

    @id_token.setter
    def id_token(self, value: Optional[str]) -> None:
        """Set the session id token."""
        id_token = value or self.get_config_variable("id-token")
        self._id_token = id_token or os.getenv("QBRAID_ID_TOKEN")
        if id_token and "refresh-token" not in self.headers:
            self.headers.update({"id-token": id_token})  # type: ignore[attr-defined]

    def _running_in_lab(self) -> bool:
        """Check if running in the qBraid Lab environment."""
        # API interaction to confirm environment
        try:
            utc_datetime = datetime.datetime.now(datetime.UTC)
        except AttributeError:  # deprecated but use as fallback if datetime.UTC is not available
            utc_datetime = datetime.datetime.utcnow()

        try:
            formatted_time = utc_datetime.strftime("%Y%m%d%H%M%S")
            directory = os.path.join(os.path.expanduser("~"), ".qbraid", "certs")
            filepath = os.path.join(directory, formatted_time)
            os.makedirs(directory, exist_ok=True)

            # Create an empty file
            with open(filepath, "w", encoding="utf-8"):
                pass  # The file is created and closed immediately

            response = self.get(f"/lab/is-mounted/{formatted_time}")
            is_mounted = bool(response.json().get("isMounted", False))
        except (RequestsApiError, KeyError):
            is_mounted = False

        try:
            os.remove(filepath)
        except (FileNotFoundError, IOError):
            pass
        return is_mounted

    def get_config_variable(self, config_name: str) -> Optional[str]:
        """Returns the config value of specified config.

        Args:
            config_name: The name of the config
        """
        filepath = DEFAULT_CONFIG_PATH
        if os.path.isfile(filepath):
            config = configparser.ConfigParser()
            config.read(filepath)
            section = DEFAULT_CONFIG_SECTION
            if section in config.sections():
                if config_name in config[section]:
                    return config[section][config_name]
        return None

    def save_config(  # pylint: disable=too-many-arguments,too-many-branches
        self,
        user_email: Optional[str] = None,
        api_key: Optional[str] = None,
        refresh_token: Optional[str] = None,
        id_token: Optional[str] = None,
        base_url: Optional[str] = None,
    ) -> None:
        """Create qbraidrc file. In qBraid Lab, qbraidrc is automatically present in filesystem.

        Args:
            user_email:  JupyterHub User.
            api_key: Authenticated qBraid api-key.
            refresh_token: Authenticated qBraid refresh-token.
            id_token: Authenticated qBraid id-token.
            base_url: Base URL for the session's requests.
        """
        self.user_email = user_email or self.user_email
        self.api_key = api_key or self.api_key
        self.refresh_token = refresh_token or self.refresh_token
        self.id_token = id_token or self.id_token
        self.base_url = base_url or self.base_url

        try:
            res = self.get("/identity")
        except RequestsApiError as err:
            raise AuthError from err

        res_json = res.json()

        if res.status_code != 200:
            raise AuthError(f"{res.status_code} Client Error: Invalid qBraid API credentials")

        res_email = res_json.get("email")

        if self.user_email:
            if self.user_email != res_email:
                raise AuthError(
                    f"Credential mismatch: Session initialized for '{self.user_email}', \
                        but API key corresponds to '{res_email}'."
                )
        else:
            self.user_email = res_email

        try:
            filepath = DEFAULT_CONFIG_PATH

            if not os.path.isfile(filepath):
                os.makedirs(os.path.dirname(filepath), exist_ok=True)
            config = configparser.ConfigParser()
            section = DEFAULT_CONFIG_SECTION
            if section not in config.sections():
                config.add_section(section)
            if self.user_email:
                config.set(section, "email", self.user_email)
            if self.api_key:
                config.set(section, "api-key", self.api_key)
            if self.refresh_token:
                config.set(section, "refresh-token", self.refresh_token)
            if self.id_token:
                config.set(section, "id-token", self.id_token)
            if self.base_url:
                config.set(section, "url", self.base_url)
            with open(filepath, "w", encoding="utf-8") as cfgfile:
                config.write(cfgfile)
        except Exception as err:
            raise ConfigError from err

    @staticmethod
    def _convert_email_symbols(email: str) -> Optional[str]:
        """Convert email to compatible string format"""
        return (
            email.replace("-", "-2d")
            .replace(".", "-2e")
            .replace("@", "-40")
            .replace("_", "-5f")
            .replace("+", "-2b")
        )

    def _initialize_retry(
        self, retries_total: int, retries_connect: int, backoff_factor: float
    ) -> None:
        """Set the session retry policy.

        Args:
            retries_total: Number of total retries for the requests.
            retries_connect: Number of connect retries for the requests.
            backoff_factor: Backoff factor between retry attempts.
        """
        retry = PostForcelistRetry(
            total=retries_total,
            connect=retries_connect,
            backoff_factor=backoff_factor,
            status_forcelist=STATUS_FORCELIST,
        )

        retry_adapter = HTTPAdapter(max_retries=retry)
        self.mount("http://", retry_adapter)
        self.mount("https://", retry_adapter)

    def request(self, method: str, url: str, **kwargs: Any) -> Response:  # type: ignore[override]
        """Construct, prepare, and send a ``Request``.

        Args:
            method: Method for the new request (e.g. ``POST``).
            url: URL for the new request.
            **kwargs: Additional arguments for the request.
        Returns:
            Response object.
        Raises:
            RequestsApiError: If the request failed.
        """
        # pylint: disable=arguments-differ
        final_url = self.base_url + url

        headers = self.headers.copy()
        headers.update(kwargs.pop("headers", {}))

        try:
            response = super().request(method, final_url, headers=headers, **kwargs)
            response.raise_for_status()
        except RequestException as ex:
            # Wrap requests exceptions for compatibility.
            message = str(ex)
            if ex.response is not None:
                try:
                    error_json = ex.response.json()["error"]
                    msg = error_json["message"]
                    code = error_json["code"]
                    message += f". {msg}, Error code: {code}."
                    logger.debug("Response uber-trace-id: %s", ex.response.headers["uber-trace-id"])
                except Exception:  # pylint: disable=broad-except
                    # the response did not contain the expected json.
                    message += f". {ex.response.text}"

            if self.refresh_token:
                message = message.replace(self.refresh_token, "...")

            raise RequestsApiError(message) from ex

        return response
