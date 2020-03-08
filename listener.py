from pynput.keyboard import Key, Listener
from threading import Thread

class KeyboardListener:

    def on_enter(self,fn):
        '''
        fn will be called each time the enter key is pressed.
        '''

        #start a thread to listen to the enter key event.
        #This is to prevent this method from blocking.
        thread = Thread(target=self.process_callback,args=[fn])
        thread.start()
        
    def process_callback(self,fn):
        '''
        setup the listener to listen to the enter event.
        '''
        self.fn = fn
        with Listener(on_press=self._on_enter) as listener:
            listener.join()

    def _on_enter(self,key):
        '''
        call the provided callback if the enter is pressed.
        '''
        if key == Key.enter:
            self.fn()
