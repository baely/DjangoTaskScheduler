import time
from datetime import datetime
import traceback

class Run:
    @staticmethod
    def get_times(t1: datetime, t2: datetime) -> (bool, bool, bool, bool, bool):
        print(t1, t2)
        t1ts = t1.timestamp()
        t2ts = t2.timestamp()
        m = t2ts // 60 > t1ts // 60
        h = t2ts // (60*60) > t1ts // (60*60)
        d = t2ts // (60*60*24) > t1ts // (60*60*24)
        w = t2ts // (60*60*24*7) > t1ts // (60*60*24*7)
        mo = t2.month != t2.month

        return m, h, d, w, mo

    @staticmethod
    def main():
        traceback.print_stack()

        from DjangoTaskScheduler.models import Task

        t = datetime.now()

        while True:
            m, h, d, w, mo = Run.get_times(t, t := datetime.now())

            if m:
                pass

            if h:
                pass

            if d:
                pass

            if w:
                pass

            if mo:
                pass

            time.sleep(1)
