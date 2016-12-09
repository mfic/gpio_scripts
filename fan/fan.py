#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
 
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))
 
temp_float = float(getCPUtemperature())
 
try: 
    if (temp_float > 47):
        print temp_float
        print "power on fan..."
        # ein
        GPIO.output(14, True)
        time.sleep(180)
        print "power off fan..."
        # aus
        GPIO.output(14, False)
        print float(getCPUtemperature())
    else:
        print temp_float
        print "temp too low"
 
except KeyboardInterrupt:
    print float(getCPUtemperature())
    print "power off fan..."
    GPIO.output(14, False)
    print "cancelling..."
