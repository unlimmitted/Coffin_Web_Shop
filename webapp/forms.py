from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from webapp.models import *


class AddPost(forms.ModelForm):
    class Meta:
        model = CoffinList
        fields = ['title', 'content', 'photo']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = {'email', 'username', 'password1', 'password2'}


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={}))


class SendPurchaseRequest(forms.Form):
    coffin = forms.CharField(label='Гроб:', widget=forms.TextInput(attrs={}))
    comment = forms.CharField(label='Комментарий', widget=forms.Textarea(attrs={}))


class AddReview(forms.ModelForm):
    class Meta:
        model = ReviewList
        fields = ['title', 'content']
