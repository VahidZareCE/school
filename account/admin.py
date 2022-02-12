from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from account.models import User, ProfileTeacher, ProfileStudent

# Register your models here.

UserAdmin.fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Roles'), {'fields':('is_teacher', 'is_student')}),
    )
UserAdmin.list_display = ('username', 'first_name', 'last_name', 'is_staff', 'is_student', 'is_teacher')
UserAdmin.list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_teacher', 'is_student')

class ProfileTeacherAdmin(admin.ModelAdmin):
    list_display = ('national_code', 'user', 'name_school', 'name_course')
    search_fields = ('national_code', 'user', 'name_school', 'name_course')
    ordering = ('id',)

class ProfileStudentAdmin(admin.ModelAdmin):
    list_display = ('national_code', 'user')
    search_fields = ('national_code', 'user')
    ordering = ('id',)

admin.site.register(User, UserAdmin)
admin.site.register(ProfileTeacher, ProfileTeacherAdmin)
admin.site.register(ProfileStudent, ProfileStudentAdmin)