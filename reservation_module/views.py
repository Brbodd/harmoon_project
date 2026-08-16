from django.views.generic import TemplateView
from datetime import timedelta
from django.utils import timezone


class ReservationView(TemplateView):
    template_name = "reservation_module/reservation.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        today = timezone.localdate()

        days = []

        for i in range(20):

            date = today + timedelta(days=i)

            days.append({
                "date": date,
                "day": date.strftime("%A"),
                "number": date.day,
            })

        context["days"] = days

        return context

class DayScheduleView(TemplateView):

    template_name = "reservation_module/day_schedule.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        times = [
            "10:00",
            "10:30",
            "11:00",
            "11:30",
            "12:00",
            "12:30",
            "13:00",
            "13:30",
            "14:00",
            "14:30",
            "15:00",
            "15:30",
            "16:00",
            "16:30",
            "17:00",
            "17:30",
            "18:00",
            "18:30",
        ]

        context["times"] = times
        context["date"] = kwargs["date"]

        return context
