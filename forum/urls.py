from django.urls import path
from .views import (
    CatAndTopicListView,
    TopicDetailView,
    CategoryTopicListView,
    UserTopicListView,
    TopicCreateView,
    TopicAllListView,
    PostCreateView,
    TopicDeleteView,
    PostListView,
    PostDeleteView
)

urlpatterns = [
    path('', CatAndTopicListView.as_view(), name='forum-home'),
    path('user/<str:username>', UserTopicListView.as_view(), name='topic-user'),
    path('topics/', TopicAllListView.as_view(), name="topic-all"),

    path('topics/category/<slug:slug>/',
         CategoryTopicListView.as_view(), name='topic-category'),
    path('topics/category/<slug:cat>/<slug:slug>/',
         TopicDetailView.as_view(), name='topic-detail'),

    path('topics-add/category/<slug:cat>/',
         TopicCreateView.as_view(), name='topic-create'),
    path('topics-delete/category/<slug:cat>/<slug:slug>/',
         TopicDeleteView.as_view(), name='topic-delete'),

    path('topics/category/<slug:cat>/<slug:slug>/new/',
         PostCreateView.as_view(), name='topic-new-post'),

    path('post/<slug:slug>/<int:pk>/',
         PostListView.as_view(), name='post-detail',),
    path('post/<slug:slug>/<int:pk>/delete',
         PostDeleteView.as_view(), name='post-delete'),
]
