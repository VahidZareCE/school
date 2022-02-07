from rest_framework import serializers

from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.hashers import make_password

from account.models import ProfileStudent, ProfileTeacher, User

# create user and profile teacher
class TeacherSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model=User
            fields=['username', 'password', 'first_name', 'last_name', 'is_teacher', 'is_student']
            read_only_fields = ['is_teacher', 'is_student']
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


# create user and profile student
class StudentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model=User
            fields=['username', 'password', 'first_name', 'last_name', 'is_teacher', 'is_student']
            read_only_fields = ['is_teacher', 'is_student']
    user = UserSerializer(required=True)
    class Meta:
        model = ProfileStudent
        fields = ('user', 'national_code', 'name_school', 'name_course')

    def create(self, validated_data):
        
        users = validated_data.pop('user')

        user = User.objects.create(
            username=users['username'],
            password=make_password(users['password']),
            first_name=users['first_name'],
            last_name=users['last_name'],
            is_student=True
        )

        profile = ProfileStudent.objects.create(
            user=user,
            national_code=validated_data['national_code'],
            name_school=validated_data['name_school'],
            name_course=validated_data['name_course'],
        )

        return profile

# create auth token 
class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type':'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password
        )

        if not user:
            msg = _('امکان ورود ندارید')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs