from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import *
from webapp.models import *
from .utils import *


class coffinHome(DataMixin, ListView):
    model = coffinList
    template_name = 'index.html'
    context_object_name = 'objects'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Ритуальные услуги ККМТ")
        return dict(list(context.items()) + list(c_def.items()))

def login(request):
    return render(request, 'login.html')


def show_details(request, slug):
    details = get_object_or_404(coffinList, slug=slug)
    return render(request, 'coffin_page.html', context={'data': details})


def about(request):
    return render(request, 'about.html')

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация пользователя")
        return dict(list(context.items()) + list(c_def.items()))
