# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def comp_alert(request):
    return render(request, "components-alerts.html")

def usr_profile(request):
    return render(request,"users-profile.html")