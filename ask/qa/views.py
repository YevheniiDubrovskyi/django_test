from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.core.paginator import Paginator
from models import *

def paginate(request, qs, baseurl):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10

    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404

    paginator = Paginator(qs, limit)
    paginator.baseurl = baseurl
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return page

def test(request, *args, **kwards):
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
        'paginator': page.paginator,
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
        'paginator': page.paginator,
        'page': page,
    })

@require_GET
def full_question(request, id):
    qt = get_object_or_404(Questions, id=id)
    return render(request, 'question.html', {
        'question': qt,
        'answers': qt.objects.get_answers(),
    })
