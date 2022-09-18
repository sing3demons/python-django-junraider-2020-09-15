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

