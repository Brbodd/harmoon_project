from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from reservation_module.models import Reservation
from .forms import RegisterForm, LoginForm
from .models import User


class AccountView(LoginRequiredMixin, TemplateView):
    template_name = "account_module/account.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        reservations = Reservation.objects.filter(
            user=self.request.user
        )

        context["reservations"] = reservations

        return context


class LoginView(View):

    def get(self, request):

        login_form = LoginForm()

        context = {
            'login_form': login_form
        }

        return render(
            request,
            'account_module/login.html',
            context
        )

    def post(self, request):

        login_form = LoginForm(request.POST)

        if login_form.is_valid():

            user_phone_number = login_form.cleaned_data.get('phone_number')

            user: User = User.objects.filter(
                phone_number=user_phone_number
            ).first()

            if user is not None:

                login(request, user)

                return redirect(reverse('Harmoon-Home'))

            else:
                login_form.add_error(
                    'phone_number',
                    'لطفا ابتدا ثبت نام کنید.'
                    )
        else:
            login_form.add_error('phone_number', 'کاربری یافت نشد.')

        context = {
            'login_form': login_form
        }

        return render(
            request,
            'account_module/login.html',
            context
        )



class RegisterView(View):

    def get(self, request):
        register_form = RegisterForm()

        context = {
            'register_form': register_form
        }

        return render(
            request,
            'account_module/register.html',
            context
        )

    def post(self, request):

        register_form = RegisterForm(request.POST)

        if register_form.is_valid():

            user_phone_number = register_form.cleaned_data.get(
                'phone_number'
            )

            user_full_name = register_form.cleaned_data.get(
                'full_name'
            )

            user_exists = User.objects.filter(
                phone_number=user_phone_number
            ).exists()

            if user_exists:

                register_form.add_error(
                    'phone_number',
                    'این شماره تلفن قبلاً ثبت شده است.'
                )

            else:

                new_user = User(
                    username=user_phone_number,
                    phone_number=user_phone_number,
                    first_name=user_full_name
                )

                new_user.set_unusable_password()
                new_user.save()

                login(request, new_user)

                return redirect(
                    reverse('Harmoon-Home')
                )

        context = {
            'register_form': register_form
        }

        return render(
            request,
            'account_module/register.html',
            context
        )

class LogoutView(View):

    def get(self, request):

        logout(request)
        
        return redirect(reverse('Harmoon-Home'))