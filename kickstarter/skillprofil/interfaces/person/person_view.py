"""API for persons."""
# ---------------------------------------------------------------------------------------------------------------------
from http import HTTPStatus
from json import loads
from logging import Logger, getLogger
from typing import Any, Optional

from drf_spectacular.utils import extend_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from skillprofil.domain.hr import HirePersonResult, HumanResources, PersonRepr
from skillprofil.interfaces.person.person_serializer import (
    GetPersonRequestSerializer,
    HirePersonRequestSerializer,
    HirePersonResponseSerializer,
)
from skillprofil.domain.authorization.skillprofil_permission import SkillProfilPermission

# ---------------------------------------------------------------------------------------------------------------------


class PersonView(APIView):
    """This Klass implements the API for hiring peoples."""

    permission_classes = [SkillProfilPermission]

    def __init__(self, *args, logger: Optional[Logger] = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.__logger: Logger = logger if logger is not None else getLogger(self.__class__.__name__)
        pass

    def __build_response(self, http_status: HTTPStatus, data: Any) -> Response:
        """Build a response object."""
        return Response(
            status=http_status.value,
            data=data,
        )

    @extend_schema(
        operation_id='hire_unknown_person',
        # parameters=[],
        request=HirePersonRequestSerializer,
        responses={
            HTTPStatus.OK.value: HirePersonResponseSerializer,
            HTTPStatus.BAD_REQUEST.value: HirePersonResponseSerializer,
            HTTPStatus.INTERNAL_SERVER_ERROR.value: HirePersonResponseSerializer,
        },
    )
    def post(self, request: Request) -> Response:
        """Hire an unknown person."""
        try:
            request_serializer: HirePersonRequestSerializer = HirePersonRequestSerializer(
                data=loads(request.body.decode())
            )
            if request_serializer.is_valid():
                parsed_data = request_serializer.data
                result: HirePersonResult = HumanResources(self.__logger.getChild('Human Ressources')).hire(
                    PersonRepr(
                        name=parsed_data['name'],
                        surname=parsed_data['surname'],
                        skills=[],
                    )
                )
                return self.__build_response(
                    HTTPStatus.OK,
                    HirePersonResponseSerializer(
                        data={
                            'return_value': result.return_value,
                            'description': result.description,
                        }
                    ).initial_data,
                )
            else:
                self.__logger.error(f'Error was: {request_serializer.errors}')
                return self.__build_response(
                    HTTPStatus.BAD_REQUEST,
                    {
                        'return_value': 0,
                        'description': 'Unable to parse request body.',
                    },
                )
        except Exception as e:  # noqa: B902
            self.__logger.exception(e)
        return self.__build_response(
            HTTPStatus.INTERNAL_SERVER_ERROR,
            {},
        )

    @extend_schema(
        operation_id='get_known_persons',
        # parameters=[],
        # request=,
        responses={
            HTTPStatus.OK.value: GetPersonRequestSerializer,
            HTTPStatus.INTERNAL_SERVER_ERROR.value: GetPersonRequestSerializer,
        },
    )
    def get(self, request: Request) -> Response:
        """Return a list of all known peoples."""
        try:
            self.__logger.info('Requested all persons...')
            hr: HumanResources = HumanResources(self.__logger.getChild('Human Ressources'))
            serializer: GetPersonRequestSerializer = GetPersonRequestSerializer(
                data={'persons': [person.to_dict() for person in hr.get_all_persons()]}
            )
            if serializer.is_valid():
                return self.__build_response(
                    HTTPStatus.OK,
                    serializer.data,
                )
            else:
                self.__logger.error(f'The View was unable to dump the given Data... Error was: {serializer.errors}')
                return self.__build_response(
                    HTTPStatus.INTERNAL_SERVER_ERROR,
                    {
                        'persons': [],
                    },
                )

        except Exception as e:  # noqa: B902
            self.__logger.exception(e)
            return self.__build_response(
                HTTPStatus.INTERNAL_SERVER_ERROR,
                {
                    'persons': [],
                },
            )

    pass


# ---------------------------------------------------------------------------------------------------------------------
