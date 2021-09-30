#! /usr/bin/env python
import RPi.GPIO as GPIO
import time

colors = [0xFF00, 0x00FF, 0x0FF0, 0xF00F]
pins = (11, 12)

GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)
GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins, GPIO.LOW)

p_R = GPIO.PWM(pins[0], 2000)
p_G = GPIO.PWM(pins[1], 2000)

p_R.start(0)
p_G.start(0)

def map(x, in_min, in_max, out_min, out_max):
    return (x-in_min)*(out_max-out_min)/(in_max-in_min) + out_min

def off():
    for i in pins:
        GPIO.output(pins[i], GPIO.HIGH)

def setColor(col):
    R_val = col >> 8
    G_val = col & 0x00FF
    # B_val = (col & 0x0000ff) >> 0

    R_val = map(R_val, 0, 255, 0, 100)
    G_val = map(G_val, 0, 255, 0, 100)
    # B_val = map(B_val, 0, 255, 0, 100)

    p_R.ChangeDutyCycle(100 - R_val)
    p_G.ChangeDutyCycle(100 - G_val)
    # p_B.ChangeDutyCycle(100 - B_val)


def loop():
    while True:
        for col in colors:
            setColor(col)
            time.sleep(1)

def destroy():
    p_R.stop()
    p_G.stop()
    # p_B.stop()
    off()
    GPIO.cleanup()

if __name__ == '__main__':
    # GPIO.cleanup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()