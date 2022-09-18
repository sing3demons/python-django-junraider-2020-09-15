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
 pip install mysql-connector-python
 ```
 3. Change settings.py DATABASES
 ```import mysql
 DATABASES = {
    'default': {
        'NAME': 'django_junraide',
        'ENGINE': 'mysql.connector.django',
        'USER': 'sing_user',
        'PASSWORD': 'my_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
 ```
 4. migrate
 ```migrate
 python manage.py migrate
 ```

