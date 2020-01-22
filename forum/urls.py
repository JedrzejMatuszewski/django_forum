from django.urls import path
from .views import (
    CatAndTopicListView,
    TopicDetailView,
    CategoryTopicListView,
    UserTopicListView,
    TopicCreateView,
    TopicAllListView,
)

urlpatterns = [
    path('', CatAndTopicListView.as_view(), name='forum-home'),
    path('user/<str:username>', UserTopicListView.as_view(), name='topic-user'),
    path('topics/', TopicAllListView.as_view(), name="topic-all"),
    path('topics/<slug:slug>/', TopicDetailView.as_view(), name='topic-detail'),
    path('topics/category/<slug:slug>/', CategoryTopicListView.as_view(), name='topic-category'),
    path('topics-new/', TopicCreateView.as_view(), name='topic-create'),
]

