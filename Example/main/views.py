from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Это мой первый сайт на Django</h1>")

def new(request):
    return HttpResponse("<h1>Это вторая страница сайта на Django</h1>")