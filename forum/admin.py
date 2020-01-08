from django.contrib import admin
from .models import Categories, Topic, Post

admin.site.register(Categories)
admin.site.register(Topic)
admin.site.register(Post)