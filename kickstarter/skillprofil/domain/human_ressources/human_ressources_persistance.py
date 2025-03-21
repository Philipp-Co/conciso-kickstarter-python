"""Implements the Persistance Layer for the Businesslayer."""

# ---------------------------------------------------------------------------------------------------------------------
from logging import Logger, getLogger
from typing import List, Optional

from django.db.transaction import atomic
from skillprofil.models.person import Person
from skillprofil.models.skill import Domain, Skill

from kickstarter_business_logic.human_ressources.ihuman_ressources import (
    IHumanResourcesPersistance,
    PersonRepr,
    SkillRepr,
)

# ---------------------------------------------------------------------------------------------------------------------


class DjangoPersistance(IHumanResourcesPersistance):
    """Persinstance with Django."""

    def __init__(self, logger: Optional[Logger] = None):
        super().__init__()
        self.__logger: Logger = logger if logger is not None else getLogger(self.__class__.__name__)
        pass

    def find_person_by_name(self, firstname: str, surname: str) -> Optional[PersonRepr]:
        try:
            person: Person = Person.objects.get(name=firstname, surname=surname)
            return PersonRepr(
                name=firstname,
                surname=surname,
                skills=[
                    SkillRepr(
                        name=skill.name,
                        description=skill.description,
                        points=skill.points,
                        domain=skill.domain.name,
                    )
                    for skill in person.skill_set.all()
                ],
            )
        except Exception as e:
            self.__logger.exception(e)
            return None
        pass

    @atomic
    def persist_person(self, person: PersonRepr) -> bool:
        try:
            new_person: Person = Person(name=person.name, surname=person.surname)
            new_person.save()

            skill: SkillRepr
            for skill in person.skills:
                new_skill: Skill = Skill(
                    person=new_person,
                    name=skill.name,
                    description=skill.description,
                    points=skill.points,
                    domain=Domain[skill.domain.upper()],
                )
                new_skill.save()
            return True
        except Exception as e:
            self.__logger.exception(e)
            return False
        pass

    def all_persons(self) -> List[PersonRepr]:
        return [
            PersonRepr(
                name=person.name,
                surname=person.surname,
                skills=[
                    SkillRepr(
                        name=skill.name,
                        description=skill.description,
                        points=skill.points,
                        domain=skill.domain.name,
                    )
                    for skill in person.skill_set.all()
                ],
            )
            for person in Person.objects.all()
        ]

    pass


# ---------------------------------------------------------------------------------------------------------------------
