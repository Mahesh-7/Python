import time
import serial

gps = serial.Serial("/dev/ttyS0",9600)
gps.timeout = 0.05


def split_string(location):
    check = '$'
    data_s = location.split(check)
    #print(data_s)
    for i in range(0,len(data_s)):
        if "GPGLL" in data_s[i]:
            #print(data_s[i])
            data = data_s[i].split(",")
            #print(data)
            return data
        

def get_location():
    ch = gps.inWaiting()
    location = gps.read(ch)
    #print(location)
    location = split_string(location)
    return location                    #  (example) ['GPGLL', '1102.1694', 'N', '07658.6619', 'E', '105119.000', 'A', 'A*58\r\n']     
    
    
while True:  
    
    location = get_location()  
    print(location)
    time.sleep(1)




