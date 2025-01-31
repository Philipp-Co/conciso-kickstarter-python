"""Model for a person."""
# ---------------------------------------------------------------------------------------------------------------------
from django.db.models import CharField, Model

# ---------------------------------------------------------------------------------------------------------------------


class Person(Model):
    """Model class."""

    class Meta:
        """Django Meta class."""

        unique_together = (
            'name',
            'surname',
        )
        pass

    name = CharField(max_length=64)
    surname = CharField(max_length=64)

    pass


# ---------------------------------------------------------------------------------------------------------------------
