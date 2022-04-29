# Simple Set up 

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



# Run With Docker Compose 

1. Make Sure Docker and Docker Compose is installed in your Machine.

```python

    # You Know what this command does
    docker-compose up -d

    # To see logs
    docker-compose logs -f 

    # To stop 
    Docker-compose down

```

## References 

Please refer to these references if you get some error or you want to understand How it is working. 

First Link gives the way of configuring docker with django. You can choose other stack if you want to.

Second Link gives tou the docker images that can be used for python. 

Third one will help to solve the Database problem mainly for Mac M1 chip laptops.

1. https://docs.docker.com/samples/django/
2. https://hub.docker.com/_/python
3. https://stackoverflow.com/questions/62807717/how-can-i-solve-postgresql-scram-authentifcation-problem

