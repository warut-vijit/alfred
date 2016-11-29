from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def echo(request, text=''):
    if 'session' in request.COOKIES:
        this_cookie = request.COOKIES['session']
        context = {'input': text, 'username': this_cookie.split(':')[1]}
    else:
        context = {'input': 'Failed to log in', 'username': ' '}
    return render(request, 'index.html', context)


def index(request):
    return HttpResponse("Hello, world. You're at the homepage.")


def warn(request):
    return HttpResponse("<h1>Make sure you include a /echo/[a-z]</h1>")
