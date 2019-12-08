from django.core.exceptions import ValidationError

# def validate_author_email(value):
#     if not "@" in value:
#         raise ValidationError("Not a valid email")
#     return value

def validate_norah(value):
    if not "norah" in value:
        raise ValidationError("Not norah")
    return value
        