import os
import magic
from rest_framework import serializers
from datetime import datetime


from course.models import Exercise, Answer

# from .views import ListCreateExerciesView


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

    def validate_file(self, value):
        if value != '':
            filetype = magic.from_buffer(value.read())
            print(filetype)
            if not 'PDF' in filetype:
                raise serializers.ValidationError('لطفا فایل با پسوند pdf ارسال کنید .')
            else:
                return value

class ExerciseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('topic', 'text', 'file', 'exp_answer_date', 'hardldess')

    def validate_file(self, value):
        if value:
            filetype = magic.from_buffer(value.read())
            if not 'PDF' in filetype:
                raise serializers.ValidationError('لطفا فایل با پسوند pdf ارسال کنید .')
            else:
                return value


class AnswerSerializer(serializers.ModelSerializer):
    exercise = serializers.PrimaryKeyRelatedField(queryset=Exercise.objects.all())
    answer_file = serializers.FileField(help_text='.اجازه ارسال دارند pdf فایل های با پسوند ')
    class Meta:
        model = Answer
        fields = ('id', 'exercise', 'student', 'answer_text', 'answer_file', 'datesend', 'grad')
        read_only_fields = ('student', 'grad', 'datesend')

    def validate(self, attrs):
        ex = attrs['exercise']
        dateend = Exercise.objects.get(topic=ex.topic)
        if datetime.now() > dateend.exp_answer_date:
            raise serializers.ValidationError({'پایان زمان':'زمان ارسال جواب پایان یافته'})
        return attrs

    def validate_answer_file(self, value):
        if value:
            filetype = magic.from_buffer(value.read())
            if not 'PDF' in filetype:
                raise serializers.ValidationError('.اجازه ارسال دارند pdf فایل های با پسوند ')
            else:
                return value


class AnswerDetailSerializer(serializers.ModelSerializer):
    exercise = ExerciseDetailSerializer(read_only=True)
    answer_file = serializers.FileField(help_text='.اجازه ارسال دارند pdf فایل های با پسوند ')

    class Meta:
        model = Answer
        fields = ('exercise', 'student', 'answer_text', 'answer_file', 'datesend', 'grad')
        read_only_fields = ('student', 'grad')

    def validate(self, attrs):
        date = attrs['datesend']
        ex = attrs['exercise']
        dateend = Exercise.objects.get(topic=ex.topic)
        if date > dateend.exp_answer_date:
            raise serializers.ValidationError({'پایان زمان':'زمان ارسال جواب پایان یافته'})
        return attrs

    def validate_answer_file(self, value):
        filetype = magic.from_buffer(value.read())
        print(filetype)
        if not 'PDF' in filetype:
            raise serializers.ValidationError('لطفا فایل با پسوند pdf ارسال کنید .')
        else:
            return value

    def validate_grad(self, value):
        pass