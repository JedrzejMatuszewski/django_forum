from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify


class Categories(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, unique=True)  # new

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('topic-category', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Topic(models.Model):
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    content = models.TextField(default="")
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('topic-detail', kwargs={'slug': self.slug, })

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='topics')

    def __str__(self):
        return self.title


