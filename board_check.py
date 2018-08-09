# -*- coding: utf-8 -*-
#
# 2018/07/31 rev 1.0 Modified for 4ch In/Out
#
 
import time
import RPi.GPIO as GPIO
import shlex
import subprocess

# GPIO pin number
GP_OUT1 = 4
GP_OUT2 = 17
GP_OUT3 = 27
GP_OUT4 = 22
GP_IN1 = 18
GP_IN2 = 23
GP_IN3 = 24
GP_IN4 = 25

gpio_in = (GP_IN1, GP_IN2, GP_IN3, GP_IN4)
gpio_out = (GP_OUT1, GP_OUT2, GP_OUT3, GP_OUT4)

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
  # Input
  GPIO.setup(GP_IN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(GP_IN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(GP_IN3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(GP_IN4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

init_gpio()
gp_out1_state = False
gp_out2_state = False
gp_out3_state = False
gp_out4_state = False


def worker_check_button_1(event):
  print("gp_out1")
  global gp_out1_state 
  gp_out1_state = not(gp_out1_state)
  GPIO.output(GP_OUT1, gp_out1_state)

def worker_check_button_2(event):
  print("gp_out2")
  global gp_out2_state 
  gp_out2_state = not(gp_out2_state)
  GPIO.output(GP_OUT2, gp_out2_state)

def worker_check_button_3(event):
  print("gp_out3")
  global gp_out3_state 
  gp_out3_state = not(gp_out3_state)
  GPIO.output(GP_OUT3, gp_out3_state)

def worker_check_button_4(event):
  print("gp_out4")
  global gp_out4_state 
  gp_out4_state = not(gp_out4_state)
  GPIO.output(GP_OUT4, gp_out4_state)

GPIO.add_event_detect(GP_IN1,
                      GPIO.FALLING,
                      callback=worker_check_button_1,
                      bouncetime=300)
GPIO.add_event_detect(GP_IN2,
                      GPIO.FALLING,
                      callback=worker_check_button_2,
                      bouncetime=300)
GPIO.add_event_detect(GP_IN3,
                      GPIO.FALLING,
                      callback=worker_check_button_3,
                      bouncetime=300)
GPIO.add_event_detect(GP_IN4,
                      GPIO.FALLING,
                      callback=worker_check_button_4,
                      bouncetime=300)
 
    
try:
  while True:
    time.sleep(1.0)
except:
  print("Quit")
finally:
  print("Clean up")
  GPIO.cleanup()

print("Done")
