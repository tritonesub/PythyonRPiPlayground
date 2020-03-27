#!/usr/bin/env python

from Adafruit_MCP230xx import Adafruit_MCP230XX

import time
import RPi.GPIO as gpio

mcp = Adafruit_MCP230XX(busnum = 1, address = 0x20, num_gpios = 16)

#setup port assignments

#setup gpio
gpio.setmode(io.BCM)

#setup mcp

while True:

	sleep(1)
