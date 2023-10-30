from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from my_app.models import User, People


# Create your views here.


class IndexListView(generic.ListView):
    model = People
    template_name = "index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()

        context["count_user"] = get_user_model().objects.count()

        return context
