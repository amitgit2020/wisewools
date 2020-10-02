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
            messages.success(request, f'Account has been created for {username}. You can login now!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'wisewools/signup.html', {"form": form})


def login(request):
    return render(request, 'wisewools/login.html')


def logout(request):
    return render(request, 'wisewools/login.html')


def home(request):
    return render(request, 'wisewools/home.html')


def art(request):
    return render(request, 'wisewools/art.html')


def culture(request):
    return render(request, 'wisewools/culture.html')


def cinema(request):
    return render(request, 'wisewools/cinema.html')


def photoessay(request):
    return render(request, 'wisewools/photoessay.html')


def design(request):
    return render(request, 'wisewools/design.html')
