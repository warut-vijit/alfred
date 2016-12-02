from django.shortcuts import render
from django.http import HttpResponse
from models import FoodRequest, Venue, User

# Create your views here.


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
    else:
        context = {'username': ' '}
    return render(request, 'index.html', context)


def index(request):
    return HttpResponse("Hello, world. You're at the homepage.")


def logout(request):
    if 'session' in request.COOKIES:
        response = HttpResponse("Successfully logged out.")
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
        return HttpResponse("Unable to process request: you are not logged in.")


def addvenue(request, venue='', phone=''):
    if 'session' in request.COOKIES:
        new_venue = Venue(name=venue, phone=phone)
        new_venue.save()
        return HttpResponse(str(Venue.objects.count())+" venues in system")
    else:
        return HttpResponse("Unable to process request: you are not logged in.")
