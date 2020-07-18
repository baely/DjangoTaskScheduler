from django.db.models import Model, AutoField, BooleanField, CharField, DateTimeField, IntegerField, ForeignKey, TextField, CASCADE
from django.forms import ModelForm
from django.utils import timezone
from django.views.generic import DetailView, ListView

import os


FREQUENCIES = [
    ("MINUTE", "Minute"),
    ("HOURLY", "Hourly"),
    ("DAILY", "Daily"),
    ("WEEKLY", "Weekly"),
    ("MONTHLY", "Monthly")
]


class Task(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255)
    frequency = CharField(max_length=16, choices=FREQUENCIES)
    active = BooleanField(default=True)
    script = TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        task_dir = os.path.join("tasks", str(self.id))

        if not os.path.exists(task_dir):
            os.mkdir(task_dir)

        with open(os.path.join(task_dir, "__init__.py"), "w") as f:
            f.write(self.script)


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "frequency", "active", "script"]


class TaskView(DetailView):
    model = Task
    template_name = "task/view.html"


class TaskList(ListView):
    model = Task
    ordering = ["id"]
    paginate_by = 20
    template_name = "task/list.html"


class Log(Model):
    id = AutoField(primary_key=True)
    time = DateTimeField()
    task = ForeignKey(Task, on_delete=CASCADE)
    success = BooleanField(default=True)
    runtime = IntegerField(default=0)
    message = TextField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.time = timezone.now()

        return super().save(*args, **kwargs)


class LogList(ListView):
    model = Log
    ordering = ["-id"]
    paginate_by = 100
    template_name = "task/loglist.html"


class LogView(DetailView):
    model = Log
    template_name = "task/logview.html"
