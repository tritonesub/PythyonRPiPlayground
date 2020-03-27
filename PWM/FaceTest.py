#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

pwm = PWM(0x40, debug=True)
pwm2 = PWM(0x41, debug=True)

def setColor(redPin, rgb, p):
  #convert from 255 to 12bit 
  for c in rgb:
    dc =  int(((int(c) / float(255)) * float(4095)) - 4095) * -1
    p.setPWM(redPin, 0, dc)
    redPin += 1

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
pwm2.setPWMFreq(60)

while (True):
    
  cmd = raw_input('Enter a comma separated RGB value: ').split(',')

  for i in range(0,14,3): 
    setColor(i, cmd, pwm)

  setColor(0,cmd, pwm2)
  setColor(3, cmd, pwm2)

