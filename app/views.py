from django.shortcuts import render
from . models import demo_v1
# Create your views here.

def index(request):
    obj = demo_v1.objects.all()
    return render(request,'index.html',{'result':obj})

