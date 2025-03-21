"""The Human Ressources is implemented in this file."""
# ---------------------------------------------------------------------------------------------------------------------
from abc import ABC, abstractmethod
from dataclasses import dataclass
from logging import Logger, getLogger
from typing import List, Optional

from kickstarter_business_logic.human_ressources.human_ressource_types import PersonRepr, SkillRepr
from kickstarter_business_logic.human_ressources.ihuman_ressources import IHumanResourcesPersistance


# ---------------------------------------------------------------------------------------------------------------------
@dataclass
class HirePersonResult:
    """Dataclass for the Result of the a hiring process."""

    return_value: int
    description: str

    pass


# ---------------------------------------------------------------------------------------------------------------------


class HumanResources:
    """The Human Ressources Department."""

    def __init__(
        self,
        logger: Optional[Logger],
        persistance: IHumanResourcesPersistance,
    ):
        self.__logger: Logger = logger if logger is not None else getLogger(self.__class__.__name__)
        self.__persistance: HumanResourcesPersistance = persistance
        pass

    def logger(self) -> Logger:
        return self.__logger

    def hire(self, person: PersonRepr) -> HirePersonResult:
        """Check if someone with the same name already is part of this company and if not hire the person!"""
        return_value: int = 0
        description: str = 'Unable to hire you!'

        try:
            self.__logger.info(f'Hire Person {person.name}, {person.surname}')

            if self.__persistance.find_person_by_name(person.name, person.surname) is None:
                self.__persistance.persist_person(person)
                return_value = 1
                description = 'You are hired!'
            else:
                return_value = 0
                description = 'We already know you!'

        except Exception as e:  # noqa: B902
            self.__logger.exception(e)

        return HirePersonResult(
            return_value=return_value,
            description=description,
        )

    def persons(self) -> List[PersonRepr]:
        """Return a list of all known persons."""
        return self.__persistance.all_persons()

    def find_person(self, name: str, surname: str) -> Optional[PersonRepr]:
        """Find a person by name."""
        return self.__persistance.find_person_by_name(name, surname)

    pass


# ---------------------------------------------------------------------------------------------------------------------
