# Generated by Django 3.0.1 on 2020-01-20 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='content',
            field=models.TextField(default=''),
        ),
    ]