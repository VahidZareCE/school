# Generated by Django 4.0.2 on 2022-02-10 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilestudent',
            name='name_course',
        ),
        migrations.RemoveField(
            model_name='profilestudent',
            name='name_school',
        ),
    ]