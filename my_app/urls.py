from django.contrib import admin
from django.urls import path, include

from my_app.views import IndexListView

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
]

app_name = "my_app"
