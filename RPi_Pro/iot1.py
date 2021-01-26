import RPi.GPIO as GPIO
import time
import urllib3


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)


def read_data_base(Component_ID):
    url = "http://azetech.in/office/scripts/IoT.php?api=ReadValue&ID="
    url += Component_ID
    http = urllib3.connection_from_url(url)
    r = http.urlopen('GET',url)
    data = r.data.decode("utf-8-sig").encode("utf-8")
    return data


def Write_Database(Component_ID,data):
    url = "http://azetech.in/office/scripts/IoT.php?api=UpdateValue&ID=" + Component_ID + "&value="
    http_pool = urllib3.connection_from_url(url)
    r = http_pool.urlopen('SET',url+str(data))

#Write_Database(write_link,50)


try:
    while 1:
       GPIO.output(29,ord(read_data_base("IOTCMP00126"))-48)
       GPIO.output(31,ord(read_data_base("IOTCMP00127"))-48)
       GPIO.output(33,ord(read_data_base("IOTCMP00128"))-48)

except Exception:
    print("Program Terminated!")
   



