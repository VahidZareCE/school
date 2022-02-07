from django.db import models

from account.models import ProfileStudent, ProfileTeacher

# Create your models here.

class Exercise(models.Model):
    STATUS = (
        ('published', 'published'),
        ('exp','exp'),
        ('deleted','deleted'),
    )
    HARDLESS = (
        ('easy','easy'),
        ('medium','medium'),
        ('hard','hard'),
    )
    origin = models.ForeignKey(to=ProfileTeacher, on_delete=models.CASCADE) #
    destination = models.ManyToManyField(to=ProfileStudent) #
    topic = models.CharField(max_length=258, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    exp_answer_date = models.DateTimeField()
    pub_date = models.DateTimeField()
    exp_date = models.DateTimeField()
    status = models.CharField(max_length=30, choices=STATUS)
    file = models.FileField(blank=True, upload_to='exercises') #
    stu_grade = models.IntegerField()
    hardldess = models.CharField(max_length=30, choices=HARDLESS)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic

class Answer(models.Model):
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE, related_name='practice')
    student = models.ForeignKey(to=ProfileStudent, on_delete=models.PROTECT)
    answer_text = models.TextField(blank=True)
    answer_file = models.FileField(blank=True, null=True, upload_to='answer exercises')
    grad = models.IntegerField(blank=True, default=0)
    datesend = models.DateTimeField(auto_now_add=True)



