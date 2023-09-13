from django.shortcuts import render

from . import models
# Create your views here.

def home(request):
    context = {}
    news = models.News.objects.all()
    context['news'] = news
    
    return render(request,'index.html', context)

def about (request):
   return render(request,"about.html")