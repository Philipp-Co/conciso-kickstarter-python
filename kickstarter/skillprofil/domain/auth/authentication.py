"""Authorization and Authetication."""
# ---------------------------------------------------------------------------------------------------------------------

from logging import Logger, getLogger

from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication
from rest_framework_simplejwt.tokens import AccessToken

# ---------------------------------------------------------------------------------------------------------------------


class MyAuthToken(AccessToken):
    """Token which is used by Simple JWT."""

    def __init__(self, *args, **kwargs):
        self.__logger: Logger = getLogger(self.__class__.__name__)
        try:
            self.__logger.info('Initialize MyAuthToken!')
            super().__init__(*args, **kwargs)
        except Exception as e:  # noqa: B 901 # Exception should be logged... Simple JWT hides Exception Information.
            self.__logger.exception(e)
            raise e
        pass

    pass


# ---------------------------------------------------------------------------------------------------------------------


class MyAuthentication(JWTStatelessUserAuthentication):
    """Authentication Class used by Simple JWT."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__logger: Logger = getLogger(self.__class__.__name__)
        pass

    def authenticate(self, request: Request):
        header = self.get_header(request)
        self.__logger.info(
            f'Header: {header}',
        )
        self.__logger.info(
            f'Raw Token: {self.get_raw_token(header)}',
        )
        super().authenticate(request)

    pass


# ---------------------------------------------------------------------------------------------------------------------
