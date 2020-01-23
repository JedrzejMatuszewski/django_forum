from django.urls import path
from .views import (
    CatAndTopicListView,
    TopicDetailView,
    CategoryTopicListView,
    UserTopicListView,
    TopicCreateView,
    TopicAllListView,
    PostCreateView,
)

urlpatterns = [
    path('', CatAndTopicListView.as_view(), name='forum-home'),
    path('user/<str:username>', UserTopicListView.as_view(), name='topic-user'),
    path('topics/', TopicAllListView.as_view(), name="topic-all"),
    path('topics/<slug:slug>/', TopicDetailView.as_view(), name='topic-detail'),
    path('topics/<slug:slug>/new-post/', PostCreateView.as_view(), name='topic-new-post'),
    path('topics/category/<slug:slug>/', CategoryTopicListView.as_view(), name='topic-category'),
    path('topics/<slug:slug>/new/', TopicCreateView.as_view(), name='topic-create'),
]

