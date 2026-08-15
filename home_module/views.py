from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView

days = {'Saturday': 'شنبه',
        'Sunday': 'یکشنبه',
        'Monday': 'دوشنبه',
        'Tuesday': 'سه شنبه',
        'Wednesday': 'چهارشنبه',
        'Thursday': 'پنج شنبه',
        'Friday': 'جمعه'}

class IndexView(TemplateView):
    template_name = "home_module/index.html"

def time_slots(request, date):
    if date not in days:
        raise Http404('day does not found')
    else:
        day_in_persian = days[date]
        content = { 'date' : day_in_persian}
        return render(request, 'home_module/day_schedule.html', content)