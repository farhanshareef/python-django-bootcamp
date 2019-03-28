from django.urls import path, include, re_path
from appTwo import views

urlpatterns = [
    re_path(r'^$',views.help, name='help'),
]
