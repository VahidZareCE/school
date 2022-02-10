from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from account.serializers import (
                                    TeacherSerializer, 
                                    StudentSerializer, 
                                    TokenSerializer, 
                                    UpdateStudentSerializer, 
                                    UpdateTeacherSerializer, 
                                    ChangePasswordSerializer
                                )
from account.models import User, ProfileTeacher, ProfileStudent
from account.permissions import IsTeacher

class ListCreateTeacherView(ListCreateAPIView):
    queryset = ProfileTeacher.objects.all()
    serializer_class = TeacherSerializer

    def post(self, request, format=None):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListCreateStudentView(ListCreateAPIView):
    queryset = ProfileStudent.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated, IsTeacher,)
    authentication_classes=(TokenAuthentication,)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateTokenView(ObtainAuthToken):
    serializer_class = TokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UpdateProfile(RetrieveUpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.user.is_teacher:
            return UpdateTeacherSerializer
        if self.request.user.is_student:
            return UpdateStudentSerializer

    def get_object(self):
        if self.request.user.is_teacher:
            return ProfileTeacher.objects.get(user=self.request.user)
        if self.request.user.is_student:
            return ProfileStudent.objects.get(user=self.request.user)

class ChangePassword(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model=User
    authentication_classes=(TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
    
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({'old_password':['Wrong password.']}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            response = {
                'status':'success',
                'code': status.HTTP_200_OK,
                'message': 'Password update successfully.',
                'data':[]
            }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)