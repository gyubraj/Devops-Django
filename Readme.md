Set up 

First Python need to be installed and ubuntu have by default python3 installed.
You should also have installed postgresql in your system. 

then 

create virtual environment

`python3 -m venv venv`

then 

activate virtual environemnt

`source venv/bin/activate`

then

install all packages

`pip install -r requirements.txt`

then 

please configure your database settings 

for that go into main/settings.py line 92

change following 

```
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<Database_name>',
        'USER':'<Username>',
        'PASSWORD':'<Password>',
        'HOST':'<Host>',   # This will be localhost when running locally
        'PORT': <database running port number>  # By default for postgres it is 5432
    }
}
```

then

you need to create database tables in the postgres so 

`python manage.py migrate`

last run the program 

`python manage.py runserver`


