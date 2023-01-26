from django import forms
from webapp.models import *


class Login(forms.Form):
    Login = forms.CharField(max_length=255, label='', required=False,
                            widget=forms.TextInput(attrs={'name': 'login',
                                                          'id': '',
                                                          'class': 'form-control',
                                                          'placeholder': 'Телефон или email'}))
    Password = forms.CharField(max_length=255, label='', required=False,
                               widget=forms.TextInput(attrs={'name': 'pass',
                                                             'id': '',
                                                             'type': 'password',
                                                             'class': 'form-control',
                                                             'placeholder': 'Пароль'}))
class addPost(forms.ModelForm):
    class Meta:
        model = coffinList
        fields = ['title', 'content', 'photo']