from django.shortcuts import render
from rest_framework import generics

from .models import Test, Examinee, Question
from .serializers import TestSerializer, ExamineeSerializer, QuestionSerializer

class TestListView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class ExamineeListView(generics.ListAPIView):
    queryset = Examinee.objects.all()
    serializer_class = ExamineeSerializer