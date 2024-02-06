from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('cadastro/', views.register_view, name='cadastro'),
    path('login/', views.login, name='login'),
]
