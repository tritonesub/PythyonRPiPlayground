#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

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

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
while (True):
  setColor(13,[255,255,255])
  setColor(10,[255,255,255])
  time.sleep(1)

  waitTime = 0.005

  for i in range(255,0,-1):
    setColor(13,[i,i,i])
    setColor(10,[i,i,i])
    time.sleep(waitTime)
 
  for red in range(256):
	#	print red
	setColor(13,[red,0,0])
	setColor(10,[red,0,0])
	time.sleep(waitTime)

  for green in range(256):
    setColor(13,[255,green,0])
    setColor(10,[255,green,0])
    time.sleep(waitTime)

  for red in range(255,0,-1):
    setColor(13,[red,255,0])
    setColor(10,[red,255,0])
    time.sleep(waitTime)

  for blue in range(256):
    setColor(13,[0,255,blue])
    setColor(10,[0,255,blue])
    time.sleep(waitTime)

  for green in range(255,0,-1):
    setColor(13,[0,green,255])
    setColor(10,[0,green,255])
    time.sleep(waitTime)
  
  for red in range(256):
	#	print red
	setColor(13,[red,0,255])
	setColor(10,[red,0,255])
	time.sleep(waitTime)
  
  for green in range(256):
    setColor(13,[255,green,255])
    setColor(10,[255,green,255])
    time.sleep(waitTime)
  
  for i in range(255,0,-1):
    setColor(13,[i,i,i])
    setColor(10,[i,i,i])
    time.sleep(waitTime)

  for i in range(256):
    setColor(13,[i,i,i])
    setColor(10,[i,i,i])
    time.sleep(waitTime)
