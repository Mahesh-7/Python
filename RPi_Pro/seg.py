import RPi.GPIO as GPIO
import time

class Segment:
    Digits = (0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f)
    Segment_Pin = tuple()

    @staticmethod
    def Init(pins):
        Segment.Segment_Pin = pins
	for i in Segment.Segment_Pin:
	    GPIO.setup(i,GPIO.OUT)

    @staticmethod
    def Display(value):
	if (value>9):
	    return
	for i in range(0,7):
	    GPIO.output(Segment.Segment_Pin[i],((Segment.Digits[value]>>i)&1))


GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

Segment.Init((7,11,13,15,29,31,33))

for i in range(0,10):
	Segment.Display(i)
	time.sleep(1)
