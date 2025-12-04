"""Tests regarding a Person."""

# ---------------------------------------------------------------------------------------------------------------------

from http import HTTPStatus
from json import loads
from unittest import TestCase

from django.conf import settings
from requests import Response, get, post
from skillprofil.models.person import Person

# ---------------------------------------------------------------------------------------------------------------------


class CreatePerson(TestCase):
    """Testcases regarding Persons."""

    def __init__(self, *args, **kwargs):
        """C'tor."""
        super().__init__(*args, **kwargs)
        self.__url: str = settings.SYSTEMTEST['url']
        pass

    def setUp(self):
        Person.objects.all().delete()
        pass

    def tearDown(self):
        Person.objects.all().delete()
        pass

    def test_initial(self):
        """Test if the Webapp returns a set of Persons."""
        response: Response = get(f'{self.__url}persons/')
        self.assertEqual(HTTPStatus.OK, response.status_code)
        pass

    def test_create_person(self):
        """Test if it is possible to create a new Person."""
        response: Response = post(f'{self.__url}persons/', json={'name': 'max', 'surname': 'mustermann', 'skills': []})
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertEqual(1, loads(response.content.decode())['return_value'], msg=response.content.decode())
        pass

    pass


# ---------------------------------------------------------------------------------------------------------------------
