#!/usr/bin/env python

import os
import spidev
from datetime import datetime
from Adafruit_CharLCD_MCP import Adafruit_CharLCD
from time import sleep, strftime

spi = spidev.SpiDev()
spi.open(0,0)

lcd = Adafruit_CharLCD()
lcd.begin(16,1)

bit_depth = 10.0
max_value = (2.0**bit_depth) - 1

temperature_sensor = 0
light_sensor = 1

def readadc(adcnum):
	if((adcnum > 7) or (adcnum <0)):
		return -1
	r = spi.xfer2([1,(8+adcnum)<<4,0])
	adcout = ((r[1]&3) << 8) + r[2]
	return adcout

log = open('sensor_log', 'w+')

while True:
	lcd.clear()	
	input = readadc(temperature_sensor)
	print "input: " + `input`
	print "max input: " + `max_value`
	mvolts = input * (3300.0 / max_value)
	print "millivolts: " + `mvolts`
	temperature = (mvolts - 500) / 10.0  
	print temperature

	photocell = readadc(light_sensor)
	
	if photocell < 10:
		photo_str = 'Dark\n'
	elif photocell < 200:
		photo_str = 'Dim\n'	
	elif photocell < 500:
		photo_str = 'Light\n'
	elif photocell < 800:
		photo_str = 'Bright\n'
	else:
		photo_str = 'Shiny\n'

	temp_str = "Temp: " + str(round(temperature,1)) + " C"
	lcd.message(datetime.now().strftime('%H:%M  '))
	lcd.message(photo_str)
	lcd.message(temp_str)
	log.write(str(temperature))
	log.write(',')
	log.write(str(photocell))
	log.write(',')
	log.write(datetime.now().strftime('%b %d %H:%M:%S'))
	log.write('\n')
	log.flush()
	sleep(5)

