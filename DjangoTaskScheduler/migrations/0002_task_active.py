# Generated by Django 2.1.15 on 2020-07-18 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoTaskScheduler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
