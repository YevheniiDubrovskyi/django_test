from django.contrib.auth.models import User
from django import forms
from models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length = 255)
    text = forms.CharField(widget = forms.Textarea)
    _user = forms.IntegerField(widget = forms.HiddenInput)

    def clean(self):
        return self.cleaned_data

    def save(self):
        self.cleaned_data['author'] = self._user
        ask = Question(**self.cleaned_data)
        ask.save()
        return ask

class AnswerForm(forms.Form):
    text = forms.CharField(widget = forms.Textarea)
    question_id = forms.IntegerField(widget = forms.HiddenInput)
    _user = forms.IntegerField(widget = forms.HiddenInput)

    def clean(self):
        return self.cleaned_data

    def save(self):
        self.cleaned_data['author'] = self._user
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

class SignupForm(forms.Form):
    username = forms.CharField(max_length = 30)
    email = forms.EmailField(max_length = 100, required = False)
    password = forms.CharField()

    def clean(self):
        return self.cleaned_data

    def save(self):
        user = User(**self.cleaned_data)
        user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 30)
    password = forms.CharField()

    def clean(self):
        return self.cleaned_data
