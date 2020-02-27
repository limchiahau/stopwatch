from timer import SecondsTimer
from pyfiglet import Figlet
import os
import winsound
import time


class Stopwatch:
    '''
    A stopwatch that plays a ringtone once the time is up.
    '''
    def __init__(self,duration):
        '''
        duration is in seconds.
        '''
        self.ringer = Ringer()
        self.time_left = Time(duration)
        self.display = ConsolePrinter()
        self.interval_timer = None
        self.paused = False

    def start(self):
        '''
        start the stopwatch
        '''
        self.init_timer()
        self.interval_timer.start()

    def pause(self):
        '''
        pause the stopwatch
        '''
        self.interval_timer.stop()
        self.__set_pause__(True)

    def resume(self):
        '''
        resume the stopwatch
        '''
        self.interval_timer.resume()
        self.__set_pause__(False)

    def end(self):
        self.interval_timer.stop()
        self.ringer.end()

    def init_timer(self):
        self.interval_timer = SecondsTimer(self.tick)

    def tick(self):
        '''
            this method should only be called once a second.

            tells the stopwatch object that 1 second has passed.
        '''
        self.display_time()
        self.time_left.reduce()

        if self.time_left.is_zero():
            self.end()

    def __set_pause__(self,pause_state):
        self.paused = pause_state
        self.display_time()

    def display_time(self):
        self.display.print(str(self.time_left))

        if self.paused:
            self.display.print_without_clear('PAUSED')


class LappedStopwatch(Stopwatch):
    '''
    A stopwatch that plays a sound:
    - at every interval, specified by lap_time;
    - at the end of the duration.
    '''
    def __init__(self,duration,lap_time):
        '''
        duration and lap_time is in seconds
        '''
        super().__init__(duration)
        self.countdown = Countdown(lap_time,self.ringer.alert)

    def tick(self):
        super().tick()
        self.countdown.toggle()


class Countdown:
    def __init__(self,count,fn):
        '''
        count is a natural number.
        fn is the function that will be called once the countdown
        reaches zero.
        '''
        self.original_count = count
        self.count = count
        self.callback = fn

    def toggle(self):
        '''
        decrese the count by 1.
        and call the function passed to the initializer.
        '''
        if self.has_ended():
            self.callback()
            self.reset()

        self.count -= 1

    def reset(self):
        '''
        reset the countdown to its original state.
        '''
        self.count = self.original_count

    def has_ended(self):
        return self.count <= 0
        

class Keyboard:
    '''
    A virtual musical keyboard.
    
    '''
    @property
    def c(self):
        '''
        Play the middle c.
        '''
        return self.play_frequency(261)

    @property
    def d(self):
        '''
        Play the middle d.
        '''
        return self.play_frequency(293)

    @property
    def e(self):
        '''
        Play the middle e.
        '''
        return self.play_frequency(329)

    @property
    def f(self):
        '''
        Play the middle f.
        '''
        return self.play_frequency(349)

    @property
    def g(self):
        '''
        Play the middle g.
        '''
        return self.play_frequency(392)

    @property
    def a(self):
        '''
        Play the middle a.
        '''
        return self.play_frequency(440)

    @property
    def b(self):
        '''
        Play the middle b.
        '''
        return self.play_frequency(493)

    @property
    def _(self):
        time.sleep(self.duration / 10)
        return self

    def play_frequency(self,frequency):
        '''Produces a certain frequency'''
        winsound.Beep(frequency,self.duration * 50)
        return self

    @property
    def duration(self):
        '''Specifies the duration of the blank note and play_frequency'''
        return 4


class Ringer:
    '''
    Container for a set of ringtones produced using a virtual
    keyboard.
    '''
    def __init__(self):
        self.keyboard = Keyboard()
        
    def alert(self):
        self.keyboard.f.f

    def end(self):
        self.keyboard.c.d.e.f.e.d.c

    def titanic(self):
        '''my heart will go on'''
        self.keyboard.f._._.f.f._.f.e.f._._.f.e.f._._.g.a.g
        self.keyboard.f._._.f.f._.f.e.f._._.f.c


class Time:
    def __init__(self,duration):
        '''
            durations is an integer which represents
            a second.
        '''
        self.duration = duration

    def reduce(self):
        '''reduce the remaining time by 1 second'''
        if not self.is_zero():
            self.duration -= 1

    def is_zero(self):
        '''check if the remaining duration is zero'''
        return self.duration < 0

    def __repr__(self):
        '''
            represents the remaining time in this format:
            hh :: mm :: ss
        '''
        return f'{self.hours_left()} :: {self.minutes_left()} :: {self.seconds_left()}'

    def __str__(self):
        return self.__repr__()

    def hours_left(self):
        return self.duration // 60 // 60

    def minutes_left(self):
        return self.duration // 60

    def seconds_left(self):
        return self.duration % 60
    

class ConsolePrinter:
    def __init__(self):
        self.renderer = Figlet()
        
    def print(self,string):
        self.clear_cmd_line()
        self.print_without_clear(string)

    def print_without_clear(self,string):
        #add a spacer to the left of every text
        output = '  ' + string
        print(self.renderer.renderText(output))

    def clear_cmd_line(self):
        os.system('cls')
