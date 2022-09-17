#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("<br><br><center>Hello, world. You're at the ultimate-social app <br> sql connection successful<center>")