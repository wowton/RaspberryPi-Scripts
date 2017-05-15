# Author: Kieran
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
GPIO.setup(16, GPIO.OUT)
 
try:
  while True:
    if GPIO.input(12) == 1:
      print "Some people here!"
      GPIO.output(16, GPIO.HIGH)
    else:
      print "Nobody!"
      GPIO.output(16, GPIO.LOW)
    time.sleep(.1)
except KeyboardInterrupt:
  GPIO.cleanup()
  print "All Cleanup!"
