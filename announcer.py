from speech import FemaleSpeechSynthesizer

class LapAnnouncer:
    '''
    An announcer that provides a vocal queue each time
    a lap has paased.

    A lap is assumed each time the toggle method is called.
    '''
    def __init__(self):
        #defaults to 1 so the first lap is lap 1.
        self._count = 1
        
        #used to produce the lap announcement
        self.announcer = FemaleSpeechSynthesizer()

    def toggle(self):
        '''Record that a lap has passed'''
        self.announcer.say(self.lap())
        self._count += 1

    def lap(self):
        '''
        returns a string that represents the
        current lap.
        '''
        return f'Lap {self._count}'
