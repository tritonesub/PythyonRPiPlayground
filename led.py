#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

RED = 24
GREEN = 25
IN = 23

COMMANDS = ["red","green","both","flash","blink","exit"]

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(IN, GPIO.IN)

def parseLights(cmd):
	if cmd == "red":
		GPIO.output(RED, True)
	elif cmd == "green":
		GPIO.output(GREEN, True)
	elif cmd == "both":
		GPIO.output(GREEN, True)
		GPIO.output(RED, True)
	else: 
		return False
	return True

def turnOffLights():
	GPIO.output(GREEN, False)
	GPIO.output(RED, False)

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
		if GPIO.input(IN) == False:
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
	
