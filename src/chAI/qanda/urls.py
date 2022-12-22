from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("question/", views.question, name="question"),
    path("answer/", views.answer, name="answer"),
]