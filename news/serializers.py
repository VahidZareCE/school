from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from news.models import News
from account.serializers import TeacherSerializer, StudentSerializer


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
