from django.shortcuts import render, redirect
from django.http import HttpResponse
from feed.models import Feed
from feed.forms import Feedform
from datetime import date
from django.contrib.auth.decorators import login_required
from .decorators import custom_login_required


# Create your views here.



@custom_login_required
def feed_list(request):
    # get all feeds from the db
    feeds = Feed.objects.all()
    return render (request, "feed_list.html", {"feeds": feeds})

def s_feed(request,id):
    feed = Feed.objects.get(id=id)
    return render(request, "s_feed.html", {"feed": feed})

@login_required
def create_feed(request):
    if(request.method == 'POST'):
        form = Feedform(request.POST)
        if form.is_valid():
            feed = form.save(commit=False) #pseudo save
            feed.user = request.user  # Assign logged-in user
            feed.published_date = date.today()
            form.save() #full save
            return redirect("feed_list")
    else:
        # for GET request
        form = Feedform()
    return render(request, "create_feed.html", {"form" : form})

@login_required
def edit_feed(request,id):
    feed = Feed.objects.get(id=id) 
    if feed.user != request.user:
        return HttpResponse("Unauthorized", status=401)
    
    if(request.method == 'POST'):
        form = Feedform(request.POST, instance=feed)
        if form.is_valid():
            feed = form.save(commit=False) #pseudo save
            feed.published_date = date.today()
            form.save() #full save
            return redirect("feed_list")
    else:
        # for GET request
        form = Feedform(instance=feed)
        return render(request, "edit_feed.html", {"form" : form})
    
@login_required
def delete_feed(request,id):
    feed = Feed.objects.get(id=id) 
    if feed.user == request.user:
        feed.delete()
        return redirect("feed_list")
    return HttpResponse("Unauthorized", status=401)

def welcome_feed(request):
    feeds = Feed.objects.all()
    return render(request, 'welcome_feed.html')

def unauthorized(request):
    return render(request, 'unauthorized.html')

