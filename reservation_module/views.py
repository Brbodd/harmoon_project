from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from datetime import timedelta
from django.utils import timezone
from datetime import datetime

from .models import Reservation

import jdatetime

from .services import send_to_barber


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

        date = datetime.strptime(
            kwargs["date"],
            "%Y-%m-%d"
        ).date()

        jalali_date = jdatetime.date.fromgregorian(
            date=date
        )

        reserved_times = Reservation.objects.filter(
            date=date
        ).values_list("time", flat=True)

        reserved_times = [
            time.strftime("%H:%M")
            for time in reserved_times
        ]

        now = timezone.localtime()
        today = timezone.localdate()

        times = self.get_available_times(
            date,
            today,
            now
        )

        context["times"] = times
        context["date"] = kwargs["date"]
        context["jalali_date"] = jalali_date
        context["reserved_times"] = reserved_times
        context["now"] = now

        return context

    def get_available_times(self, date, today, now):

        if date != today:
            return self.get_all_times()

        return self.get_today_times(now)

    def get_all_times(self):

        times = []

        for hour in range(10, 21):
            times.append(f"{hour}:00")
            times.append(f"{hour}:30")

        return times

    def get_today_times(self, now):

        times = []

        start_hour = now.hour

        if now.minute < 30:
            start_minute = 30
        else:
            start_hour += 1
            start_minute = 0

        for hour in range(start_hour, 21):

            if hour == start_hour and start_minute == 30:
                times.append(f"{hour}:30")
            else:
                times.append(f"{hour}:00")
                times.append(f"{hour}:30")

        return times


class CreateReservationView(LoginRequiredMixin, View):

    def get(self, request, date, time):

        date = datetime.strptime(
            date,
            "%Y-%m-%d"
        ).date()

        time = datetime.strptime(
            time,
            "%H:%M"
        ).time()



        if Reservation.objects.filter(
            date=date,
            time=time
        ).exists():

            return redirect("reservation")

        Reservation.objects.create(
            user=request.user,
            date=date,
            time=time
        )

        try:

            send_to_barber.send_booking_sms(
                full_name=request.user.first_name,
                phone_number=request.user.phone_number,
                reserv_date=date,
                reserv_time=time
            )

        except Exception as e:
            print("SMS ERROR:", repr(e))

        return redirect("reservation")