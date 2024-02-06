from django.shortcuts import render
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from traders.models import Traders
from traders.forms import TradersModelForm


def home(request):
    trader = get_object_or_404(Traders, pk=id)
    return render(request, 'pages/home.html', context={
        'trader': trader,
    })


class NewTraderCreateView(CreateView):
    model = Traders
    form_class = TradersModelForm
    template_name = 'pages/new_trader.html'
    success_url = 'home'





