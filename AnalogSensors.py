#!/usr/bin/env python

import os
import spidev
from datetime import datetime
from time import sleep, strftime

spi = spidev.SpiDev()
spi.open(0,0)

bit_depth = 10.0
max_value = (2.0**bit_depth) - 1

proximity = 7
lm35 = 2
tmp36 = 1
photo = 0

def readadc(pin):
  if((pin > 7) or (pin < 0)):
    return -1
  r = spi.xfer([1, (8 + pin) << 4, 0])
  adcout = ((r[1] & 3) << 8) + r[2]
  return adcout

def toMV(value):
  mv = (value * 3300.0) / max_value 
  return mv

def convert_lm35(value):
  print "lm35 value: " + `value`
  mv = toMV(value)
  print "lm35 mv: " + `mv`
  celcius = mv/10.0 
  print "lm35 celcius: " + `celcius`
  return celcius 

def convert_tmp36(value):
  print "tmp36 value: " + `value`
  mv = toMV(value)
  print "tmp36: " + `mv`
  celcius = (mv / 10) - 50 
  print "tmp36 celcius: " + `celcius`

def convert_photo(value):
  mv = toMV(value)
  print "photo: " + `mv`
  
  if value < 10:
    photo_str = 'Dark\n'
  elif value < 200:
    photo_str = 'Dim\n'
  elif value < 500:
    photo_str = 'Light\n'
  elif value < 800:
    photo_str = 'Bright\n'
  else:
    photo_str = 'Shiny\n' 

  print "it is: " + `photo_str`

def convert_prox(value):
  mv = toMV(value)
  print "prox: " + `mv`

while True:
  lm35_in = readadc(lm35)
  lm35_in = readadc(lm35)
  tmp36_in = readadc(tmp36)
  photo_in = readadc(photo)
  prox_in = readadc(proximity)

  convert_lm35(lm35_in)
  convert_tmp36(tmp36_in)
  convert_photo(photo_in)
  convert_prox(prox_in)

  sleep(1)
