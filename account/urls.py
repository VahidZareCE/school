# django
from django.urls import path

# app account
from account.views import (
                            CreateTeacherView, 
                            CreateStudentView, 
                            CreateTokenView, 
                            UpdateProfile, 
                            ChangePassword
                        )


urlpatterns = [
    path('register/teacher/', CreateTeacherView.as_view()),
    path('register/student/', CreateStudentView.as_view()),
    path('update/profile/', UpdateProfile.as_view()),
    path('token/', CreateTokenView.as_view()),

    path('account/changpassword/', ChangePassword.as_view())
]