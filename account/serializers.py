# regex python
import re

# rest_framework
from rest_framework import serializers

# django
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password

# app account
from account.models import ProfileStudent, ProfileTeacher, User


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


class StudentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model=User
            fields=['username', 'password', 'first_name', 'last_name', 'is_teacher', 'is_student']
            read_only_fields = ['is_teacher', 'is_student']

        def validate_username(self, value):
            if len(value) >= 10 and re.match(r'^\d*$', value) == None:
                raise serializers.ValidationError('لطفا برای نام کاربری کد ملی معتر وارد کنید .')
            
            if re.match(r'^\d*$', value):
                return value

    user = UserSerializer(required=True)
    class Meta:
        model = ProfileStudent
        fields = ('user', 'national_code',)


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
        )

        return profile



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
            msg = _('نام کاربری یا رمز عبور اشتباه است .')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs



class UpdateStudentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model=User
            fields=('username', 'first_name', 'last_name', 'is_student')
            read_only_fields=('is_student',)

    user = UserSerializer()

    class Meta:
        model=ProfileStudent
        fields=('id','user', 'national_code')


class UpdateTeacherSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model=User
            fields=('username', 'first_name', 'last_name', 'is_teacher')
            read_only_fields=('is_teacher',)

    user = UserSerializer()

    class Meta:
        model=ProfileTeacher
        fields=('user', 'national_code', 'name_school', 'name_course')
        

class ChangePasswordSerializer(serializers.Serializer):
    model=User

    old_password=serializers.CharField(required=True, style={'input_type':'password'})
    new_password=serializers.CharField(required=True, style={'input_type':'password'})


class StudentListSerilaizer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model=User
            fields=('username', 'first_name', 'last_name')
    user = UserSerializer()
    
    class Meta:
        model=ProfileStudent
        fields=('user', 'national_code')