#coding: utf8

from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from models import paginate, Question, Answer
from forms import AskForm, AnswerForm, SignupForm, LoginForm

def test(request, *args, **kwargs):
    return HttpResponse('OK')

@require_GET
def new_questions(request):
    try:
        questions = Question.objects.main()
    except Question.DoesNotExist:
        raise Http404
    page = paginate(request, questions, '/?page=')
    return render(request, 'new_questions.html', {
        'questions': page.object_list,
        'page': page,
    })

@require_GET
def popular_questions(request):
    try:
        questions = Question.objects.popular()
    except Question.DoesNotExist:
        raise Http404
    page = paginate(request, questions, '/popular/?page=')
    return render(request, 'popular_questions.html', {
        'questions': page.object_list,
        'page': page,
    })

@require_GET
def full_question(request, id):
    question = get_object_or_404(Question, id=id)
    form = AnswerForm(initial = {'question_id': question.id})
    return render(request, 'question.html', {
        'question': question,
        'answers': Answer.objects.get_answers(question.id),
        'form': form,
    })

def add_ask(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            form = AskForm(request.POST)
            form._user = request.user
            if form.is_valid():
                ask = form.save()
                url = ask.get_url()
                return HttpResponseRedirect(url)
        else:
            return HttpResponseRedirect(reverse('login'))
    else:
        form = AskForm()
    return render(request, 'add_ask.html', {
        'form': form,
    })

def add_answer(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            form = AnswerForm(request.POST)
            form._user = request.user
            if form.is_valid():
                answer = form.save()
            url = answer.get_question_url()
            return HttpResponseRedirect(url)
        else:
            return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponseRedirect(reverse('base'))

def signup(request):
    error = ''
    if request.method == 'POST':
        user = SignupForm(request.POST)
        if user.is_valid():
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('base'))
        else:
            error = u'Не валидный пользователь'
    else:
        user = SignupForm(request.POST)
    return render(request, 'signup.html', {
        'form': user,
        'error': error,
    })

def login(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('base'))
        else:
            form = LoginForm(request.POST)
            error = u'Неверный логин \ пароль'
    else:
        form = LoginForm()
    return render(request, 'login.html', {
        'form': form,
        'error': error,
    })
