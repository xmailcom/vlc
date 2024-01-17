import threading
import time


class PyTimer:

    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.running = False

    def _run_func(self):
        th = threading.Thread(target=self.func, args=self.args, kwargs=self.kwargs)
        th.setDaemon(True)
        th.start()

    def _start(self, interval, once):
        if interval < 0.010:
            interval = 0.010

        if interval < 0.050:
            dt = interval / 10
        else:
            dt = 0.005

        if once:
            deadline = time.time() + interval
            while time.time() < deadline:
                time.sleep(dt)

            if self.running:
                self._run_func()
        else:
            self.running = True
            deadline = time.time() + interval
            while self.running:
                while time.time() < deadline:
                    time.sleep(dt)

                deadline += interval

                if self.running:
                    self._run_func()

    def start(self, interval, once=True):
        """启动定时器

        interval    - 定时间隔，浮点型，以毫秒为单位，最高精度10毫秒
        once        - 是否仅启动一次
        """

        th = threading.Thread(target=self._start, args=(interval / 1000, once))
        th.setDaemon(True)
        th.start()

    def stop(self):
        self.running = False
