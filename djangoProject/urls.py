"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app01.views import account
from app01.views import tpl
from app01.views import my
from app01.views import check
from app01.views import deal
from app01.views import help

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", account.login, name='login'),
    path("home/", account.home, name='home'),
    path("logout/", account.logout, name="logout"),

    path("tpl/", tpl.tpl, name="tpl"),
    path("tpl/<int:pk>/edit/", tpl.tpl_edit, name="tpl_edit"),
    path("tpl/<int:pk>/delete/", tpl.tpl_delete, name="tpl_delete"),

    path("my/", my.my, name="my"),
    path("my/add/", my.my_add, name="my_add"),

    path("help/", help.help, name="help"),
    path("help/action/<int:action>/<int:oid>/", help.help_action, name="help_action"),

    path("deal/", deal.deal, name="deal"),
    path("deal/action/<int:action>/<int:oid>/", deal.deal_action, name="deal_action"),

    path("check/", check.check, name="check"),
    path("check/action/<int:action>/<int:oid>/", check.check_action, name="check_action"),
]
