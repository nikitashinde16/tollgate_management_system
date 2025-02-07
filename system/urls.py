"""
URL configuration for tollgate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from system import views

urlpatterns = [
   # path('admin/', admin.site.urls),
    path("register",views.register),
    path("studentdata",views.studentdata),
    path("searchperson",views.searchperson),
    path("home",views.home),
    path("login",views.login),
    path("changepassword",views.changepassword),
    path("ticketbook",views.ticketbook),
    path("tollnumber",views.tollnumber),
    path("tolldata",views.tolldata),
    path("home",views.home),
    path("pay",views.pay),
    path("paydata",views.paydata),
]
