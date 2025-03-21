"""Types used by the Human Resources Department."""
# ---------------------------------------------------------------------------------------------------------------------
from dataclasses import dataclass
from typing import List

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
