#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

pwm = PWM(0x40, debug=True)

def setColor(redPin, rgb):
  #convert from 255 to 12bit 
  for c in rgb:
    dc =  int(((int(c) / float(255)) * float(4095)) - 4095) * -1
    pwm.setPWM(redPin, 0, dc)
    redPin += 1

pwm.setPWMFreq(100)                        # Set frequency to 60 Hz
while (True):
    
  cmd = raw_input('Enter a comma separated RGB value: ').split(',')
  
  setColor(0, cmd)

