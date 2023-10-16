from django.contrib import admin
from django.urls import path, include

from my_app.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "my_app"
