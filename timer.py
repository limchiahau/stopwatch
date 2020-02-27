from threading import Timer


class IntervalTimer:
    def __init__(self,seconds,fn):
        self.timer = None
        self.fn = fn
        self.interval = seconds
        self.active = True

    def start(self):
        self.timer = Timer(self.interval,self.run)
        self.timer.start()

    def resume(self):
        self.active = True

    def stop(self):
        self.active = False

    def run(self):
        if self.active:
            self.fn()
        self.start()


class SecondsTimer(IntervalTimer):
    def __init__(self,fn):
        super().__init__(1,fn)
