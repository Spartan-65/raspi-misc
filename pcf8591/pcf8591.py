#!/usr/bin/env python

import smbus
import time

bus = smbus.SMBus(1)

def setup(Addr):
    global address
    address = Addr

def read(chn): #channel
    if chn == 0:
        bus.write_byte(address,0x40)
    if chn == 1:
        bus.write_byte(address,0x41)
    if chn == 2:
        bus.write_byte(address,0x42)
    if chn == 3:
        bus.write_byte(address,0x43)
    bus.read_byte(address)
    return bus.read_byte(address)

def write(val):
    temp = val
    temp = int(temp)
    # print temp to see on terminal else comment out
    bus.write_byte_data(address, 0x40, temp)

if __name__ == "__main__":
    setup(0x48)
    while True:
        print ('AIN0 = ' + str(read(0)))
        print ('AIN1 = ' + str(read(1)))
        print ('AIN2 = ' + str(read(2)))
        tmp = read(1)
        tmp = tmp*(255-125)/255+125

        write(tmp)
        time.sleep(2)
