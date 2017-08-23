from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return  HttpResponse("Hey:)")
def contato(request):
    return  HttpResponse("Marco Roberto")
# Create your views here.
