from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hellow")

def add(request, num1, num2):
    return HttpResponse(f'<h1>{num1 + num2}</h1>')

def minus(request, num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    return HttpResponse(f'<h1>{num1 - num2}</h1>')

def div(request, num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    div = round(num1/num2,1)
    return HttpResponse(f'<h1>{div}</h1>')
