# Generated by Django 3.0.1 on 2020-01-24 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0012_topic_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='category_slug',
        ),
    ]