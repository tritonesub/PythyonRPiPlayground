#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM 
import time

pwm = PWM(0x41, debug=True)

cycle = 60 
pwm.setPWMFreq(cycle)
length = 1000000/cycle
tick = length/4096

while(True):
   value = raw_input('Enter pan,tilt: ')
   
   value = value.split(':')

   for v in value:
      pair = v.split(',') 
      pwm.setPWM(10,0,int(pair[0])/tick)
      pwm.setPWM(9,0,int(pair[1])/tick)
      time.sleep(1)
