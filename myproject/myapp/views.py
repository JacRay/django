from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
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


    #making a object of Feature class
    # feature1 = Feature()
    # #giving values
    # feature1.id = 0
    # feature1.name = 'John'
    # feature1.details = ' Our service is very quick'
    # #the object is send to the html with a new name feature
    # return render(request, 'index.html', {'feature': feature1 })  




    # feature1 = Feature()
    # #giving values
    # feature1.id = 0
    # feature1.name = 'Fast'
    # feature1.details = ' Our service is very quick'

    # feature2 = Feature()
    # #giving values
    # feature2.name = 'Easy to Use'
    # feature2.id = 1
    # feature2.details = ' Our service is Easy to use'

    # feature3 = Feature()
    # #giving values
    # feature3.id = 2
    # feature3.name = 'Affordable'
    # feature3.details = ' Our service is very affordable'

    # feature4 = Feature()
    # #giving values
    # feature4.id = 3
    # feature4.name = 'Fast'
    # feature4.details = ' Our service is very very quick'
    # # when there are multiple same type of modes we can use django list
    # # make it easy using fro loop in index.html
    # features = {feature1, feature2, feature3, feature4}

    # return render(request, 'index.html', {'features': features})


    #giving all object in  Feature to features
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

def counter(request):
    
    #gets the text entered and store in variable text 
    text = request.POST['word']
    
    #find no of words in the text
    nowords = len(text.split())

    #returns a http response with the no of words
    return render(request, 'counter.html',{'length':nowords})