from django.urls import path

from news.views import ListCreateNews, UpdateDeleteNews

urlpatterns = [
    path('news/', ListCreateNews.as_view()),
    path('news/<int:pk>', UpdateDeleteNews.as_view()),
]