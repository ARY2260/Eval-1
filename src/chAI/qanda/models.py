from django.db import models
from django.contrib.auth.models import User
from datetime import date

class QuestionSubmission(models.Model):
    question = models.CharField(max_length=200)
    totalMarks = models.IntegerField()
    Answer1 = models.CharField(max_length=2000)
    Answer2 = models.CharField(max_length=2000)
    Answer3 = models.CharField(max_length=2000)
    Answer4 = models.CharField(max_length=2000)
    Answer5 = models.CharField(max_length=2000)
    def __str__(self):
        return self.question
        
class AnswerSubmission(models.Model):
    question = models.CharField(max_length=2000)
    answer = models.CharField(max_length=2000)
    def __str__(self):
        return self.question

class Tests(models.Model):
    # make testId into auto increment
    testId = models.AutoField(primary_key=True)
    question = models.CharField(max_length=2000)
    answer = models.CharField(max_length=2000)
    score = models.FloatField()
    tag = models.CharField(max_length=2000)
    dateTime = models.DateTimeField(default=date.today)
    def __str__(self):
        return self.question
# Create your models here.
