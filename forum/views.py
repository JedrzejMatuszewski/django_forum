from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy


from .models import Categories, Topic, Post


class CatAndTopicListView(ListView):
    model = Categories
    template_name = 'forum/home.html'  # <app>/<model>_<viewtype>.html

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CatAndTopicListView, self).get_context_data(**kwargs)
        context['categories_obj'] = Categories.objects.all().order_by('title')
        context['topic_obj'] = Topic.objects.all().order_by('-date_posted')[:3]
        return context


class TopicDetailView(DetailView):
    model = Topic
    context_object_name = 'topic_obj'


class TopicAllListView(ListView):
    model = Topic
    template_name = 'forum/topic_all.html'
    context_object_name = 'topic_obj'
    ordering = ['-date_posted']
    paginate_by = 3


class CategoryTopicListView(ListView):
    model = Topic
    template_name = 'forum/topic_category.html'
    context_object_name = 'topic_obj'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryTopicListView, self).get_context_data(**kwargs)
        context['categories_obj'] = Categories.objects.all()
        context['topic_obj'] = Topic.objects.filter(category__slug=self.kwargs['slug']).order_by('-date_posted')
        return context


class UserTopicListView(ListView):
    model = Topic
    template_name = 'forum/topic_user.html'
    context_object_name = 'topic_obj'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Topic.objects.filter(author=user).order_by('-date_posted')


class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['title', 'content', 'category']

    def form_valid(self, form):
        category = Categories.objects.filter(title=self.kwargs['category'])
        form.instance.category = category
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'topic']
    slug = Post.topic
    success_url = reverse_lazy('topic-detail', slug)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
