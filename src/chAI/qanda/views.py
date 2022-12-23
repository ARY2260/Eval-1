from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import QuestionSubmissionForm
import requests
def questionPOST(question, totalMarks, Answer1, Answer2, Answer3, Answer4, Answer5):
    url = "https://cohereapi.asimjawahir.repl.co/answers"

    payload = {
        "question": question,
        "totalMarks": totalMarks,
        "answer1": Answer1,
        "answer2": Answer2,
        "answer3": Answer3,
        "answer4": Answer4,
        "answer5": Answer5
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'SL2v4gFFFQ9eEqHvDQ3Y7NGS5uvmI0U5',
    }

    response = requests.request("POST", url, headers=headers, json=payload)

    print(response.text.encode('utf8'))


def questionGET():
    url = "https://cohereapi.asimjawahir.repl.co/answers"

    response = requests.get(url)
    questions = []
    if response.status_code == 200:
        data = response.json()
        for item in data:
            questionDict = {
                "question": item['question'],
                "q_category": item['q_category'],
            }
            questions.append(questionDict)
        return questions
    return []


def home(request):
    return render(request, 'qanda/dashbaord.html')


def question(request):
    submitted = False
    if request.method == 'POST':
        form = QuestionSubmissionForm(request.POST)
        if form.is_valid():
            print("Valid")

            question = form.cleaned_data['question']
            totalMarks = form.cleaned_data['totalMarks']
            Answer1 = form.cleaned_data['Answer1']
            Answer2 = form.cleaned_data['Answer2']
            Answer3 = form.cleaned_data['Answer3']
            Answer4 = form.cleaned_data['Answer4']
            Answer5 = form.cleaned_data['Answer5']

            questionPOST(question, totalMarks, Answer1, Answer2, Answer3, Answer4, Answer5)

            return HttpResponseRedirect('/question?submitted=True')
    else:  
        form = QuestionSubmissionForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'qanda/question.html', {'form': form, 'submitted': submitted})
def answer(request):
    if request.method == 'GET':
        questionGET()
    return render(request, 'qanda/answer.html', {'questions': questionGET()})
# Create your views here.
