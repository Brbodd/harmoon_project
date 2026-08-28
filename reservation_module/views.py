from django.views.generic import TemplateView
from datetime import timedelta
from django.utils import timezone
from datetime import datetime
import jdatetime


class ReservationView(TemplateView):
    template_name = "reservation_module/reservation.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        today = timezone.localdate()

        days = []

        week_days = {
            0: "دوشنبه",
            1: "سه‌شنبه",
            2: "چهارشنبه",
            3: "پنجشنبه",
            4: "جمعه",
            5: "شنبه",
            6: "یکشنبه",
        }

        for i in range(20):

            date = today + timedelta(days=i)

            jalali_date = jdatetime.date.fromgregorian(
                date=date
            )

            days.append({
                "date": date,
                "day": week_days[date.weekday()],
                "number": jalali_date.day,
                "month": jalali_date.month,
                "year": jalali_date.year,
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

        date = datetime.strptime(
            kwargs["date"],
            "%Y-%m-%d"
        ).date()

        jalali_date = jdatetime.date.fromgregorian(
            date=date
        )

        context["times"] = times
        context["date"] = kwargs["date"]
        context["jalali_date"] = jalali_date

        return context
