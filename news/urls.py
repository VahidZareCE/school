# django
from django.urls import path

# app news
from news.views import (
                            ListCreateNews, 
                            UpdateDeleteNews, 
                            ListNewsStudent
                        )

urlpatterns = [
    path('news/', ListCreateNews.as_view()),
    path('news/<int:pk>', UpdateDeleteNews.as_view()),

    path('list/news/', ListNewsStudent.as_view())
]