"""DjangoTaskScheduler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic.base import RedirectView
from .models import TaskList
from .views import task_create, task_edit, task_list

urlpatterns = [
    path("task/create", task_create, name="task_create"),
    path("task/edit/<int:pk>", task_edit, name="task_edit"),
    path("task/list", TaskList.as_view(template_name="task/list.html"), name="task_list"),
    path("", RedirectView.as_view(pattern_name="task_list", permanent=True))
]
