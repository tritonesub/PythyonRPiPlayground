#!/usr/bin/env python

import os
import spidev
from datetime import datetime
from time import sleep, strftime
from array import array
from Adafruit_PWM_Servo_Driver import PWM
import math

spi = spidev.SpiDev()
spi.open(0,0)

bit_depth = 10.0
max_value = (2.0**bit_depth) - 1

pwm = PWM()

proximity = 7

def setColor(redPin, rgb):
  #convert from 255 to 12bit
  for c in rgb:
    dc =  int(((c / float(255)) * float(4095)) - 4095) * -1
    pwm.setPWM(redPin, 0, dc)
    redPin += 1

def smoothTo(redPin,newRGB, oldRGB):
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
      for x in redPin:
        setColor(x, oldRGB)
#      sleep(0.001)

def readadc(pin):
  if((pin > 7) or (pin < 0)):
    return -1
  r = spi.xfer2([1,(8+pin)<<4,0])
  adcout = ((r[1]&3) << 8) + r[2]
  return adcout

def toMV(value):
  mv = value * (3300.0 / max_value)
  return mv

def convertTo(value, maxRange):
  color = int((value - 3000)/(400-3000)*(maxRange) + 0)
  if color > maxRange:
    color = maxRange 
  elif color < 0:
    color = 0
#  print "value: " + `value`
#  print "color: " + `color`
  return color

pwm.setPWMFreq(100)
rgb = array('l',[255,255,255])
old_rgb = array('l',[255,255,255])
index = 0

while True:
  prox_in = readadc(proximity)
  proxMV = toMV(prox_in)
  rgb[index] = convertTo(proxMV,255)

#  smoothTo([10,13], rgb, old_rgb)

  setColor(10, rgb)
  setColor(13, rgb)

  for i in range(3):
    old_rgb[i] = rgb[i]
  
  sleep(1)
  
  if index == 2:
    index = 0
  else:
    index += 1
