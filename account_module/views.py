from django.shortcuts import render
from django.views.generic import TemplateView


class AccountView(TemplateView):
    template_name = "account_module/account.html"


class RegisterView(TemplateView):
    template_name = "account_module/register.html"


