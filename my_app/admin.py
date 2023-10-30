from django.contrib import admin

from my_app.models import User, People

# Register your models here.
admin.site.register(User)
admin.site.register(People)
