from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoriesListView.as_view(), name='forum-home'),
]

