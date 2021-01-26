
import RPi.GPIO as GPIO
import time



def stepper_init(stepper_pin):

    for i in stepper_pin:
        GPIO.setup(stepper_pin,GPIO.OUT)
        


def rotate_forward(stepper_rotation,speed = 1):

    rotation = int(stepper_rotation * 12)
    print(rotation*4," steps ,",stepper_rotation,"rotation")
    i = 0
    while i<rotation:
        GPIO.output(29,True)
        GPIO.output(31,False)
        GPIO.output(33,False)
        GPIO.output(37,False)

        time.sleep(speed)

        GPIO.output(29,False)
        GPIO.output(31,False)
        GPIO.output(33,True)
        GPIO.output(37,False)

        time.sleep(speed)


        GPIO.output(29,False)
        GPIO.output(31,False)
        GPIO.output(33,False)
        GPIO.output(37,True)
        
        time.sleep(speed)

        GPIO.output(29,False)
        GPIO.output(31,True)
        GPIO.output(33,False)
        GPIO.output(37,False)

        time.sleep(speed)

        i = i+1
def rotate_reverse(stepper_rotation,speed = 1):

    rotation = int(stepper_rotation * 12)
    print(rotation*4," steps ,",stepper_rotation,"rotation")
    i = 0
    while i<rotation:

        GPIO.output(29,False)
        GPIO.output(31,True)
        GPIO.output(33,False)
        GPIO.output(37,False)

        time.sleep(speed)

        GPIO.output(29,False)
        GPIO.output(31,False)
        GPIO.output(33,False)
        GPIO.output(37,True)

        time.sleep(speed)

        GPIO.output(29,False)
        GPIO.output(31,False)
        GPIO.output(33,True)
        GPIO.output(37,False)

        time.sleep(speed)
        
        GPIO.output(29,True)
        GPIO.output(31,False)
        GPIO.output(33,False)
        GPIO.output(37,False)

        time.sleep(speed)

        i = i+1

