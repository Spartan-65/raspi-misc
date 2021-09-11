#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

RelayPin = 11    # pin11

def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(RelayPin, GPIO.OUT)
    GPIO.output(RelayPin, GPIO.LOW)

def loop():
    while True:
        print ('...relayd on')
        GPIO.output(RelayPin, GPIO.LOW)
        time.sleep(5)
        print ('relay off...')
        GPIO.output(RelayPin, GPIO.HIGH)
        time.sleep(5)

def destroy():
    GPIO.output(RelayPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()