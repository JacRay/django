from django.urls import path
from . import views

urlpatterns = [
    #define the url pattern for the home page
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter')
]
