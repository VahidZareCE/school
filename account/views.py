
from django.shortcuts import render

from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

from account.models import ProfileTeacher, User
from account.serializers import TeacherSerializer

# Create your views here.

class UserList(ListCreateAPIView):
    # permission_classes = (IsAuthenticatedOrWriteOnly,)
    queryset = ProfileTeacher.objects.all()
    serializer_class = TeacherSerializer

    def post(self, request, format=None):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)