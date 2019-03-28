This project is to follow along the Python Django Bootcamp.

[Managing Environments](https://conda.io/docs/using/envs.html)
=====================
Create new Environment: conda create --name myDjangoEnv django
List conda Environments: conda info --envs
Activate Environment: source activate myDjangoEnv

Django
=======
Create Django project: django-admin startproject first_project

Structure
---------
* __init__.py tells python that this is a package
* settings.py stores project settings
* urls.py stores urls for project using regular expressions
* wsgi.py used for deploying in production
* manage.py used for managing webapps

Apps
----
Create django app: python manage.py startapp first_app

* __init__.py tells python that this is a package
* admin.py used to register models to use in admin interface
* apps.py used for application specific config
* models.py used to store application data models (ER diagram) <<
* tests.py store functions to test your code
* views.py handles requests and returns responses <<
* migrations stores information as it relates to the models

Models and Views files are the two main files

After creating app, modify first_project/settings.py
Under INSTALLED_APPS list, add 'first_app'.

Add 'from django.http import HttpResponse' to the top of views.py.
# All views exist here as individual functions.
# Each view will take at least one argument.
# Each view must return an HttpResponse object with the content of the page.
# Each view must be mapped to urls.py file

Add from first_app import views in urls.py
Add from django.urls import path, include, re_path
Then, add URL pattern as regex (ie. 're_path(r'^$',views.index, name='index'),') to urlpatterns list.

Using templates
# Create templates folder in the project folder
# Create app folder in templates folder
# Add TEMPLATE_DIR = os.path.join(BASE_DIR,"templates") to settings.py
# Modify TEMPLATES dict in settings.py to use TEMPLATE_DIR
# Create urls.py in app folder (proj/app)
# Add the following code
  from django.urls import path, include, re_path
  from first_app import views

  urlpatterns = [
      re_path(r'^$',views.help, name='help'),
    ]
# Connect app urls.py to proj urls.py by adding
  re_path(r'^help/',include('appTwo.urls')),
  to urlpatterns in proj urls.py
# Add new view def to views.py
  def help(request):
      helpdict = {'help_insert':'HELP PAGE'}
      return render(request,'appTwo/help.html',context=helpdict)
# Add template tag to html file. Make sure it is the key from the dictionary.
  {{ help_insert }}

Using Statis Files
# Add static files dir to settings.py

ss16 lec125
