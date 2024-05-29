from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def contact_view(request):
    return HttpResponse('<h1>Contact Page</h1>')