from stopwatch import Stopwatch, LappedStopwatch
from alternator import Alternator
from listener import KeyboardListener

def minutes(mins):
    return mins * 60

s = LappedStopwatch(minutes(30),minutes(1))
alt = Alternator(lambda: s.pause(), lambda: s.resume())

#toggle alternator when enter is pressed.
listener = KeyboardListener()
listener.on_enter(alt.toggle)

#start the LappedStopwatch.
s.start()

