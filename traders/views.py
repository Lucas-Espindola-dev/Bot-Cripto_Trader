from django.shortcuts import render
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from traders.models import Traders
from traders.forms import TradersModelForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
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





