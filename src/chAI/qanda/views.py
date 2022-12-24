from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import QuestionSubmissionForm, AnswerSubmissionForm, Answer
from .models import Tests
import requests
from datetime import datetime


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

def answerPOST(question, answer):
    url = "https://cohereapi.asimjawahir.repl.co/evaluate"

    payload = {
        "category": question,
        "answer": answer
    }

    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        return data
    return {}

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
                "totalMarks": item['totalMarks'],
            }
            questions.append(questionDict)
        return questions
    return []

def questionGETV2():
    url = "https://cohereapi.asimjawahir.repl.co/answers"

    response = requests.get(url)
    questions = []
    if response.status_code == 200:
        data = response.json()
        for item in data:
            questionDict = {
                "question": item['question'],
                "q_category": item['q_category'],
                "answer1": item['answer1'],
                "answer2": item['answer2'],
                "answer3": item['answer3'],
                "answer4": item['answer4'],
                "answer5": item['answer5'],
                "totalMarks": item['totalMarks'],
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
    form = AnswerSubmissionForm()
    submitted = False
    score = 0
    tag = ''
    if request.method == 'POST':
        form = AnswerSubmissionForm(request.POST)
        if form.is_valid():
            print("Valid")

            question = form.cleaned_data['question']
            answer = form.cleaned_data['answer']

            res = answerPOST(question, answer)
            score = res.get('score', 0)
            tag = res.get('tag', '')
            return HttpResponseRedirect(f'/answer?submitted=True&score={score}&tag={tag}&question={question}&answer={answer}')
    else:
        form = AnswerSubmissionForm()
        if 'submitted' in request.GET:
            submitted = True
            score = request.GET.get('score', 0)
            tag = request.GET.get('tag', 'Error')
            question = request.GET.get('question', '')
            answer = request.GET.get('answer', '')
            # store it in the database model Tests if it is not already there
            test = Tests.objects.filter(question=question, answer=answer)
            if not test:
                test = Tests(question=question, answer=answer, score=score, tag=tag, dateTime = datetime.now())
                test.save()
    return render(request, 'qanda/answer.html', {'form': form, 'submitted': submitted, 'score': score, 'tag': tag})

def test(request):
    # pass model test
    tests = Tests.objects.all()
    questions = questionGET()
    return render(request, 'qanda/test.html', {'tests': tests, 'questions': questions})

def questionBank(request):
    form = Answer()
    questions = questionGETV2()
    return render(request, 'qanda/questionBank.html', {'questions': questions, 'form': form})
# Create your views here.
