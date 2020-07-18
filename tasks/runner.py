import contextlib
import io
import os
import sys
import time

from datetime import datetime


def input():
    return "0\n"


@contextlib.contextmanager
def stdout_io(stdout=None):
    old_out = sys.stdout

    if stdout is None:
        stdout = io.StringIO()
    sys.stdout = stdout
    yield stdout

    sys.stdout = old_out


class Run:
    def __init__(self):
        self.TASK = None

    @staticmethod
    def get_times(t1: datetime, t2: datetime) -> (bool, bool, bool, bool, bool):
        t1ts = t1.timestamp()
        t2ts = t2.timestamp()
        m = t2ts // 60 > t1ts // 60
        h = t2ts // (60*60) > t1ts // (60*60)
        d = t2ts // (60*60*24) > t1ts // (60*60*24)
        w = t2ts // (60*60*24*7) > t1ts // (60*60*24*7)
        mo = t2.month != t2.month

        return m, h, d, w, mo

    def main(self):
        from DjangoTaskScheduler.models import Log, Task

        self.LOG = Log
        self.TASK = Task

        t = datetime.now()

        while True:
            m, h, d, w, mo = Run.get_times(t, t := datetime.now())

            if m:
                self.run_tasks("MINUTE")

            if h:
                self.run_tasks("HOURLY")

            if d:
                self.run_tasks("DAILY")

            if w:
                self.run_tasks("WEEKLY")

            if mo:
                self.run_tasks("MONTHLY")

            time.sleep(5)

    def run_tasks(self, f: str) -> None:
        tasks = self.TASK.objects.filter(frequency=f)

        for task in tasks:
            module = os.path.join("tasks", str(task.id), "__init__.py")

            if task.active:
                print(f"Running {task.name}")

                try:
                    with stdout_io() as s:
                        exec(open(module).read())

                    log = self.LOG(task=task, message=s.getvalue())
                    log.save()
                except Exception as e:
                    log = self.LOG(task=task, success=False, message=e)
                    log.save()
