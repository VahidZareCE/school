# rest_framework
from rest_framework.generics import (
                                        ListCreateAPIView, 
                                        RetrieveUpdateDestroyAPIView, 
                                        ListAPIView
                                    )
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# app news
from news.serializers import NewsSerializer, NewsDetailSerializer
from news.models import News
from news.permissions import IsStudent, IsTeacher

# app account
from account.models import ProfileStudent, ProfileTeacher


# list and create news just for teacher
class ListCreateNews(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsTeacher)
    search_fields = ['destination__national_code', 'topic', 'status']
    ordering_fields = ['pub_date', 'exp_date']

    def perform_create(self, serializer):
        user = ProfileTeacher.objects.get(user=self.request.user)
        serializer.save(origin=user)

    def get_queryset(self):
        user = ProfileTeacher.objects.get(user=self.request.user)
        return News.objects.filter(origin=user)

# update and delete news just for teacher
class UpdateDeleteNews(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsTeacher)

    def perform_create(self, serializer):
        user = ProfileTeacher.objects.get(user=self.request.user)
        serializer.save(origin=user)

    def get_queryset(self):
        user = ProfileTeacher.objects.get(user=self.request.user)
        return News.objects.filter(origin=user)

# list news just for student
class ListNewsStudent(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsStudent)
    search_fields = ['origin__user__first_name', 'origin__user__last_name', 'topic']
    ordering_fields = ['pub_date', 'exp_date']

    def get_queryset(self):
        user = ProfileStudent.objects.get(user=self.request.user)
        return News.objects.filter(destination__national_code=user.national_code).filter(status='published')