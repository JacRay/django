from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #gives a http response to the browser when this function is called
    #return HttpResponse('<h1> Hey, Welcome to myapp</h1>')
    # to render a html file
    #doesnt need full directory info becase of settings.py template dir
    return render(request, 'index.html')      