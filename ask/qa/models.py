from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.contrib.auth.models import User

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

class QuestionManager(models.Manager):
    def main(self):
        return self.order_by('-id')
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='likes_set')

    objects = QuestionManager()

    def get_url(self):
        return reverse('question', kwargs={'id': self.id})

class AnswerManager(models.Manager):
    def get_answers(self, id):
        return self.filter(question=id)

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    objects = AnswerManager()

    def get_question_url(self):
        return reverse('question', kwargs={'id': self.question_id})
