from django.contrib import admin
from .models import (
    Test,
    Question,
    Examinee,
    Submission
)

class QuestionInline(admin.TabularInline):
    model = Question

class SubmissionInline(admin.TabularInline):
    model = Submission

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline,
    ]

@admin.register(Examinee)
class ExamineeAdmin(admin.ModelAdmin):
    inlines = [
        SubmissionInline,
    ]