from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def Zapal(request):
    context={
        'zapallar':Zapallar.objects.all()
    }
    return render(request,'zapal.html',context)
