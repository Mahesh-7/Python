import serial
import time,sys

SERIAL_PORT="/dev/ttyS0"
ser=serial.Serial(SERIAL_PORT,baudrate=9600,timeout=5)

ser.write("AT+CMGF=1\r")
print('text mode enable')
time.sleep(3)

ser.write('AT+CMGS="9789299309"\r')
msg="welcome to embedded world"
print('sending msg')

ser.write(msg+chr(26))
time.sleep(3)
print('msg sent') 


