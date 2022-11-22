from django.contrib.auth.forms import AuthenticationForm
from django.forms import CharField, EmailField, PasswordInput


class LoginForm(AuthenticationForm):
    pass

# class LoginForm(AuthenticationForm):
#     phone = CharField(max_length=25)
#     email = EmailField(max_length=255)
#     password = CharField(widget=PasswordInput(attrs={"autocomplete": "current-password"}),)
#     confirm_password = CharField(widget=PasswordInput(attrs={"autocomplete": "current-password"}),)
#

