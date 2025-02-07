from rest_framework import permissions
from rest_framework.request import Request
from logging import getLogger, Logger
from skillprofil.domain.authorization.skillprofil_user import SkillprofilUser

class SkillProfilPermission(permissions.BasePermission):
    
    def __init__(self):
        self.__logger: Logger = getLogger(self.__class__.__name__)
        pass

    def has_permission(self, request: Request, view) -> bool:
        try:
            self.__logger.info(f'Request {request} asked for permission.')
            #if isinstance(request.user, SkillprofilUser) and request.method == 'POST':
            #    return request.user.is_human_ressource_manager()
            #else:
            #    return True
            return True
        except Exception as e:
            self.__logger.exception(e)
        return False

    pass
