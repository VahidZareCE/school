from urllib import request
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from course.models import Exercise, Answer
from course.serializers import ExerciseSerializer, AnswerSerializer, ExerciseDetailSerializer, AnswerDetailSerializer

from account.models import ProfileStudent

from course.permissions import IsTeacher, IsStudent
from rest_framework.authentication import TokenAuthentication


class ListCreateExerciesView(ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsTeacher)

class UpdateDeleteExerciesView(RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsTeacher)

    

class ListCreateAnswerView(ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsStudent)

    def perform_create(self, serializer):
        user = ProfileStudent.objects.get(user=self.request.user)
        print(user)
        serializer.save(student=user)

    def get_queryset(self):
        return Answer.objects.filter(student__user=self.request.user)


class UpdateDeleteAnswerView(RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerDetailSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsStudent)

    def perform_create(self, serializer):
        user = ProfileStudent.objects.get(user=self.request.user)
        print(user)
        serializer.save(student=user)

    def get_queryset(self):
        return Answer.objects.filter(student__user=self.request.user)