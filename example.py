from rgbled import rgbled
from random import randint
import time

led = rgbled(11,9,10)

try:
    while True:
        r = randint(0,100)
        g = randint(0,100)
        b = randint(0,100)
        led.changeto(r,g,b,0.8)
        time.sleep(2)
        
except KeyboardInterrupt:
    led.off(0.8)
    led.cleanup()

    
