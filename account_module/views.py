from django.shortcuts import render
from django.views.generic import TemplateView
from reservation_module.models import Reservation


class AccountView(TemplateView):
    template_name = "account_module/account.html"
    model = Reservation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reservations"] = f"this is my reserve"
        return context
    


class RegisterView(TemplateView):
    template_name = "account_module/register.html"


