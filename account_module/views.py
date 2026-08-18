from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from reservation_module.models import Reservation
from .forms import RegisterForm


class AccountView(TemplateView):
    template_name = "account_module/account.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reservations = Reservation.objects.filter(user=self.request.user)
        context["reservations"] = reservations
        return context
    
    


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            pass

        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)

    


