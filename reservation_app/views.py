from django.shortcuts import render
from django.http import Http404

days = {'Saturday': 'شنبه',
        'Sunday': 'یکشنبه',
        'Monday': 'دوشنبه',
        'Tuesday': 'سه شنبه',
        'Wednesday': 'چهارشنبه',
        'Thursday': 'پنج شنبه',
        'Friday': 'جمعه'}

def index(request):
    return render(request, 'reservation_app/index.html')

def register(request):
    return render(request, 'reservation_app/register.html')

def reserv(request):
    return render(request, 'reservation_app/reserv.html')

def time_slots(request, date):
    if date not in days:
        raise Http404('day does not found')
    else:
        day_in_persian = days[date]
        content = { 'date' : day_in_persian}
        return render(request, 'reservation_app/day_schedule.html', content)