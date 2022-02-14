# rest_framework
from rest_framework.generics import (
                                        ListCreateAPIView, 
                                        RetrieveUpdateDestroyAPIView, 
                                        ListAPIView, 
                                        RetrieveUpdateAPIView
                                    )
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication

# app course
from course.models import Exercise, Answer
from course.serializers import (
                                    ExerciseSerializer, 
                                    AnswerSerializer, 
                                    AnswerDetailSerializer, 
                                    AnswerDetailTeacherSerializer,
                                )
from course.permissions import IsTeacher, IsStudent

# app account
from account.models import ProfileStudent, ProfileTeacher




# list and create exercies just for teacher
class ListCreateExerciesView(ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsTeacher)
    search_fields = ['topic', 'status', 'destination__national_code', 'destination__user__first_name', 'destination__user__last_name']
    ordering_fields = ['exp_answer_date']

    def get_queryset(self):
        return Exercise.objects.filter(origin__user=self.request.user)

    def perform_create(self, serializer):
        user = ProfileTeacher.objects.get(user=self.request.user)
        serializer.save(origin=user)


# update and delete exercies just for teacher
class UpdateDeleteExerciesView(RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsTeacher)

    def get_queryset(self):
        return Exercise.objects.filter(origin__user=self.request.user)

    def perform_create(self, serializer):
        user = ProfileTeacher.objects.get(user=self.request.user)
        serializer.save(origin=user)

# list and create answer for student
class ListCreateAnswerView(ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsStudent)
    search_fields = ['exercise__topic', 'exercise__origin__user__first_name', 'exercise__origin__user__last_name', 'datesend']
    ordering_fields = ['datesend']

    def perform_create(self, serializer):
        user = ProfileStudent.objects.get(user=self.request.user)
        serializer.save(student=user)

    def get_queryset(self):
        return Answer.objects.filter(student__user=self.request.user)

# update and delete answer for student
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


# list answer for teacher
class ListAnswarTeacherView(ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerDetailSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsTeacher)
    search_fields = ['exercise__topic', 'student__national_code', 'datesend']
    ordering_fields = ['datesend']

    def get_queryset(self):
        return Answer.objects.filter(exercise__origin__user=self.request.user)

# update answer (grad) for teacher
class UpdateAnswerTeacherView(RetrieveUpdateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerDetailTeacherSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsTeacher)

    def get_queryset(self):
        return Answer.objects.filter(exercise__origin__user=self.request.user)