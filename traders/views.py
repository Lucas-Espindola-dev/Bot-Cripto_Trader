from django.shortcuts import render
from django.views.generic import CreateView
from traders.models import Traders
from traders.forms import TradersModelForm


def home(request):
    return render(request, 'pages/home.html')





