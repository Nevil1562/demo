from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def home(request):
    # return HttpResponse("<h2>Hello, Welcome to Django!</h2>")
    return render(request, 'home.html')