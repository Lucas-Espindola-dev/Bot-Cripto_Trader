from django.urls import path
from traders import views

app_name = 'traders'

urlpatterns = [
    path('', views.home, name='home'),
    path('sala/', views.link_sala, name='link_sala'),
    path('plataforma/', views.plataforma, name='plataforma'),
]
