from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

from .models import Categories


def home(request):
    return render(request, 'forum/home.html')


class CategoriesListView(ListView):
    model = Categories
    template_name = 'forum/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'categories_obj'


def home(request):
    return render(request, 'forum/home.html')




