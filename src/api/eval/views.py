from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Test, Examinee, Question, Submission
from .serializers import TestSerializer, ExamineeSerializer, QuestionSerializer, SubmissionSerializer

class TestListView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class ExamineeListView(generics.ListAPIView):
    queryset = Examinee.objects.all()
    serializer_class = ExamineeSerializer

class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class SubmissionListView(generics.ListAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer