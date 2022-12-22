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

class QuestionsByTestView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    def get_queryset(self):
        test_id = self.kwargs['test_id']
        return Question.objects.filter(test_id=test_id)

class SubmissionListView(generics.ListAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
 

class TestAndQuestionsView(APIView):
    queryset = Test.objects.all()

    def get(self, request):
        tests = Test.objects.all()
        test_serializer = TestSerializer(tests, many=True)
        response = []
        for test in test_serializer.data:
            questions = Question.objects.filter(test_id=test['id'])
            question_serializer = QuestionSerializer(questions, many=True)
            response.append({
                'test': test,
                'questions': question_serializer.data
            })
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        questions = data.pop('questions')
        test_serializer = TestSerializer(data=data)
        if test_serializer.is_valid():
            test_serializer.save()
            for question in questions:
                question['test_id'] = test_serializer.data['id']
                question_serializer = QuestionSerializer(data=question)
                if question_serializer.is_valid():
                    question_serializer.save()
                else:
                    return Response(question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(test_serializer.data, status=status.HTTP_201_CREATED)
        return Response(test_serializer.errors, status=status.HTTP_400_BAD_REQUEST)