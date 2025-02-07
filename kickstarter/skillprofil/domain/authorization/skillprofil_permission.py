"""Persmission Classes for "Skillprofil"."""
# ---------------------------------------------------------------------------------------------------------------------
from logging import Logger, getLogger

from rest_framework import permissions
from rest_framework.request import Request
from skillprofil.domain.authorization.skillprofil_user import SkillprofilUser

# ---------------------------------------------------------------------------------------------------------------------


class SkillProfilPermission(permissions.BasePermission):
    """Permission Class for View Skillprofil."""

    def __init__(self):
        self.__logger: Logger = getLogger(self.__class__.__name__)
        pass

    def has_permission(self, request: Request, view) -> bool:
        """Allows Access if the User is from Human Ressource Management."""
        try:
            self.__logger.info(f'Request {request} asked for permission.')
            if isinstance(request.user, SkillprofilUser) and request.method == 'POST':
                return request.user.is_human_ressource_manager()
            else:
                return True
            return True
        except (
            Exception
        ) as e:  # noqa: B902 # If Exception is raised, there is an Error... Don't permit anyone if there is an internal Error..
            self.__logger.exception(e)
        return False

    pass


# ---------------------------------------------------------------------------------------------------------------------
