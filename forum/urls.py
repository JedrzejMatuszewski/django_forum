from django.urls import path
from .views import (
    CatAndTopicListView,
    TopicDetailView,
    CategoryTopicListView,
)

urlpatterns = [
    path('', CatAndTopicListView.as_view(), name='forum-home'),
    path('topics/<int:pk>/', TopicDetailView.as_view(), name='topic-detail'),
    path('topics/category/<int:pk>/', CategoryTopicListView.as_view(), name='topic-category'),
]

