from django.contrib import admin

from account.models import User, ProfileTeacher, ProfileStudent

# Register your models here.

admin.site.register(User)
admin.site.register(ProfileTeacher)
admin.site.register(ProfileStudent)