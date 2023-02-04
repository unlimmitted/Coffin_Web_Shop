import telebot
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from Interception_of_login_data import settings
from .forms import *
from webapp.models import *
from .utils import *


def create_review(request):
    form = AddReview(request.POST)
    if form.is_valid():
        review_data = form.save(commit=False)
        review_data.username = request.user.username
        review_data.save()
        return redirect('about')


def show_details(request, slug):
    details = get_object_or_404(CoffinList, slug=slug)
    form = SendPurchaseRequest(request.POST)
    return render(request, 'coffin_page.html', context={'data': details, 'form': form})


def send_message(request):
    form = SendPurchaseRequest(request.POST or None)
    if form.is_valid():
        bot = telebot.TeleBot(settings.TELEGRAM_API)
        bot.send_message(settings.CHAT_ID,
                         f'Username: {request.user.username}\nEmail: {request.user.email}'
                         f'\nCoffin: {request.POST.get("coffin")}'
                         f'\nComment: {form.cleaned_data.get("comment")}')
        return redirect('home')


def about(request):
    all_review = ReviewList.objects.all()
    form = AddReview(request.POST)
    return render(request, 'about.html', {'create_review': form, 'all_review': all_review})


def logout_user(request):
    logout(request)
    return redirect('login')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация пользователя")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Вход пользователя")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class CoffinHome(DataMixin, ListView):
    model = CoffinList
    template_name = 'index.html'
    context_object_name = 'objects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Ритуальные услуги ККМТ")
        return dict(list(context.items()) + list(c_def.items()))
