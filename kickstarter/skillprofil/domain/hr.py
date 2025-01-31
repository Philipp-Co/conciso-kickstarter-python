"""The Human Ressources is implemented in this file."""
# ---------------------------------------------------------------------------------------------------------------------
from dataclasses import dataclass
from logging import Logger, getLogger
from typing import List, Optional

from skillprofil.models.person import Person
from skillprofil.models.skill import Domain

# ---------------------------------------------------------------------------------------------------------------------


@dataclass
class SkillRepr:
    """Dataclass for skills."""

    name: str
    description: str
    points: int
    domain: str

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'points': self.points,
            'domain': self.domain,
        }

    pass


# ---------------------------------------------------------------------------------------------------------------------


@dataclass
class PersonRepr:
    """Dataclass for persons."""

    name: str
    surname: str
    skills: List[SkillRepr]

    def to_dict(self):
        return {
            'name': self.name,
            'surname': self.surname,
            'skills': [skill.to_dict() for skill in self.skills],
        }

    pass


# ---------------------------------------------------------------------------------------------------------------------
@dataclass
class HirePersonResult:
    """iDataclass for the Result of the a hiring process."""

    return_value: int
    description: str

    pass


# ---------------------------------------------------------------------------------------------------------------------


class HumanResources:
    """The Human Ressources Department."""

    def __init__(self, logger: Optional[Logger]):
        self.__logger: Logger = logger if logger is not None else getLogger(self.__class__.__name__)
        pass

    def logger(self) -> Logger:
        return self.__logger

    def hire(self, person: PersonRepr) -> HirePersonResult:
        """Check if someone with the same name already is part of this company and if not hire the person!"""
        return_value: int = 0
        description: str = 'Unable to hire you!'

        try:
            self.__logger.info(f'Hire Person {person.name}, {person.surname}')

            model: Person = Person()
            model.name = person.name
            model.surname = person.surname
            model.save()

            return_value = 1
            description = 'You are hired!'

        except Exception as e:  # noqa: B902
            self.__logger.exception(e)

        return HirePersonResult(
            return_value=return_value,
            description=description,
        )

    def get_all_persons(self) -> List[PersonRepr]:
        """Return a list of all known persons."""
        result: List[PersonRepr] = []
        for person in Person.objects.all():
            result.append(
                PersonRepr(
                    name=person.name,
                    surname=person.surname,
                    skills=[
                        SkillRepr(
                            name=skill.name,
                            description=skill.description,
                            points=skill.points,
                            domain=Domain(skill.domain).name,
                        )
                        for skill in person.skill_set.all()
                    ],
                )
            )
        return result

    def find_person(self, name: str) -> Optional[PersonRepr]:
        """Find a person by name."""
        return None

    pass


# ---------------------------------------------------------------------------------------------------------------------
