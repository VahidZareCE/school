from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from news.models import News
from account.serializers import TeacherSerializer, StudentSerializer


class NewsSerializer(serializers.ModelSerializer):
    origin = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = News
        fields = ('id','origin', 'destination', 'topic', 'text', 'pub_date', 'exp_date', 'status')
