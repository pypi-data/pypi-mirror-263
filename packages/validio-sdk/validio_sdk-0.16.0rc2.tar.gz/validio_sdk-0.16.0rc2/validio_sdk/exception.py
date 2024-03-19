"""Exceptions used throughout the system."""

from typing import Any


class ValidioError(Exception):
    """Base exception used for every exception thrown by Validio."""

    def __init__(self, *args: Any):
        """Construct the exception."""
        super().__init__(*args)


class ConfigNotFoundError(ValidioError):
    """Exception when no configuration is found."""

    def __init__(
        self, endpoint_env: str, access_key_env: str, secret_access_key_env: str
    ) -> None:
        """Construct the exception."""
        super().__init__(
            "No configuration file found. Run 'validio config init' to create one or"
            f" set the environment variables '{endpoint_env}',"
            f" '{access_key_env}' and '{secret_access_key_env}'"
        )


class ConfigInvalidError(ValidioError):
    """Exception when the configuration file is invalid."""

    def __init__(self) -> None:
        """Construct the exception."""
        super().__init__("Configuration file is invalid.")


class UnauthorizedError(ValidioError):
    """Exception thrown when unauthorized request is made."""

    def __init__(self, access_key_env: str, secret_access_key_env: str) -> None:
        """Construct the exception."""
        super().__init__(
            "🛑 Unauthorized!\n"
            "Make sure you have proper credentials and run 'validio config init' to"
            f" add them or use '{access_key_env}' and"
            f" '{secret_access_key_env}'"
        )


class ValidioConnectionError(ValidioError):
    """Exception thrown when connection to Validio backend fails."""

    def __init__(self, endpoint_env: str, e: Exception) -> None:
        """Construct the exception."""
        super().__init__(
            f"🛑 Failed to connect to server: {e!s}\n"
            "Check your network environment, run 'validio config init' to set a proper"
            f" server endpoint or use '{endpoint_env}'"
        )
