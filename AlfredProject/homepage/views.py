from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from models import FoodRequest, Venue, User

# Create your views here.


def auth(request):
    if 'session' in request.COOKIES:
        this_cookie = request.COOKIES['session']
        context = {'username': this_cookie.split(':')[1]}
        return render(request, 'index.html', context)
    return redirect("/auth")


def dev(request):
    if 'session' in request.COOKIES:
        this_cookie = request.COOKIES['session']
        context = {'username': this_cookie.split(':')[1]}
        return render(request, 'dev.html', context)
    return HttpResponse("Not logged in, no action taken")


def echo(request):
    if 'session' in request.COOKIES:
        this_cookie = request.COOKIES['session']
        context = {'username': this_cookie.split(':')[1]}
        return render(request, 'index.html', context)
    return redirect("/auth")


def index(request):
    return HttpResponse("Hello, world. You're at the homepage.")


def logout(request):
    if 'session' in request.COOKIES:
        response = render(request, 'logout.html')
        response.delete_cookie('session')
        return response
    return HttpResponse("Not logged in, no action taken")


def warn(request):
    return HttpResponse("<h1>Make sure you include a /echo/[a-z]</h1>")


def queryresp(request, venue='', order='', cost=''):
    if 'session' in request.COOKIES:
        user = request.COOKIES['session'].split(':')[1]
        user_id = User(name=user).objects.get(pk=1).id
        venue_id = Venue(name=venue).objects.get(pk=1).id
        new_request = FoodRequest(poster=user_id, venue=venue_id, item=order, cost=cost)
        new_request.save()
        return HttpResponse(str(FoodRequest.objects.count())+" requests being processed")
    else:
        return redirect("/auth")


def addvenue(request, venue='', phone=''):
    if 'session' in request.COOKIES:
        new_venue = Venue.objects.create(name=venue, phone=phone)
        new_venue.save()
        venues = [{'name':venue.name, 'phone':venue.phone} for venue in Venue.objects.all()]
        return HttpResponse(json.dumps(venues))
    else:
        return redirect("/auth")


def delvenue(request, venue=''):
    if 'session' in request.COOKIES:
        Venue.objects.filter(name=venue).delete()
        venues = [{'name': venue.name, 'phone': venue.phone} for venue in Venue.objects.all()]
        return HttpResponse(json.dumps(venues))
    else:
        return redirect("/auth")


def detail(request, name=''):
    if 'session' in request.COOKIES:
        try:
            userid = User.objects.get(name=name).id
        except User.DoesNotExist:
            userid = ""
        return HttpResponse(userid)
    else:
        return redirect("/auth")


def getvenue(request):
    if 'session' in request.COOKIES:
        venues = [{'name':venue.name, 'phone':venue.phone} for venue in Venue.objects.all()]
        return HttpResponse(json.dumps(venues))
    else:
        return redirect("/auth")


def adduser(request, name='', email=''):
    if 'session' in request.COOKIES:
        new_user = User.objects.create(name=name, email=email)
        new_user.save()
        users = [{'name':user.name, 'email':user.email} for user in User.objects.all()]
        return HttpResponse(json.dumps(users))
    else:
        return redirect("/auth")


def deluser(request, name=''):
    if 'session' in request.COOKIES:
        User.objects.filter(name=name).delete()
        users = [{'name': user.name, 'email': user.email} for user in User.objects.all()]
        return HttpResponse(json.dumps(users))
    else:
        return redirect("/auth")


def getuser(request):
    if 'session' in request.COOKIES:
        users = [{'name': user.name, 'email':user.email} for user in User.objects.all()]
        return HttpResponse(json.dumps(users))
    else:
        return redirect("/auth")