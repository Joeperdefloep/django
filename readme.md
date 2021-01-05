#Django tutorial
repo for following the Django tutorial.
https://docs.djangoproject.com/en/3.1/intro/tutorial01/
## Django cheat sheet
1. create a project
    - `cd` to the directory, then `django-admin startproject <site-name>`
this will create a folder structure like:
```
<site-name>
manage.py        #Has all classes etc
<site-name>
    __init__.py
    settings.py  #settings: set TIME_ZONE = 'Europe/Amsterdam', add apps to INSTALLED_APPS
    urls.py      #manage links here
    asgi.py
    wsgi.py
```
2. create an app 
    - run `python manage.py startapp <appp-name>`
```
<app-name>/
    __init__.py
    admin.py          #set what classes can be changed as admin
    apps.py
    migrations/
        __init__.py
    models.py         #define classes here
    tests.py          
    urls.py           #define url patterns
    views.py          #handle rsponses here
```
    - add `'<app-name>.apps.<App-name>Config'` to `INSTALLED_APPS` in `<site-name>/settings.py`
    - migrate with `python manage.py migrate` to update changes
    - debug with `python manage.py shell`
3. add templates folder for `.html` files
    - in `<app-name>/views.py`, link to html files with `render(request, <app-name>/<template-name>.html, argDict)`
```
<app-name>/
    ...
    templates/
        <app-name>/
            <template-name>.html
```
    - handle requests with `get_object_or_404()`
4. creating a form

5. make tests
Encountered following issue: https://github.com/ipython/ipython/issues/12745
run `conda install 'jedi<0.18.0' to fix

repo for me following the Django python tutorial
