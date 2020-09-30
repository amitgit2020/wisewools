# This file is created by Amit
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account has been created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'wisewools/signup.html', {"form": form})


def login(request):
    # return HttpResponse('This is my login page.')
    return render(request, 'wisewools/login.html')


def home(request):
    # return HttpResponse("This is my Home page")
    return render(request, 'wisewools/home.html')


def art(request):
    # return HttpResponse("This is my Art page")
    return render(request, 'wisewools/art.html')


def culture(request):
    # return HttpResponse("This is my Culture page")
    return render(request, 'wisewools/culture.html')


def cinema(request):
    # return HttpResponse("This is my Cinema page")
    return render(request, 'wisewools/cinema.html')


def photoessay(request):
    # return HttpResponse("This is my Photo Essay page")
    return render(request, 'wisewools/photoessay.html')


def design(request):
    # return HttpResponse("This is my design page")
    return render(request, 'wisewools/design.html')
