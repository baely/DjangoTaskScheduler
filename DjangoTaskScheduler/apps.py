from django.apps import AppConfig
from tasks.runner import Run
from threading import Thread


class DTSAppConfig(AppConfig):
    name = "DjangoTaskScheduler"

    def ready(self):
        run = Run()

        t = Thread(target=run.main)
        t.daemon = True
        t.start()
