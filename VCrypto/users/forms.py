from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms


def validate_bitcoin_address(value):
    # Add your Bitcoin address validation logic here
    if not value.startswith('1'):
        raise ValidationError('Неправильный адрес кошелька')


class UserRegisterForm(UserCreationForm):
    bitcoin_address = forms.CharField(max_length=100, required=True, validators=[validate_bitcoin_address],
                                      error_messages={'required': 'Адрес кошелька обязателен'})

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'bitcoin_address']
