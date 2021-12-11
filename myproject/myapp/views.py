from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #gives a response to the browser when this function is called
    return HttpResponse('<h1> Hey, Welcome to myapp</h1>')