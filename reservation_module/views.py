from django.shortcuts import render
from django.views.generic import TemplateView


class ReservationView(TemplateView):
    template_name = "reservation_module/reservation.html"
