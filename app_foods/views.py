from datetime import datetime
from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
all_foods = [
    {
        'id': 1, 'title': 'Dark Choco Premium', 'price': 499,
        'is_premium': True, 'promotion_end_at': datetime(2022, 2, 28)
    },
    {
        'id': 2, 'title': 'Red Spicy', 'price': 499, 'is_premium': False,
        'promotion_end_at': datetime(2022, 2, 15)
    },
    {
        'id': 3, 'title': 'Blue Glacier', 'price': 349, 'is_premium': False,
        'promotion_end_at': datetime(2022, 2, 15)
    },
]


def foods(request):
    data = {'foods': all_foods}
    return render(request, 'app_foods/foods.html', context=data)


def food(request, food_id):
    one_food = None
    try:
        one_food = [f for f in all_foods if f['id'] == food_id][0]
    except IndexError:
        print('not found')
    context = {'food': one_food}
    return render(request, 'app_foods/food.html', context)
