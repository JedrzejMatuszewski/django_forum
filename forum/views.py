from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

from .models import Categories, Topic


def home(request):
    return render(request, 'forum/home.html')


class CategoriesListView(ListView):
    model = Categories
    template_name = 'forum/home.html'  # <app>/<model>_<viewtype>.html

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoriesListView, self).get_context_data(**kwargs)
        context['categories_obj'] = Categories.objects.all()
        context['topic_obj'] = Topic.objects.all()
        return context


def home(request):
    return render(request, 'forum/home.html')




