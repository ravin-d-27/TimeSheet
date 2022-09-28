from django.shortcuts import render, redirect
from .models import Times
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'times/home.html')

@login_required(login_url = "/accounts/login")
def update(request):
        if request.method == 'POST':
            if request.POST['description'] and request.POST['approval'] :
                times = Times()
                times.description = request.POST['description']
                times.approved = request.POST['approval']

                times.pub_date = timezone.datetime.now()
                times.user = request.user

                times.save()
                return redirect("")
            else:
                return render(request,'times/update.html',{'error':'All Fields are required!'})

        else:
            return render(request,'times/update.html')
