# coding=utf-8

from django import forms
from django.contrib.auth.forms import UsernameField
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', widget=forms.TextInput(attrs={'placeholder': 'Nome', 'class': 'form-control'}))
    email = forms.EmailField(label='Email',
                             widget=forms.TextInput(attrs={'placeholder': 'E-mail', 'class': 'form-control'}))
    message = forms.CharField(label='Mensagem',
                              widget=forms.Textarea(
                                  attrs={'placeholder': 'Mensagem', 'class': 'form-control', 'cols': 60, 'rows': 5}))

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        message = 'Nome: {0}\nE-mail:{1}\n{2}'.format(name, email, message)
        send_mail(
            'Contato E-commerce Django', message, settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL]
        )


class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    username = UsernameField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'E-mail', 'class': 'form-control'}),
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': True, 'placeholder': 'Senhaa', 'class': 'form-control'}),
    )