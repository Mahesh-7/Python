import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
l=(29,31,33,35,37)
for i in l:
  GPIO.setup(i,GPIO.OUT)
while 1:
 for i in range(5):
  GPIO.output(l[i],True)
  print('led  on',i+1)
  time.sleep(1)
  
