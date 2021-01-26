import RPi.GPIO as GPIO
import time

DT = 27
SCK=22


def read_weight():
  sample = 8410856
  i=0
  Count=0
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(DT, GPIO.OUT)
  GPIO.output(DT,1)
  GPIO.setup(SCK,GPIO.OUT)
  GPIO.output(SCK,0)
  GPIO.setup(DT, GPIO.IN)

  while GPIO.input(DT) == 1:
      print("in  polling")
      i=0
  for i in range(24):
        GPIO.output(SCK,1)
        Count=Count<<1

        GPIO.output(SCK,0)
        time.sleep(0.001)
        if GPIO.input(DT) == 0: 
            Count=Count+1
        
  GPIO.output(SCK,1)
  Count=Count^0x800000
  GPIO.output(SCK,0)
  w = (Count - sample )/30
  if w<0:return 0
  return w 

while True:
  weight = read_weight()
  print("Weight = ",weight)
  time.sleep(1)


