from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReservationView.as_view(), name="reservation"),
    path("day/<str:date>/", views.DayScheduleView.as_view(), name="reservation-day"),
]
