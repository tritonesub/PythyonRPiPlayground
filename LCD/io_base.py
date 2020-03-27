#!/usr/bin/env python

import threading
import RPi.GPIO as gpio

class MotionDetector(threading.Thread):
	def __init__(self,io,pin):
		self.io = io
		self.pin = pin
