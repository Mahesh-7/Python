import RPi.GPIO as GPIO

import urllib3



def read_data_base(url):

    http = urllib3.connection_from_url(url)

    r = http.urlopen('GET',url)

    data = r.data.decode("utf-8-sig").encode("utf-8")

    print(data)

    return data

GPIO.setmode(GPIO.BOARD)

GPIO.setup(10,GPIO.OUT)

GPIO.output(10,False)


url = "http://www.azetech.in/office/scripts/IoT.php?api=ReadValue&ID=IOTCMP00031"


while True:

    value = read_data_base(url)

    print(value)

    if value == b'1':

        GPIO.output(10,True)
        print("LED ON")


    else:

        GPIO.output(10,False)
        print("LED OFF")










