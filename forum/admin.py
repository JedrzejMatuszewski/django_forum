from django.contrib import admin
from .models import Categories, Topic, Post


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'author',
                    'category', 'content', 'slug',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post)
