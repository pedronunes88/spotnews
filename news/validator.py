from django.core.exceptions import ValidationError


def validate_even(value):
    if len(value) == 0 or len(value) < 200:
        raise ValidationError(
            "The length of the text should be greater than 200."
        )  # copilot tentou fazer por pares primeiro, ai ajeitei pro requisito
