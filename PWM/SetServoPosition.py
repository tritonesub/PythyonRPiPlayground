#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM 
import time

pwm = PWM(0x40, debug=True)

cycle = 50 
pwm.setPWMFreq(cycle)

pulseLength = 1000000 / cycle
tick = pulseLength / 4096 #12 bit

while(True):
   value = raw_input('Enter the micro second position: ')
   
   pwm.setPWM(0,0,int(value)/tick)
   time.sleep(1)
