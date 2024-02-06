from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def home(request):
    return render(request, 'pages/home.html')


@method_decorator(login_required(login_url='accounts:login'))
def link_sala(request):
    return render(request, 'pages/link_sala.html')





