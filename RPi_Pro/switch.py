import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

switch_in  = [12,16,18]
switch_out = [7,13,15,29,31]


def switch_init(switch_in,switch_out):
    
    print("Output pins")
    for i in switch_out:
        GPIO.setup(i,GPIO.OUT)
        print(i)
        
    print("Input pins")
    for j in switch_in:
        GPIO.setup(j,GPIO.IN)
        print(j)

def pin_state(pin_high):
    for i in switch_out:
        if i == pin_high:   
            GPIO.setup(i,GPIO.HIGH)
            #print("pin = ",i,",state = ",GPIO.LOW)
        else:
            GPIO.setup(i,GPIO.LOW)
            #print("pin = ",i,",state = ",GPIO.HIGH)

def which_char(character):
    count = 0
    for i in switch_in:
        #print(i)
        if GPIO.input(i):
            print(character[count])
            time.sleep(.5)
        count = count+1


def switch_output():
    GPIO.output(7,GPIO.HIGH)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(15,GPIO.LOW)
    GPIO.output(29,GPIO.LOW)
    GPIO.output(31,GPIO.LOW)
    which_char(['a','f','k'])

    GPIO.output(7,GPIO.LOW)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(15,GPIO.LOW)
    GPIO.output(29,GPIO.LOW)
    GPIO.output(31,GPIO.LOW)
    which_char(['b','g','l'])

    GPIO.output(7,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(15,GPIO.HIGH)
    GPIO.output(29,GPIO.LOW)
    GPIO.output(31,GPIO.LOW)
    which_char(['c','m','h'])

    GPIO.output(7,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(15,GPIO.LOW)
    GPIO.output(29,GPIO.HIGH)
    GPIO.output(31,GPIO.LOW)
    which_char(['d','i','n'])

    GPIO.output(7,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(15,GPIO.LOW)
    GPIO.output(29,GPIO.LOW)
    GPIO.output(31,GPIO.HIGH)
    which_char(['e','j','o'])
    
switch_init(switch_in,switch_out)


while True:
    switch_output()
    #time.sleep(1)


    
    
