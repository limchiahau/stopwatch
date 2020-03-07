import pyttsx3

class SpeechSynthesizer:
    def __init__(self):
        self.engine = pyttsx3.init()

        #A speech rate of 125 is what I feel
        #is a good rate.
        self.speech_rate = 125

    def say(self,text):
        '''
        Say the provided text.

        text is a string.
        '''
        #ensure that the speech rate is correct.
        #__set_speech_rate__ is called before say()
        #so that the speech rate is consistent.
        self.__set_speech_rate__()
        
        #tell the engine what to say.
        self.engine.say(text)

        #send the audio to the audio output
        self.engine.runAndWait()
        self.engine.stop()

    def __set_speech_rate__(self):
        self.engine.setProperty('rate', self.speech_rate)


class GenderedSpeechSynthesizer(SpeechSynthesizer):
    def __init__(self,gender):
        '''
        set the gender of the voice.

        gender is a string.
        
        gender should be "male" or "female"
        if gender is anything other than male
        the gender is presumed to be female.
        '''
        super().__init__()
        
        if gender == 'male':
            self.gender = 0
        else:
            # gender = female
            self.gender = 1

    def say(self,text):
        self.__set_voice__()
        super().say(text)

    def __set_voice__(self):
        '''
        __set_voice__ should be called everytime before
        the superclass say() method to ensure that the voice
        is of the propert gender.
        '''
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice',voices[self.gender].id)


class MaleSpeechSynthesizer(GenderedSpeechSynthesizer):
    def __init__(self):
        super().__init__('male')


class FemaleSpeechSynthesizer(GenderedSpeechSynthesizer):
    def __init__(self):
        super().__init__('female')
