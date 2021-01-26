import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(12,GPIO.OUT)

while True:
	GPIO.output(12,GPIO.HIGH)
	print("Led on")
	time.sleep(1)
	GPIO.output(12,GPIO.LOW)
	print "Led off"
	time.sleep(1)
