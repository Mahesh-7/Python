import RPi.GPIO as gpio
import time

data_line = [7,13,15,29,31,33,37,32]
com_line  = [12,16,18]


gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)


def char_to_bit(byte_1):
    byte = ord(byte_1)    #convert char to interger  
    bit_list = []         #empty list for holding bit pattern
    item = 0              #to hold a bit during seperation
    
    for i in range(0,8):        #to shift byte 8 times even if the value reached zero, to obtain complete bit pattern 
        item = 1 & byte
        bit_list.append(item)
        byte >>= 1

    return bit_list


def byte_to_bit(byte): 
    bit_list = []         #empty list for holding bit pattern
    item = 0              #to hold a bit during seperation
    
    for i in range(0,8):        #to shift byte 8 times even if the value reached zero, to obtain complete bit pattern 
        item = 1 & byte
        bit_list.append(item)
        byte >>= 1

    return bit_list


def lcd_command(command):
    bit = []
    gpio.output(18,True)
    gpio.output(12,False)
    gpio.output(16,False)

    bit = byte_to_bit(command)

    for i in range(0,8):
        gpio.output(data_line[i],bit[i])
        #print("data_line=",data_line[i],"bit = ",bit[i])   #print

    time.sleep(0.1)
    gpio.output(18,False)

def display_char(data):
    bit = []
    gpio.output(18,True)
    gpio.output(12,True)
    gpio.output(16,False)

    bit = char_to_bit(data)

    for i in range(0,8):
        gpio.output(data_line[i],bit[i])
        #print("data_line=",data_line[i],"bit = ",bit[i])   

    time.sleep(0.1)
    gpio.output(18,False)


def lcd_init():
    #print("Pin State")
    for i in data_line:
        gpio.setup(i,gpio.OUT)
        #print("pin",i,"state",gpio.OUT)                    
    for i in com_line:
        gpio.setup(i,gpio.OUT)
        #print("pin",i,"state",gpio.OUT)                    
 
    #print("For Command")
    lcd_command(0x01)
    time.sleep(0.1)
    
    lcd_command(0x0C)
    time.sleep(0.1)
    
    lcd_command(0x06)
    time.sleep(0.1)
    
    lcd_command(0x38)
    time.sleep(0.1)
    
    lcd_command(0x80)
    time.sleep(0.1)



def display_str(data):
    for i in range(0,len(data)):
        display_char(data[i])


lcd_init()

while True:
	display_char('A')
	print("Cleared")
	time.sleep(3)



