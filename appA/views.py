from django.shortcuts import render

from .forms import employee,sample,car_gallery
from .models import car_model


# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request,'A.html',{'title':'Django','link':'http://127.0.0.1:8000/'})

def profile(request):
    return render(request,'A.html',{'title':'profile page','link':'http://youtube.com'})

def expression(request):
    form = employee()
    #a = int(request.POST['text1'])
    #b = int(request.POST['text2'])
    #c = a+b
    #return render(request,'Output.html',{'result':c})
    return render(request,'Output.html',{'form':form})



def sample_exp(request):
    form = sample()
    return render(request,'Output.html',{'form':form})

def car(request):
    if request.method == 'POST':
        form = car_gallery(request.POST)
        if form.is_valid():
            form.save()
    form = car_gallery()
    return render(request,'Output.html',{'form':form})
