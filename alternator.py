class Alternator:
    '''
        Given 2 functions fn1 and fn2 calling the toggle
        function will alternate between calling fn1 and fn2.
    '''
    def __init__(self,fn1,fn2):
        self.fn1 = fn1
        self.fn2 = fn2
        self.call_fn1 = True

    def toggle(self):
        if self.call_fn1:
            self.fn1()
        else:
            self.fn2()

        self.alternate()

    def alternate(self):
        '''
            manage state of call_fn1 so that we
            know which function to call
        '''
        self.call_fn1 = not self.call_fn1
