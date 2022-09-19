# python-django-junraider-2020-09-15

- install virtualenv
```virtualenv
python3 -m pip install virtualenv
```

- create environment
```env
python3 -m virtualenv venv
```

- Activate
```activate
source ./venv/bin/activate 
```
```install django
pip install django  
```
- create project django
```create project django
django-admin startproject project_jrd .
```

 - start server
 ```runserver
 python manage.py runserver
 ```

- create app
```
  python manage.py startapp app_general
  python manage.py startapp app_foods 
```

- MySQL database connect
 1. create database gjango_junraide
 2. install mysql-connector-python
 ```install
 pip3 install mysql-connector-python==8.0.29
 ```
 3. Change settings.py DATABASES
 ```import mysql
DATABASES = {
    'default': {
        'NAME': 'django_junraider',
        'ENGINE': 'mysql.connector.django',
        'USER': 'kpsing',
        'PASSWORD': 'P@ssw0rd',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
 ```
 4. migrate
 ```migrate
 python manage.py migrate
 ```


 ## Database migration
 ### app_foods create class models.py 
 1. create/edit model
 2. makemigrations
 ```
 python manage.py makemigrations app_foods
 ```
 3. migrate
 ```migrate
  python manage.py migrate
 ```

## Test models in shell before real use 
1. install bpython 
```shell
pip install bpython
```
2. shell
```shell
 python manage.py shell  
```
3. create/update
```create/update
from app_foods.models import Food
food1 = Food()
food1.title = 'Red Spicy'
food1.price = 349
food1.save()
food1.special_price = 299
food1.description = ''
from backports.zoneinfo import ZoneInfo
from datetime import datetime
date1 = datetime(2022,2,15, tzinfo=ZoneInfo('Asia/Bangkok'))
food1.promotion_end_at = date1
food1.save()

>>> food2 = Food()
>>> food2.title = 'ei'
>>> food2.price = 2
>>> food2.save()
>>> food2.delete()
(1, {'app_foods.Food': 1})
>>> food3 = Food()
>>> food3.title = 'Dark Choco Premium'
>>> food3.price = 449
>>> food3.special_price = 399
>>> food3.is_premium = True
>>> food3.promotion_end_at = date1
>>> food3.description = ''
>>> food3.save()
```
4. delete
```delete
food2 = Food()
food2.title = 'ei'
food2.price = 2
food2.save()
food2.delete()
```
5. read
```read
>>> from app_foods.models import Food
>>> all_foods =Food.objects.all()
>>> all_foods
```

