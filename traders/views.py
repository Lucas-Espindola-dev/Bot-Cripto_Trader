from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def home(request):
    return render(request, 'pages/home.html')


@method_decorator(login_required(login_url='accounts:login'), name="dispatch")
def link_sala(request):
    return render(request, 'pages/link_sala.html')


def plataforma(request):
    return render(request, 'pages/plataforma.html')





