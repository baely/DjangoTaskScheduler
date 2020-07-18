from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from .models import Task, TaskForm


def empty_return(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    message = "#TODO"
    return render(request, "message.html", {"message": message})


def task_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = TaskForm()
        return render(request, "task/create.html", {"form": form})


def task_edit(request: HttpRequest, pk: int) -> HttpResponse:
    instance = Task.objects.get(id=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=instance)
        if form.is_valid():
            instance.save()
            return redirect(f"/task/view/{instance.id}")

    else:
        form = TaskForm(instance=instance)
        return render(request, "task/edit.html", {"form": form, "id": instance.id})
