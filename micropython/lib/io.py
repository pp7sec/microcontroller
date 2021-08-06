#from lib.io import p_digitalOut, p_digitalIn, p_analogIn, p_sleep

from machine import Pin, ADC
import time

class p_digitalOut:
    def __init__(self, gpio):
        self.gpio = Pin(gpio, Pin.OUT)
        
    def p_high(self):
        self.gpio.on()
        
    def p_low(self):
        self.gpio.off()
        
    def p_read(self):
        return self.gpio.value()
    
class p_digitalIn:
    def __init__(self, gpio, mode = None):
        if type(mode) == str:
            if mode.upper() == 'UP':
                self.gpio = Pin(gpio, Pin.IN, Pin.PULL_UP)
            elif mode.upper() == 'DOWN':
                self.gpio = Pin(gpio, Pin.IN, Pin.PULL_DOWN)
            else:
                self.gpio = Pin(gpio, Pin.IN)
        else:
            self.gpio = Pin(gpio, Pin.IN)
            
    def p_read(self):
        return self.gpio.value()
    
class p_analogIn:
    def __init__(self, gpio):
        self.gpio = ADC(Pin(gpio))
        #self.gpio.atten(ADC.ATTN_0DB)      #the full range voltage: 1.2V
        #self.gpio.atten(ADC.ATTN_2_5DB)    #the full range voltage: 1.5V
        #self.gpio.atten(ADC.ATTN_6DB)      #the full range voltage: 2.0V
        self.gpio.atten(ADC.ATTN_11DB)     #the full range voltage: 3.3V
        
        #ADC.WIDTH_9BIT: (range 0 to 511)
        #ADC.WIDTH_10BIT: (range 0 to 1023)
        #ADC.WIDTH_11BIT: (range 0 to 2047)
        #ADC.WIDTH_12BIT: (range 0 to 4095)
        
    def p_read(self):
        return self.gpio.read()
    

def p_sleep(delay_time):
    time.sleep(delay_time)
    
