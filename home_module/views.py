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