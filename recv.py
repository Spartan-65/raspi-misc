import pwm.led.python.rgb_led as RGB

import _thread
import os
from socket import *

record_flag = True

def recAlert():
    global record_flag
    try:
        _thread.start_new_thread(RGB.blinkColor, (RGB.colors[5],))
    except:
        pass

    try:
        if record_flag:
            print("recording")
            os.system("raspivid -o /home/pi/vid/vid_`date +%Y%m%d%H%M%S`.h264 -t 60000 -w 640 -h 480 -fps 25 -b 1200000 -p 0,0,8,6")
    except:
        pass

if __name__ == '__main__':
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(('0.0.0.0', 9002))
    
    while True:
        print("wait...")
        data, address = s.recvfrom(16)
        print(data, address)
        recv_str = data.decode()
        if recv_str.startswith('close'):
            record_flag = False
        elif recv_str.startswith('record'):
            record_flag = True
            continue
        recAlert()
    s.close()
