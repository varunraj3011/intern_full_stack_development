from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import RegisterForm, QuestionForm
from .models import Question
from .openai_service import get_ai_answer


def home(request):
    if request.user.is_authenticated:
        return redirect('ask')
    topics = [
        "3-phase induction motors",
        "DC motor back EMF",
        "Transformer losses",
        "Synchronous generators",
        "Motor efficiency",
        "Motor overheating causes",
        "Universal motors",
        "Stepper motors"
    ]

    return render(request, 'qa/home.html', {
        'topics': topics
    })

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}!')
            return redirect('ask')
    else:
        form = RegisterForm()
    return render(request, 'qa/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('ask')
    else:
        form = AuthenticationForm()
    return render(request, 'qa/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def ask_view(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            q = form.save(commit=False)
            q.user = request.user
            q.answer = get_ai_answer(q.question)
            q.save()
            return redirect('question_detail', pk=q.pk)
    else:
        form = QuestionForm()
    recent = Question.objects.filter(user=request.user)[:5]
    return render(request, 'qa/ask.html', {'form': form, 'recent': recent})


@login_required
def history_view(request):
    questions = Question.objects.filter(user=request.user)
    return render(request, 'qa/history.html', {'questions': questions})


@login_required
def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk, user=request.user)
    return render(request, 'qa/question_detail.html', {'question': question})