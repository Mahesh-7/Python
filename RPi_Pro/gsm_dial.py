import serial
import time,sys

SERIAL_PORT="/dev/ttyS0"
ser=serial.Serial(SERIAL_PORT,baudrate=9600,timeout=5)

ser.write("ATD9789299309\r")
print('DIALING..')

time.sleep(10)


#while True:
 #   if (int(input('Press 1 to dis '))==1):
ser.write('ATH\r')
print('hanging')        
#	break


