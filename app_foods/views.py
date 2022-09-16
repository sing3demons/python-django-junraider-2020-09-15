from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("foods...")


def food(request, food_id):
    return HttpResponse('food id: '+str(food_id))
