from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    
    #gives a http response to the browser when this function is called
    #return HttpResponse('<h1> Hey, Welcome to myapp</h1>')
    
    # to render a html file
    #doesnt need full directory info becase of settings.py template dir
    # 'myname' is a variable and name is a value
    # return render(request, 'index.html',{'myname':name})      

    #dynamic data
    # context = {
    #     'name': 'John',
    #     'age': '25',
    #     'nation': 'Indian'
    # }
    # name = 'John'
    # return render(request, 'index.html',context) 

    return render(request, 'index.html')  

def counter(request):
    
    #gets the text entered and store in variable text 
    text = request.POST['word']
    
    #find no of words in the text
    nowords = len(text.split())

    #returns a http response with the no of words
    return render(request, 'counter.html',{'length':nowords})