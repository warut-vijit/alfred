from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def echo(request, text=''):
    context = {'input': text}
    return render(request, 'index.html', context)


def index(request):
    return HttpResponse("Hello, world. You're at the homepage.")


def warn(request):
    return HttpResponse("<h1>Make sure you include a /echo/[a-z]</h1>")
