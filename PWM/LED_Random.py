#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
from array import array
import time
import random
import math

# ===========================================================================
# Example Code
# ===========================================================================

pwm = PWM()

def setColor(redPin, rgb):
  #convert from 255 to 12bit 
  for c in rgb:
    dc =  int(((c / float(255)) * float(4095)) - 4095) * -1
    pwm.setPWM(redPin, 0, dc)
    redPin += 1

def smoothTo(newRGB, oldRGB):
    rgb = array('l',[0,0,0])
    
    for i in range(3):
      rgb[i] = oldRGB[i] - newRGB[i] 
    
    while (rgb[0] != 0 or rgb[1] != 0 or rgb[2] != 0):
      for i in range(3):
        if(rgb[i] > 0):
          oldRGB[i] -= 1
          rgb[i] = oldRGB[i] - newRGB[i]
        elif(rgb[i] < 0):
          oldRGB[i] += 1
          rgb[i] = oldRGB[i] - newRGB[i]
      
        setColor(13, oldRGB)
      time.sleep(0.005)

pwm.setPWMFreq(100)                        # Set frequency to 60 Hz
rgb1 = array('l',[0,0,0])
old_rgb1 = array('l',[0,0,0])

while (True):
    rgb1[0] = int(random.random() * 1000) % 256
    rgb1[1]= int(random.random() * 1000) % 256
    rgb1[2]= int(random.random() * 1000) % 256
   
    smoothTo(rgb1,old_rgb1)
#    setColor(7,rgb1)
#    setColor(10,rgb1)
#    setColor(13,rgb1)
    
    old_rgb1[0] = rgb1[0]
    old_rgb1[1] = rgb1[1]
    old_rgb1[2] = rgb1[2]

    time.sleep(0.5)
