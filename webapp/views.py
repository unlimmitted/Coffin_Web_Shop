from django.shortcuts import render, get_object_or_404
from .forms import *
from webapp.models import *


def log_page(request):
    if request.method == 'POST':
        form_login = Login(request.POST)
        return render(request, "index.html", {'form': form_login})


def main_page(request):
    posts = coffinList.objects.all()
    return render(request, 'main.html', {'posts': posts})

def show_details(request, slug):
    details = get_object_or_404(coffinList, slug=slug)
    return render(request, 'coffin_page.html', context={'data': details})
def about(request):
    return render(request, 'about.html')
