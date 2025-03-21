"""Interface to a Persistance Layer."""
# ---------------------------------------------------------------------------------------------------------------------
from abc import ABC, abstractmethod
from dataclasses import dataclass
from logging import Logger, getLogger
from typing import List, Optional

from kickstarter_business_logic.human_ressources.human_ressource_types import PersonRepr, SkillRepr


# ---------------------------------------------------------------------------------------------------------------------
class IHumanResourcesPersistance(ABC):
    """Interfacedefinition for Persistance Access."""

    @abstractmethod
    def find_person_by_name(self, firstname: str, surename: str) -> Optional[PersonRepr]:
        """Find a Person by his First- and Secondname.

        Returns:
            Optional[PersonRepr]: A Representationobject if the given Person was found and None otherwise.
        """
        pass

    @abstractmethod
    def persist_person(self, person: PersonRepr) -> bool:
        """Persist a Person.

        Returns:
            bool: True on success and False otherwise.
        """
        pass

    @abstractmethod
    def all_persons(self) -> List[PersonRepr]:
        """Return all persisted Persons."""
        pass

    pass


# ---------------------------------------------------------------------------------------------------------------------
