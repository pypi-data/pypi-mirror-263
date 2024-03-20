class InvalidTokenError(Exception):
    """Raised when an invalid token is provided."""

    pass


class InternalServerError(Exception):
    """Raised when an internal server error occurs."""

    pass


class InvalidDataError(Exception):
    """Raised when invalid data is provided."""

    pass


class MissingDataError(Exception):
    """Raised when required data is missing."""

    pass


class CoreDataError(Exception):
    """Raised when core server data is invalid."""

    pass
