from pynput.keyboard import Key, Listener


class KeyboardListener:
    
    def on_enter(self,fn):
        self.fn = fn
        with Listener(on_press=self._on_enter) as listener:
            listener.join()

    def _on_enter(self,key):
        if key == Key.enter:
            self.fn()
