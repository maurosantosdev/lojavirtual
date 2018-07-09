# coding=utf-8

from django import forms
from django.core.mail import send_mail
from django.conf import settings


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