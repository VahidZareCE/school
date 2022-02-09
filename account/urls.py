from django.urls import path

from account.views import ListCreateTeacherView, ListCreateStudentView, CreateTokenView, UpdateProfile, ChangePassword

urlpatterns = [
    path('register/teacher/', ListCreateTeacherView.as_view()),
    path('register/student/', ListCreateStudentView.as_view()),
    path('update/profile/', UpdateProfile.as_view()),
    path('token/', CreateTokenView.as_view()),

    path('account/changpassword/', ChangePassword.as_view())
]