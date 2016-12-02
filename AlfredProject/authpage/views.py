from django.shortcuts import render, redirect
import random
import hashlib

# Create your views here.


def auth_main(request):
    return render(request, 'auth_main.html')


def auth_verify(request, username='', password=''):
    if username == 'username' and password == 'password':
        response = redirect("/home/echo")
        username_hash = hashlib.sha224(username).hexdigest()
        response.set_cookie('session', username_hash+':'+username)
        return response
    return redirect("/auth/err/"+username)


def auth_err(request, username=''):
    context = {'Username': username}
    return render(request, 'auth_err.html', context)
