from django import forms
from models import *

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        return self.cleaned_data

    def save(self):
        ask = Question(**self.cleaned_data)
        ask.save()
        return ask

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField()

    def clean(self):
        return self.cleaned_data

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
