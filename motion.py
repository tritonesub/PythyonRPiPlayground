#!/usr/bin/env python
from Adafruit_MCP230xx import Adafruit_MCP230XX
import time
import RPi.GPIO as io

mcp = Adafruit_MCP230XX(busnum = 1, address = 0x20, num_gpios = 16)

RELAY = 24 
GREEN_LED = 15
RED_LED = 14
PIR = 23

io.setmode(io.BCM)
io.setup(PIR, io.IN)
#io.setup(RELAY,io.OUT)

mcp.config(GREEN_LED, mcp.OUTPUT)
mcp.config(RED_LED, mcp.OUTPUT)

while True:
	if io.input(PIR):
#		print "moving"
#		io.output(RELAY,1)
		mcp.output(GREEN_LED,1)

	else:
#		print "not"
#		io.output(RELAY,0)
		mcp.output(GREEN_LED,0)
	time.sleep(1)
