from django.contrib import admin
from django.urls import path
from home.views import  *

urlpatterns = [
    path("", index, name='home'),
    path("about", about , name='about'),
    path("services", services ,name='services'),
    path("contact", contact ,name='contact'),
    path("contact/add", add ,name='add'),
    path("webhook/", webhook , name="webhook"),


]

