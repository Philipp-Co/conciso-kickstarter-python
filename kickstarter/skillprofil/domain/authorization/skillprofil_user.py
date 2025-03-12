"""Authorization."""
# ---------------------------------------------------------------------------------------------------------------------
from logging import Logger, getLogger

from rest_framework_simplejwt.models import TokenUser
from rest_framework_simplejwt.tokens import Token

# ---------------------------------------------------------------------------------------------------------------------


class SkillprofilUser(TokenUser):
    """Encapulates Role Management."""

    def __init__(self, token: Token):
        super().__init__(token)
        self.__logger: Logger = getLogger(self.__class__.__name__)
        pass

    def is_human_ressource_manager(self) -> bool:
        """Tell me if this User is a 'Human Ressource Manager'."""
        return 'Human Ressource Manager' in self.roles()

    def roles(self):
        """Give me all Roles of this User."""
        try:
            return [role for role in self.token.get('realm_access', {'roles': []}).get('roles')]  # noqa: C416
        except KeyError as e:
            self.__logger.exception(e)
            return []

    pass


# ---------------------------------------------------------------------------------------------------------------------
