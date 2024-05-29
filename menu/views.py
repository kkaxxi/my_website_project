from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def menu_view(request):
    return HttpResponse('<h1>Menu Page</h1>')


def index(request):
    return render(request, 'welcome.html')
