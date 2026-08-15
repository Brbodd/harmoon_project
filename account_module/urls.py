from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccountView.as_view(), name='account-page'),
    path('register/', views.RegisterView.as_view(), name='register-page')
]