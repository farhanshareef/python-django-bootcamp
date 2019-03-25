from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# All views exist here as individual functions.
# Each view will take at least one argument.
# Each view must return an HttpResponse object with the content of the page.
# Each view must be mapped to urls.py file

def index(request):
    return HttpResponse("Hello World!")
