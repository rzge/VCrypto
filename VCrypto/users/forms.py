from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms

from validators import btc_address


def validate_bitcoin_address(value):
    if not btc_address(value):
        raise ValidationError('Неправильный адрес кошелька')


class UserRegisterForm(UserCreationForm):
    bitcoin_address = forms.CharField(max_length=100, required=True, validators=[validate_bitcoin_address],
                                      error_messages={'required': 'Адрес кошелька обязателен'})

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'bitcoin_address']
