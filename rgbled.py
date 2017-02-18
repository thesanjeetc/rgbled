import random, time
import RPi.GPIO as GPIO
import math
import thread

class rgbled:
    def __init__(self,rpin,gpin,bpin):
            self.rpin = rpin
            self.gpin = gpin
            self.bpin = bpin
            self.freq = 100
            self.setup(self.rpin,self.gpin,self.bpin,self.freq)


    def setup(self,rpin,gpin,bpin,freq):
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(rpin, GPIO.OUT)
            GPIO.setup(gpin, GPIO.OUT)
            GPIO.setup(bpin, GPIO.OUT)
            self.RED = GPIO.PWM(rpin, freq)
            self.RED.start(0)
            self.GREEN = GPIO.PWM(gpin, freq)
            self.GREEN.start(0)
            self.BLUE = GPIO.PWM(bpin, freq)
            self.BLUE.start(0)
            self.frequency = freq
            self.redprev = 1
            self.greenprev = 1
            self.blueprev = 1
            
    def changeto(self,redv,greenv,bluev,speed):
            GPIO.setwarnings(False)
            r = redv
            g = greenv
            b = bluev
            if(r == self.redprev or r == 0):
                    rx = self.redprev + 1
            else:
                    rx = abs(r-self.redprev)
            if(g == self.greenprev or g == 0):
                    gx = self.greenprev + 1
            else:
                    gx = abs(g-self.greenprev)
            if(b == self.blueprev or b == 0):
                    bx = self.blueprev + 1
            else:
                    bx = abs(b-self.blueprev)
            rs = speed/rx
            gs = speed/gx
            bs = speed/bx
            thread.start_new_thread(self.changered,(r,rs))
            thread.start_new_thread(self.changegreen,(g,gs))
            thread.start_new_thread(self.changeblue,(b,bs))

    def changered(self,red,speed):
            if(red > self.redprev):
                    for x in range (self.redprev,red):
                        self.RED.ChangeDutyCycle(x)
                        time.sleep(speed)
            else:
                    down = self.redprev - red
                    for x in range (0,down):
                        self.RED.ChangeDutyCycle(self.redprev - x )
                        time.sleep(speed)
            self.redprev = red

    def changegreen(self,green,speed):
            if(green > self.greenprev):
                    for x in range (self.greenprev,green):
                        self.GREEN.ChangeDutyCycle(x)
                        time.sleep(speed)
            else:
                    down = self.greenprev - green
                    for x in range (0,down):
                        self.GREEN.ChangeDutyCycle(self.greenprev - x )
                        time.sleep(speed)
            self.greenprev = green

    def changeblue(self,blue,speed):
            if(blue > self.blueprev):
                    for x in range (self.blueprev,blue):
                        self.BLUE.ChangeDutyCycle(x)
                        time.sleep(speed)
            else:
                    down = self.blueprev - blue
                    for x in range (0,down):
                        self.BLUE.ChangeDutyCycle(self.blueprev - x )
                        time.sleep(speed)
            self.blueprev = blue

    def on(self,r,g,b,speed):
            self.setup(self.rpin,self.gpin,self.bpin,self.freq)
            time.sleep(0.001)
            self.changeto(r,g,b,speed)
            
    def off(self,speed):
            self.changeto(1,1,1,speed)
            time.sleep(speed)
            self.RED.stop()
            self.GREEN.stop()
            self.BLUE.stop()

    def cleanup(self):
            self.RED.stop()
            self.GREEN.stop()
            self.BLUE.stop()
            GPIO.cleanup()
