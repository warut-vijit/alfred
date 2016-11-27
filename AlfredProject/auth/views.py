from django.shortcuts import render, redirect

# Create your views here.


def auth_main(request):
    return render(request, 'auth_main.html')


def auth_verify(request, username='', password=''):
    if username == 'username' and password == 'password':
        return redirect("/home/echo/khan")
    return redirect("/auth/err/"+username)


def auth_err(request, username=''):
    context = {'Username': username}
    return render(request, 'auth_err.html', context)
