# Django docker-compose example

### link

https://docs.docker.com/compose/django/

### create example app

`sudo docker-compose run web django-admin startproject composeexample .`

### update file owner (root -> user)

`sudo chown -R $USER:$USER .`

### modify settings.py

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```
