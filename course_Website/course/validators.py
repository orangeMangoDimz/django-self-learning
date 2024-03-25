from django.core.exceptions import ValidationError

def validate_title(value):
    if value == "abc":
        raise ValidationError(value + " cannot be used!")