"""Model for a skill."""
# ---------------------------------------------------------------------------------------------------------------------
from django.db.models import CASCADE, CharField, ForeignKey, IntegerChoices, IntegerField, Model
from skillprofil.models.person import Person

# ---------------------------------------------------------------------------------------------------------------------


class Domain(IntegerChoices):
    """Enum for different domains."""

    UNAPPLICABLE = 0
    AGILE_ADVISORY = 1
    VIABLE_ARCHITECTURE = 2
    PRAGMATIC_DEVELOPMENT = 3

    pass


# ---------------------------------------------------------------------------------------------------------------------


class Skill(Model):
    """Model class.

    One Person cann have multiple Skills.
    """

    name = CharField(max_length=256)
    description = CharField(max_length=1024)
    points = IntegerField(default=0)
    domain = IntegerField(default=Domain.UNAPPLICABLE.value, choices=Domain.choices)
    person = ForeignKey(to=Person, on_delete=CASCADE)

    pass


# ---------------------------------------------------------------------------------------------------------------------
