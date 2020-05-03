# coding=utf-8
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from core.forms import ContactForm
from django.contrib import messages
from django.views import generic
from watson import search as watson

from catalog.models import Product

User = get_user_model()


class IndexView(generic.ListView):

    template_name = 'index.html'

    paginate_by = 10

    # Pesquisando no formulario de pesquisa (Filtrando pelo título do Produto | pelo nome da Categoria | pela descrição do produto

    def get_queryset(self):
        queryset = Product.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            queryset = watson.filter(queryset, q)
        return queryset


index = IndexView.as_view()


def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido')
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)


class RegisterView(CreateView):

    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    model = User
    success_url = reverse_lazy('index')


register = RegisterView.as_view()