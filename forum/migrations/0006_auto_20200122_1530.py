# Generated by Django 3.0.1 on 2020-01-22 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_topic_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
