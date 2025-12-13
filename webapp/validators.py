from django.core.exceptions import ValidationError
import re


def validate_summary_capital(value):
    if not value[0].isupper():
        raise ValidationError('Краткое описание должно начинаться с заглавной буквы.')


def validate_description_english(value):
    if value:
        pattern = r'^[A-Za-z0-9\s.,!?:;"\'-]*$'
        if not re.fullmatch(pattern, value):
            raise ValidationError('Описание должно быть на английском языке')