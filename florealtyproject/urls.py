"""
URL configuration for florealtyproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from feed import views
from django.contrib.auth import views as auth_views
# from .views import register_user, aboutpage
from florealtyproject import views as flo_views

urlpatterns = [
    path('register/', flo_views.register_user, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
   

    path('admin/', admin.site.urls),
    path("", flo_views.homepage),
    path("about/", flo_views.aboutpage),
    path("contactus/", flo_views.contactuspage),
    path("service/", flo_views.servicespage),
    path("", include("feed.urls"))
]
