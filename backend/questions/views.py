from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Question

class QuestionListView(LoginRequiredMixin, ListView):
    model = Question
    template_name = 'questions/question_list.html'
    context_object_name = 'questions'

class QuestionDetailView(LoginRequiredMixin, DetailView):
    model = Question
    template_name = 'questions/question_detail.html'
    context_object_name = 'question'