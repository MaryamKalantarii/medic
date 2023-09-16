from django.shortcuts import render,redirect
from .models import NewsLetter,ContactUs,Services,HealthService,Doctor,Building
from .forms import NewsLetterForm,ContactUsForm
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method =='GET':
       
        services = Services.objects.filter(status=True)
        healthService=HealthService.objects.filter(status=True)
        doctor = Doctor.objects.filter(status=True)
        context = {
            'service':services,
            'healthService':healthService,
            'doctor':doctor,
        }
        return render(request,"root/index.html",context=context)
    elif request.method == 'POST' and len(request.POST) == 2 :
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'your email submited')
            return redirect('root:home')   
        else :
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect('root:home')
        
    elif request.method == 'POST' and len(request.POST) > 2 :
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'we received your message and call with you as soon')
            return redirect('/')   
        else :
            messages.add_message(request,messages.ERROR,'Invalid data')
            return redirect('/')
