from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Home Page')

def test1(request):
    return HttpResponse('test1')

def test2(request):
    return HttpResponse('test2')