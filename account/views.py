# coding=utf-8

from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, TemplateView, UpdateView, FormView
)
from .models import User
from .forms import UserAdminCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/index.html'


class RegisterView(CreateView):

    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')


class UpdateUserView(LoginRequiredMixin, UpdateView):

    model = User
    template_name = 'accounts/update_user.html'
    fields = ['name', 'email']
    success_url = reverse_lazy('account:index')

    def get_object(self):
        return self.request.user


class UpdateAddressView(LoginRequiredMixin, UpdateView):

    model = User
    template_name = 'accounts/update_address.html'
    fields = ['rua', 'numero', 'complemento', 'bairro']
    success_url = reverse_lazy('account:index')

    def get_object(self):
        return self.request.user


class UpdatePasswordView(LoginRequiredMixin, FormView):

    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('account:index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)


index = IndexView.as_view()
register = RegisterView.as_view()
update_user = UpdateUserView.as_view()
update_password = UpdatePasswordView.as_view()
update_address = UpdateAddressView.as_view()