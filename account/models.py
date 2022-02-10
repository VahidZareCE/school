from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class ProfileTeacher(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    national_code = models.CharField(max_length=10)
    name_school = models.CharField(max_length=255)
    name_course = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class ProfileStudent(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    national_code = models.CharField(max_length=10)

    def __str__(self):
        return self.national_code 
