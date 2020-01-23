from django import forms
from .models import Post


class TopicForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
