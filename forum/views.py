from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

from .models import Categories, Topic


class CatAndTopicListView(ListView):
    model = Categories
    template_name = 'forum/home.html'  # <app>/<model>_<viewtype>.html

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CatAndTopicListView, self).get_context_data(**kwargs)
        context['categories_obj'] = Categories.objects.all()
        context['topic_obj'] = Topic.objects.all()
        return context


class TopicDetailView(DetailView):
    model = Topic
    context_object_name = 'topic_obj'


class CategoryTopicListView(ListView):
    model = Topic
    template_name = 'forum/topic_category.html'
    context_object_name = 'topic_obj'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryTopicListView, self).get_context_data(**kwargs)
        context['categories_obj'] = Categories.objects.all()
        context['topic_obj'] = Topic.objects.filter(category_id=self.kwargs.get('pk')).order_by('-date_posted')
        return context
