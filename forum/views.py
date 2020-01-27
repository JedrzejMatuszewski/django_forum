from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse


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
    paginate_by = 5

    def get_context_data(self, object_list=None, **kwargs):
        context = super(CategoryTopicListView, self).get_context_data(**kwargs)
        context['categories_obj'] = Categories.objects.all()
        context['topic_obj'] = Topic.objects.filter(category__slug=self.kwargs['slug']).order_by('-date_posted')
        context['category'] = self.kwargs['slug']
        return context


class UserTopicListView(ListView):
    model = Topic
    template_name = 'forum/topic_user.html'
    context_object_name = 'topic_obj'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Topic.objects.filter(author=user).order_by('-date_posted')


# nic nie znaczaca klasa, niech tu będzie na razie
class PostListView(ListView):
    model = Post
    context_object_name = 'object'


class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['title', 'content']

    def form_valid(self, form):
        category = get_object_or_404(Categories, slug=self.kwargs['cat'])
        form.instance.category = category
        form.instance.author = self.request.user
        return super(TopicCreateView, self).form_valid(form)


class TopicDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Topic

    def get_success_url(self):
        topic_p = get_object_or_404(Categories, slug=self.kwargs['cat'])
        return reverse_lazy('topic-category', kwargs={'slug': topic_p.slug})

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def get_success_url(self):
        topic_p = get_object_or_404(Topic, slug=self.kwargs['slug'])
        return reverse_lazy('topic-detail', kwargs={'cat': topic_p.category.slug,
                                                    'slug': topic_p.slug})

    def form_valid(self, form):
        topic = get_object_or_404(Topic, slug=self.kwargs['slug'])
        form.instance.author = self.request.user
        form.instance.topic = topic
        return super(PostCreateView, self).form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def get_success_url(self):
        obj = get_object_or_404(Topic, slug=self.kwargs['slug'])
        return reverse_lazy('topic-detail', kwargs={'cat': obj.category.slug,
                                                    'slug': obj.slug})

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False