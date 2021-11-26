#! /usr/bin/env python3

import RPi.GPIO as GPIO


def setup(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def destroy(pin):
    GPIO.output(pin, GPIO.LOW)
    GPIO.setup(pin, GPIO.IN)
    GPIO.cleanup()


if __name__ == '__main__':
    pin = 7
    try:
        setup(pin)
        while True:
            pass
    except KeyboardInterrupt:
        destroy(pin)