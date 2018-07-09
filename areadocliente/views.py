from django.shortcuts import render

# Create your views here.


def areadocliente(request):
    return render(request, 'cliente/home.html')