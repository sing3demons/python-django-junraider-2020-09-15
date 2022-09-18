from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'app_foods/foods.html')


def food(request, food_id):
    return render(request, 'app_foods/food.html', context={'food_id': food_id})
