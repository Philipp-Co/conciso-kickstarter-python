"""Serializers for person API."""
# ---------------------------------------------------------------------------------------------------------------------
from rest_framework.serializers import CharField, IntegerField, Serializer

# ---------------------------------------------------------------------------------------------------------------------


class SkillSerializer(Serializer):
    """Serializer."""

    name = CharField(required=True)
    description = CharField(required=True)
    points = IntegerField(required=True)
    domain = CharField(required=True)

    pass


# ---------------------------------------------------------------------------------------------------------------------


class PersonSerializer(Serializer):
    """Serializer."""

    name = CharField(required=True)
    surname = CharField(required=True)
    skills = SkillSerializer(many=True, default=[])

    pass


# ---------------------------------------------------------------------------------------------------------------------


class GetPersonRequestSerializer(Serializer):
    """Serializer."""

    persons = PersonSerializer(many=True)

    pass


# ---------------------------------------------------------------------------------------------------------------------


class HirePersonRequestSerializer(PersonSerializer):
    """Serializer."""

    pass


# ---------------------------------------------------------------------------------------------------------------------


class HirePersonResponseSerializer(Serializer):
    """Serializer."""

    return_value = IntegerField(required=True)
    description = CharField(required=True)

    pass


# ---------------------------------------------------------------------------------------------------------------------
