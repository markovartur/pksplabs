from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'templates/static_handle.html')

def hello(request):
    return HttpResponse('Markov Artur BFI2001')
# Create your views here.

