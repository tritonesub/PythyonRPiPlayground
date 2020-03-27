#!/usr/bin/env python

import sys
sys.path.append("home/pi/libraries/Adafruit-Raspberry-Pi-Python-Code/Adafruit_MCP230xx")
from Adafruit_MCP230xx import Adafruit_MCP230XX

import time

mcp = Adafruit_MCP230XX(busnum = 1, address = 0x21, num_gpios = 16)

RED = 8 
GREEN = 7 
IN = 10

COMMANDS = ["red","green","both","flash","blink","exit"]

mcp.config(GREEN, mcp.OUTPUT)
mcp.config(RED, mcp.OUTPUT)
mcp.config(IN, mcp.INPUT)
mcp.pullup(IN, 1)

def parseLights(cmd):
	if cmd == "red":
		mcp.output(RED, 1)
	elif cmd == "green":
		mcp.output(GREEN, 1)
	elif cmd == "both":
		mcp.output(GREEN, 1)
		mcp.output(RED, 1)
	else: 
		return False
	return True

def turnOffLights():
	mcp.output(GREEN, 0)
	mcp.output(RED, 0)

def parseCommand(cmd):
	result = False
	if cmd == "flash" or cmd == "blink":
		for i in range(10):
			turnOffLights()
			if cmd == "flash":	
				result = parseLights(COMMANDS[i%2])
			else: 
				result = parseLights(COMMANDS[2])
				time.sleep(0.5)
				turnOffLights()

			time.sleep(0.5)

		turnOffLights()
	else:
		result = parseLights(cmd)
		time.sleep(0.5)

	return(result)

def processButton():
	index = 0
	while index < len(COMMANDS):
		if (mcp.input(IN)) == 0:
			turnOffLights()
			parseCommand(COMMANDS[index])
			index+=1
		time.sleep(0.2)
		if index == len(COMMANDS) - 1:
			return()

GO = True

while GO:
	cmd=raw_input('Pick a color: ')
	cmd = cmd.lower()
	turnOffLights()
	
	if cmd == "button":
		processButton()
	else:
		GO = parseCommand(cmd)
	
