from threading import Timer
import time


class IntervalTimer:
    def __init__(self,seconds,fn):
        '''
        seconds is a natural number.
        It represents the interval that the timer is going
        to use.

        fn is a function.
        fn will be called at each interval defined by seconds.
        '''
        self.timer = None
        self.fn = fn
        self.interval = seconds
        self.active = True

    def start(self):
        '''
        Start the interval timer.

        Note: This method is blocking. It is suggested that
        this method be called near the end of the program.

        Note2: I've used a while loop instead of a callback
        here to resolve a conflict between this class and the
        SpeechSynthesizer class.
        '''
        while True:
            time.sleep(self.interval)
            self._run()

    def resume(self):
        self.active = True

    def stop(self):
        self.active = False

    def _run(self):
        if self.active:
            self.fn()


class SecondsTimer(IntervalTimer):
    def __init__(self,fn):
        super().__init__(1,fn)
