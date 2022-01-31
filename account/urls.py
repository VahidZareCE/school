from django.urls import path, include

from account.views import UserList

app_name = 'account'

urlpatterns = [
    path('create/teacher/', UserList.as_view(), name='create_teacher'),
]
