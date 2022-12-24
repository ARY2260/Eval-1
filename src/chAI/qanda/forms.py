from django import forms
from django.forms import ModelForm
from .models import QuestionSubmission, AnswerSubmission
import requests

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

def getChoices():
    url = "https://cohereapi.asimjawahir.repl.co/answers"

    response = requests.get(url)
    questions = []
    if response.status_code == 200:
        data = response.json()
        for item in data:
            questionTuple = (item['q_category'], item['question'])
            questions.append(questionTuple)
        return questions
    return []

# class AnswerSubmissionForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         val = getChoices()
#         print(val)
#         self.fields['question'].queryset  = val
#     class Meta:
#         model = AnswerSubmission
#         fields = ['question', 'answer']
#         labels = {
#             'question': 'Question',
#             'answer': 'Answer',
#         }
#         widgets = {
#             'question': forms.Select(attrs={'class': 'form-control [border:1px_solid_#000] bg-white self-stretch box-border flex flex-row p-[12px] items-center justify-start w-full'}),
#             'answer': forms.Textarea(attrs={'class': 'form-control [border:1px_solid_#000] bg-white font-roboto text-base self-stretch box-border h-[182px] shrink-0 flex flex-row p-[12px] items-start justify-start'}),
#         }

class AnswerSubmissionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['question'] = forms.ChoiceField(
            choices=getChoices(), # this is the function call
            widget=forms.Select(attrs={'class': 'form-control [border:1px_solid_#000] bg-white self-stretch box-border flex flex-row p-[12px] items-center justify-start w-full'})
        )
        self.fields['answer'] = forms.CharField(
            widget=forms.Textarea(attrs={'class': 'form-control [border:1px_solid_#000] bg-white font-roboto text-base self-stretch box-border h-[182px] shrink-0 flex flex-row p-[12px] items-start justify-start'})
        )


class Answer(forms.Form):
    # CHOICES = ((1, 'Answer 1'),(2, 'Answer 2'),(3, 'Answer 3'),(4, 'Answer 4'),(5, 'Answer 5'))
    # field = forms.ChoiceField(choices=CHOICES)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['answer'] = forms.ChoiceField(
            choices=[('1', 'Answer 1'),('2', 'Answer 2'),('3', 'Answer 3'),('4', 'Answer 4'),('5', 'Answer 5')], # this is the function call
            widget=forms.Select(attrs={'class': 'form-control [border:1px_solid_#000] bg-white self-stretch box-border flex flex-row items-center justify-start'})
        )
