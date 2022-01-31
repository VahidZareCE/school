from dataclasses import fields
from rest_framework import serializers
# from rest_auth.registration.serializers import RegisterSerializer

from django.contrib.auth.hashers import make_password

from account.models import ProfileTeacher, User

# class UserSerializer(serializers.ModelSerializer):

#     # teacher = TeacherSerializer(required=True)

#     class Meta:
#         model = User
#         fields = ('username', 'password')


class TeacherSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model=User
            fields=['username', 'password', 'first_name', 'last_name']
    user = UserSerializer(required=True)
    class Meta:
        model = ProfileTeacher
        fields = ('user', 'national_code', 'name_school', 'name_course')

    def create(self, validated_data):
        
        users = validated_data.pop('user')

        user = User.objects.create(
            username=users['username'],
            password=make_password(users['password']),
            first_name=users['first_name'],
            last_name=users['last_name'],
            is_teacher=True
        )

        profile = ProfileTeacher.objects.create(
            user=user,
            national_code=validated_data['national_code'],
            name_school=validated_data['name_school'],
            name_course=validated_data['name_course'],
        )

        return profile







