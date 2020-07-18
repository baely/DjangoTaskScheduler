from django.db.models import Model, AutoField, BooleanField, CharField, ForeignKey, TextField, CASCADE
from django.forms import ModelForm
from django.views.generic import ListView

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


class TaskList(ListView):
    model = Task
    paginate_by = 20
