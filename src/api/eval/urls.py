from django.urls import path
from . import views

app_name = 'eval'

urlpatterns = [
    path('api/tests/', views.TestListView.as_view(), name='test_list'),
    path('api/examinees/', views.ExamineeListView.as_view(), name='examinee_list'),
    path('api/questions/', views.QuestionListView.as_view(), name='question_list'),
    path('api/submissions/', views.SubmissionListView.as_view(), name='submission_list'),

    path('api/alltests', views.TestAndQuestionsView.as_view(), name='test_and_questions'),
    path('api/questions/<int:test_id>/', views.QuestionsByTestView.as_view(), name='questions_by_test'),
]