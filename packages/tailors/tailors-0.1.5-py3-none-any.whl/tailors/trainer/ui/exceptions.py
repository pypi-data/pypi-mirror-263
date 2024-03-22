class AuthException(Exception):
    """Authentication or authorization failed"""

    def __init__(self, msg=None, *args, **kwargs):
        super().__init__(msg or self.__doc__, *args, **kwargs)


class InvalidUserOrPasswordException(AuthException):
    """Invalid username or password"""


class UnAuthedException(AuthException):
    """Not authed, please login first"""


class BadTokenException(AuthException):
    """The token is invalid"""


class ExpiredTokenException(AuthException):
    """The token is expired, please login again"""


class PermissionDeniedException(AuthException):
    """You have no permission to access the resource"""
