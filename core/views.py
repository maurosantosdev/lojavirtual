# coding=utf-8
from django.shortcuts import render
from core.forms import ContactForm


def index(request):
    return render(request, 'index.html')


def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)