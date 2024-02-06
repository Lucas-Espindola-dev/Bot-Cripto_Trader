from django import forms
from traders.models import Traders


class TradersModelForm(forms.ModelForm):

    class Meta:
        model = Traders
        fields = '__all__'
