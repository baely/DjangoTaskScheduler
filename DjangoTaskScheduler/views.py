from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from .models import TaskForm


def task_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = TaskForm()
        return render(request, "task/create.html", {"form": form})
