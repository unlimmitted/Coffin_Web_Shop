"""Interception_of_login_data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from webapp import views
from Interception_of_login_data import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('login/', views.LoginUser.as_view(), name='login'),
                  path('register/', views.RegisterUser.as_view(), name='register'),
                  path('logout/', views.logout_user, name='logout'),
                  path('', views.CoffinHome.as_view(), name='home'),
                  path('about/', views.about, name='about'),
                  path('coffin/<str:slug>', views.show_details, name='details'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
