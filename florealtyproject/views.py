from .forms import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponse

def register_user(request):
    if(request.method == 'POST'):
    
        form = RegistrationForm(request.POST)

        if (form.is_valid()):
            user = form.save() 
            login(request, user) #login the user automatically
            return redirect("feed_list")
    else:
        # for GET request
    
        form = RegistrationForm()
    return render(request, "register.html", {"form" : form})

def homepage(request):
   return render(request, "welcome_feed.html")

def aboutpage(request):
    return HttpResponse("This Page is About FloRealty")

def contactuspage(request):
    return HttpResponse("Click Here to Contact Us")

def servicespage(request):
    return HttpResponse("Here are the Variuos Services we Render")
    
    