from django.db.models import Model, AutoField, CharField, ForeignKey, CASCADE
from django.forms import ModelForm


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
    file = CharField(max_length=255)

    def __str__(self):
        return self.name


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "frequency", "file"]
