from django import forms
from django.forms import ModelForm
from .models import QuestionSubmission


class QuestionSubmissionForm(ModelForm):
    class Meta:
        model = QuestionSubmission
        fields = ['question', 'totalMarks', 'Answer1', 'Answer2', 'Answer3', 'Answer4', 'Answer5']
        labels = {
            'question': 'Question',
            'totalMarks': 'Total Marks',
            'Answer1': 'Answer 1',
            'Answer2': 'Answer 2',
            'Answer3': 'Answer 3',
            'Answer4': 'Answer 4',
            'Answer5': 'Answer 5',
        }
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control [border:1px_solid_#000] bg-white self-stretch box-border flex flex-row p-[12px] items-center justify-start'}),
            'totalMarks': forms.TextInput(attrs={'class': 'form-control [border:1px_solid_#000] bg-white self-stretch box-border flex flex-row p-[12px] items-center justify-start'}),
            'Answer1': forms.Textarea(attrs={'class': 'form-control [border:1px_solid_#000] bg-white font-roboto text-base self-stretch box-border h-[182px] shrink-0 flex flex-row p-[12px] items-start justify-start'}),
            'Answer2': forms.Textarea(attrs={'class': 'form-control [border:1px_solid_#000] bg-white font-roboto text-base self-stretch box-border h-[182px] shrink-0 flex flex-row p-[12px] items-start justify-start'}),
            'Answer3': forms.Textarea(attrs={'class': 'form-control [border:1px_solid_#000] bg-white font-roboto text-base self-stretch box-border h-[182px] shrink-0 flex flex-row p-[12px] items-start justify-start'}),
            'Answer4': forms.Textarea(attrs={'class': 'form-control [border:1px_solid_#000] bg-white font-roboto text-base self-stretch box-border h-[182px] shrink-0 flex flex-row p-[12px] items-start justify-start'}),
            'Answer5': forms.Textarea(attrs={'class': 'form-control [border:1px_solid_#000] bg-white font-roboto text-base self-stretch box-border h-[182px] shrink-0 flex flex-row p-[12px] items-start justify-start'}),
        }
        # max_length = {
        #     'Answer1': 1000,
        #     'Answer2': 1000,
        #     'Answer3': 1000,
        #     'Answer4': 1000,
        #     'Answer5': 1000,
        # }

class AnswerSubmissionForm(forms.Form):
    class Meta:
        fields = []
