from django.urls import path
from . import views

app_name = 'eval'

urlpatterns = [
    path('api/tests', views.TestListView.as_view(), name='test_list'),
    path('api/examinees', views.ExamineeListView.as_view(), name='examinee_list'),
]