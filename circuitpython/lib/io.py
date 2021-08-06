#from lib.io import p_digitalOut, p_digitalIn, p_analogIn, p_sleep

from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
import board
import time

class p_digitalOut:
    def __init__(self, pin):
        self.pin = getattr(board, 'GP'+str(pin))
        self.gpio = DigitalInOut(self.pin)
        self.gpio.direction = Direction.OUTPUT
        
    def p_high(self):
        self.gpio.value = True
        
    def p_low(self):
        self.gpio.value = False
        
    def p_read(self):
        value = self.gpio.value
        if value == True:
            return 1
        elif value == False:
            return 0
        #return self.gpio.value

class p_digitalOut:
    def __init__(self, pin, mode = None):
        self.pin = getattr(board, 'GP'+str(pin))
        self.gpio = DigitalInOut(self.pin)
        self.gpio.direction = Direction.INPUT
        if type(mode) == str:
            if mode.upper() == 'UP':
                self.gpio.pull = Pull.UP
            elif mode.upper() == 'DOWN':
                self.gpio.pull = Pull.DOWN
                
    def p_read(self):
        value = self.gpio.value
        if value == True:
            return 1
        elif value == False:
            return 0
        
class p_analogIn:
    def __init__(self, pin):
        self.pin = getattr(board, 'GP'+str(pin))
        self.gpio = AnalogIn(self.pin)
        
    def p_read(self):
        return self.gpio.value
    
    def p_read3v3(self):
        return (self.gpio.value * 3.3) / 65536
    
    def p_read5v(self):
        return (self.gpio.value * 5) / 65536
    
def p_sleep(delay_time):
    time.sleep(delay_time)


