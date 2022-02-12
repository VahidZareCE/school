from django.db import models

from account.models import ProfileStudent, ProfileTeacher

# Create your models here.

class News(models.Model):
    STATUS = (
        ('published', 'published'),
        ('exp','exp'),
        ('deleted','deleted'),
    )
    origin = models.ForeignKey(to=ProfileTeacher, on_delete=models.CASCADE) #
    destination = models.ManyToManyField(to=ProfileStudent) #
    topic = models.CharField(max_length=258, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    pub_date = models.DateTimeField()
    exp_date = models.DateTimeField()
    status = models.CharField(max_length=30, choices=STATUS)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
