from django.contrib import admin

from course.models import Exercise, Answer

# Register your models here.

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('origin', 'topic', 'exp_answer_date', 'status')
    search_fields = ('origin', 'topic')
    list_filter = ('exp_answer_date', 'status', 'pub_date', 'exp_date')
    ordering = ('exp_answer_date', )

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'student', 'datesend', 'grad')
    search_fields = ('exercise', 'datesend', 'grad')
    list_filter = ('datesend',)
    ordering = ('datesend',)

admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Answer, AnswerAdmin)