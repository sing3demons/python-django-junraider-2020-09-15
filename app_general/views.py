from http.client import HTTPResponse
from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('app_general')

def about(request):
    return HttpResponse('about')
