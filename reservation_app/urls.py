from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Harmoon-Home'),
    path('register', views.register, name='Login-Harmoon-Barber'),
    path('reservation', views.reserv, name='Book-Harmoon-Appointment')
]
