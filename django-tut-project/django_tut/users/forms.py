from django.contrib import auth
from django.contrib.auth import forms
from django.forms import Form
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.fields import CharField
from django.contrib.auth.models import User
from django.forms import ModelForm, BaseForm



class AuthenticationForm(AuthenticationForm):

    class Meta:
        model = User
        declared_fields = ['username','email']

    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required':'{fieldname} is required'.format(fieldname=field.label)}

class signin(LoginView):
    authentication_form = AuthenticationForm
    template_name = 'users/signin.html'
    # authentication_form = LoginForm
    # class Meta: