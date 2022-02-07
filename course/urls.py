from django.urls import path

from course.views import (ListCreateExerciesView, UpdateDeleteExerciesView, ListCreateAnswerView, UpdateDeleteAnswerView)

urlpatterns = [
    path('exercise/', ListCreateExerciesView.as_view(), name='list-create-exercies'),
    path('exercise/<int:pk>/', UpdateDeleteExerciesView.as_view(), name='update-delete-exercies'),
    
    path('answer/', ListCreateAnswerView.as_view()),
    path('answer/<int:pk>/', UpdateDeleteAnswerView.as_view()),

]