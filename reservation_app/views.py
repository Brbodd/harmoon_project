from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'reservation_app/index.html')

def register(request):
    return render(request, 'reservation_app/register.html')

def reserv(request):
    return render(request, 'reservation_app/reserv.html')