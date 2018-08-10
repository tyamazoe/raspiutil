# -*- coding: utf-8 -*-
 
import time
import RPi.GPIO as GPIO

# GPIO pin number
GP_OUT1 = 4
GP_OUT2 = 17
GP_OUT3 = 27
GP_OUT4 = 22

def init_gpio():
  print("Initialize GPIO\n")
  # Use GPIO pin num
  GPIO.setmode(GPIO.BCM)
  # Output
  GPIO.setup(GP_OUT1, GPIO.OUT)
  GPIO.output(GP_OUT1, False)
  GPIO.setup(GP_OUT2, GPIO.OUT)
  GPIO.output(GP_OUT2, False)
  GPIO.setup(GP_OUT3, GPIO.OUT)
  GPIO.output(GP_OUT3, False)
  GPIO.setup(GP_OUT4, GPIO.OUT)
  GPIO.output(GP_OUT4, False)

def counter():
  for num in range(16):
    #print(num)
    led_on(num)
    time.sleep(0.4)

def led_on(num):
  binstr = format(num, '04b')
  GPIO.output(GP_OUT4, int(binstr[0]))
  GPIO.output(GP_OUT3, int(binstr[1]))
  GPIO.output(GP_OUT2, int(binstr[2]))
  GPIO.output(GP_OUT1, int(binstr[3]))
  #print("{0} {1} {2} {3}".format(binstr[0], binstr[1], binstr[2], binstr[3]))


init_gpio()
try:
  print("Start binary counter ....")
  while True:
    counter()
    time.sleep(2.0)
except:
  print("Quit")
finally:
  print("Clean up")
  GPIO.cleanup()

print("Done")
