from django.contrib.auth.models import User
from django import forms
from models import Question, Answer

class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text', 'author']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question', 'author']

class SignupForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=100, required=False)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        return self.cleaned_data

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
