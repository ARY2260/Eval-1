from rest_framework import serializers
from .models import Test, Question, Examinee, Submission

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'title', 'description', 'created_at']

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'

class ExamineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examinee
        fields = ['id', 'test_id', 'name', 'email', 'total_score', 'created_at']