from django.urls import path
from traders import views

app_name = 'traders'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('new_trader/', views.NewTraderCreateView.as_view(), name='new_trader-view')
]
