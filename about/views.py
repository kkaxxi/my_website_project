from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def about_view(request):
    return HttpResponse('<h1>About Page</h1>')