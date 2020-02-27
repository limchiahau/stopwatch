from stopwatch import Stopwatch, LappedStopwatch
from alternator import Alternator
from listener import KeyboardListener

def minutes(mins):
    return mins * 60

#s = Stopwatch(minutes(1))
s = LappedStopwatch(minutes(30),minutes(1))
alt = Alternator(lambda: s.pause(), lambda: s.resume())

s.start()

listener = KeyboardListener()
listener.on_enter(alt.toggle)

#keyboard.f._._.f.f._.f.e.f._._.f.e.f._._.g.a.g
#keyboard.f._._.f.f._.f.e.f._._.f.c
