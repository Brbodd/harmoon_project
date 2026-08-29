from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from reservation_module.models import Reservation
from .forms import RegisterForm, LoginForm, PhoneNumberVerificationForm
from .models import User, PhoneVerification
from .services import sms_verify



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

                request.session["register_phone_number"] = user_phone_number

                return redirect(
                    reverse('phone-verify-page')
                )

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

                request.session["register_phone_number"] = user_phone_number
                request.session["register_full_name"] = user_full_name

                sms_verify.send_otp(user_phone_number)

                return redirect(
                    reverse("phone-verify-page")
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


class PhoneNumberVerificationView(TemplateView):

    template_name = "account_module/number_verify.html"

    def post(self, request):

        phone_number_form = PhoneNumberVerificationForm(
            request.POST
        )

        if phone_number_form.is_valid():

            code = (
                phone_number_form.cleaned_data["code_input_1"]
                + phone_number_form.cleaned_data["code_input_2"]
                + phone_number_form.cleaned_data["code_input_3"]
                + phone_number_form.cleaned_data["code_input_4"]
                + phone_number_form.cleaned_data["code_input_5"]
            )

            phone_number = request.session.get(
                "register_phone_number"
            )

            verification = PhoneVerification.objects.filter(
                phone_number=phone_number,
                code=code
            ).last()

            if verification:

                full_name = request.session.get(
                    "register_full_name"
                )

                user = User.objects.create(
                    username=phone_number,
                    phone_number=phone_number,
                    first_name=full_name
                )

                user.set_unusable_password()
                user.save()

                login(request, user)

                request.session.pop(
                    "register_phone_number",
                    None
                )

                request.session.pop(
                    "register_full_name",
                    None
                )

                verification.delete()

                return redirect(
                    reverse("Harmoon-Home")
                )

            phone_number_form.add_error(
                None,
                "کد وارد شده صحیح نیست."
            )

        context = {
            "phone_number_form": phone_number_form
        }

        return render(
            request,
            self.template_name,
            context
        )