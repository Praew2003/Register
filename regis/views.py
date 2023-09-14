from django.shortcuts import render

from . import models
# Create your views here.

def home(request):
    context = {}
    course = models.Course.objects.all()
    context['courses'] = course
    
    return render(request,'index.html', context)

def general(request):
    context = {}
    category = models.Category.objects.get(id=1)
    
    course = models.Course.objects.filter(category=category)
    context['courses'] = course
    
    return render(request,'general.html', context)

def only(request):
    context = {}
    category = models.Category.objects.get(id=2)
    
    course = models.Course.objects.filter(category=category)
    context['courses'] = course
    
    return render(request,'only.html', context)

def choose(request):
    context = {}
    category = models.Category.objects.get(id=3)
    
    course = models.Course.objects.filter(category=category)
    context['courses'] = course
    
    return render(request,'choose.html', context)

def about (request):
   return render(request,"about.html")