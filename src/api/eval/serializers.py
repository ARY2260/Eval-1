from rest_framework import serializers
from .models import Test, Question, Examinee, Submission

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class TestSerializer(serializers.HyperlinkedModelSerializer):
    test_questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Test
        fields = ['id', 'title', 'description', 'created_at', 'test_questions']

class SubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'

class ExamineeSerializer(serializers.HyperlinkedModelSerializer):
    examinee_submissions = SubmissionSerializer(many=True, read_only=True)
    class Meta:
        model = Examinee
        fields = ['id', 'test_id', 'name', 'email', 'total_score', 'created_at']