#!/usr/bin/python

from Adafruit_CharLCD_MCP import Adafruit_CharLCD
from subprocess import * 
from time import sleep, strftime
from datetime import datetime

lcd = Adafruit_CharLCD()

cmd = "ip addr show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f1"

#lcd.begin(16,1)


while 1:
	msg = raw_input("Enter a message: ")
	lcd.clear()
	words = msg.split('|')
	lcd.message(words[0]+'\n')
	lcd.message(words[1])
	sleep(10)
