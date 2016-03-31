from django import forms
from models import Question, Answer

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
    question_id = forms.IntegerField(widget=forms.HiddenInput)

    def clean(self):
        return self.cleaned_data

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

class SignupForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=100)
