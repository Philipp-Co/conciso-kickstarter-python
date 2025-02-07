from rest_framework_simplejwt.models import TokenUser
from rest_framework_simplejwt.tokens import Token
from logging import getLogger, Logger


class SkillprofilUser(TokenUser):

    def __init__(self, token: Token):
        super().__init__(token)
        self.__logger: Logger = getLogger(self.__class__.__name__)
        pass

    def is_human_ressource_manager(self) -> bool:
        return 'Human Ressource Manager' in self.roles()

    def roles(self):
        try:
            return [
                role for role in self.token.get('realm_access', {'roles': []}).get('roles')
            ]
        except KeyError as e:
            self.__logger.exception(e)
            return []

    pass

