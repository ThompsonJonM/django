from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    html = '<h1> BOBOP </h1>'
    return HttpResponse(html)

