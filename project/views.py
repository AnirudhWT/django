from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')
    # return HttpResponse("this is home page")


def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    return redirect('/login')
