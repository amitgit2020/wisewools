# I have created this file - Amit 
from django.http import HttpResponse
from django.shortcuts import render




def signup(request):
    return HttpResponse('This is my signup page.')
    # return render(request, 'wisewools/signup.html')


def login(request):
    return HttpResponse('This is my login page.')
    # return render(request, login, context)



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

