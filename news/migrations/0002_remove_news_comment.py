# Generated by Django 4.0.2 on 2022-02-12 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='comment',
        ),
    ]
