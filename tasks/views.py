from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Welcome to my home")

def contact(request):
    return HttpResponse("<h1> Welcome contact </h1>")


def show_task(request):
    return HttpResponse("<h1> Welcome to Task management page </h1>")
