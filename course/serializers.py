# pakage python
import magic
from datetime import datetime

# rest_framework
from rest_framework import serializers

# app course
from course.models import Exercise, Answer

# app account
from account.serializers import StudentListSerilaizer



class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'
        read_only_fields=('origin',)

    def validate_file(self, value):
        if value:
            filetype = magic.from_buffer(value.read()) # check file type
            if not 'PDF' in filetype:
                raise serializers.ValidationError('لطفا فایل با پسوند pdf ارسال کنید .')
            else:
                return value
        return value

class ExerciseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('topic', 'text', 'file', 'exp_answer_date', 'hardldess')

    def validate_file(self, value):
        if value:
            filetype = magic.from_buffer(value.read()) # check file type
            if not 'PDF' in filetype:
                raise serializers.ValidationError('لطفا فایل با پسوند pdf ارسال کنید .')
            else:
                return value
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
        date = datetime.now()
        dateend = Exercise.objects.get(topic=ex.topic)
        if date.date() > dateend.exp_answer_date.date() and date.time() > dateend.exp_answer_date.time():
            raise serializers.ValidationError({'پایان زمان':'زمان ارسال جواب پایان یافته'})
        return attrs

    def validate_answer_file(self, value):
        if value:
            filetype = magic.from_buffer(value.read()) # check file type
            if not 'PDF' in filetype and not 'Zip' in filetype:
                raise serializers.ValidationError('شما می توانید فقط فایل با فرمت PDF و Zip ارسال کنید .')
            else:
                return value
        return value


class AnswerDetailSerializer(serializers.ModelSerializer):
    exercise = ExerciseDetailSerializer(read_only=True)
    answer_file = serializers.FileField(help_text='.اجازه ارسال دارند pdf فایل های با پسوند ')

    class Meta:
        model = Answer
        fields = ('id', 'exercise', 'student', 'answer_text', 'answer_file', 'datesend', 'grad')
        read_only_fields = ('student', 'grad')

    def validate(self, attrs):
        date = attrs['datesend']
        ex = attrs['exercise']
        dateend = Exercise.objects.get(topic=ex.topic)
        if date > dateend.exp_answer_date:
            raise serializers.ValidationError({'پایان زمان':'زمان ارسال جواب پایان یافته'})
        return attrs

    def validate_answer_file(self, value):
        if value:
            filetype = magic.from_buffer(value.read()) # check file type
            if not 'PDF' in filetype and not 'Zip' in filetype:
                raise serializers.ValidationError('شما می توانید فقط فایل با فرمت PDF و Zip ارسال کنید .')
            else:
                return value
        return value

class AnswerDetailTeacherSerializer(serializers.ModelSerializer):
    exercise = ExerciseDetailSerializer(read_only=True)
    student = StudentListSerilaizer(read_only=True)
    class Meta:
        model = Answer
        fields = ('id', 'exercise', 'student', 'answer_text', 'answer_file', 'datesend', 'grad')
        read_only_fields = ('exercise', 'student', 'answer_text', 'answer_file', 'datesend')