# RGB_Led

Use this python library to control your rgb leds with smooth color changes between colors. First you need to import the library like this:

	from rgbled import rgbled

And then you can use the functions below.
Note that this has to be in the same folder as your script in order for it to be found and imported.

To start off, a rgbled object has to be created:

	led = rgbled(rpin,gpin,bpin) - takes the parameters red pin, green pin, blue pin

Here are the methods :

     led.changeto(r,g,b,speed) - takes the parameters red value, green value, blue value and speed

        The speed is how fast the color transition is and the colour values must be between 0 and 100. It is in seconds and works best around 2 or less.

     led.off(speed) - takes parameters speed
	
	The speed is how fast the led turns off. The RGB LED turns off completely.

     led.on(r,g,b,speed) - takes the parameters red value, green value, blue value and speed
	
	This must be run after the off() method. The speed is how fast the color transition is and the colour values must be between 0 and 100. It is in seconds and works best around 2 or less.

     led.cleanup() - 

        This needs to be run at the end of your script so that the pins can be used again.

Have fun playing around with your rgb led!
