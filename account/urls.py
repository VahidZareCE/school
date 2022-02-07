from django.urls import path

from account.views import ListCreateTeacherView, ListCreateStudentView, CreateTokenView

urlpatterns = [
    path('register/teacher/', ListCreateTeacherView.as_view()),
    path('register/student/', ListCreateStudentView.as_view()),
    path('token/', CreateTokenView.as_view())
]