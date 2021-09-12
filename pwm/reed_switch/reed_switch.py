#! /usr/bin/env python

import RPi.GPIO as GPIO
BtnPin = 11
Gpin = 12
Rpin = 13

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Gpin, GPIO.OUT)
    GPIO.setup(Rpin, GPIO.OUT)
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(BtnPin, GPIO.BOTH, callback=detect, bouncetime=200)

def Led(x):
    if x == 0:
        GPIO.output(Rpin, 1)
        GPIO.output(Gpin, 0)

    if x == 1:
        GPIO.output(Gpin, 1)
        GPIO.output(Rpin, 0)

def Print(x):
    if x == 0:
        print('    *********************')
        print('    *  Button Pressed!  *')
        print('    *********************')

def detect(chn):
    Led(GPIO.input(BtnPin))
    print(GPIO.input(BtnPin))


def loop():
    while True:
        pass

def destroy():
    GPIO.output(Gpin, GPIO.HIGH)
    GPIO.output(Rpin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()