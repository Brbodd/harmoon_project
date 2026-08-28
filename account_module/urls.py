from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccountView.as_view(), name='account-page'),
    path('login/', views.LoginView.as_view(), name='login-page'),
    path('logout/', views.LogoutView.as_view(), name='logout-page'),
    path('phone_verify/', views.PhoneNumberVerificationView.as_view(), name='phone-verify-page'),
    path('register/', views.RegisterView.as_view(), name='register-page')
]