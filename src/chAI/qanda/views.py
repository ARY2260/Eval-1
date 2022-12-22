from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'qanda/dashbaord.html')
def question(request):
    return render(request, 'qanda/question.html')
def answer(request):
    return render(request, 'qanda/answer.html')
# Create your views here.
