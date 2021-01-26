
import RPi.GPIO as GPIO
import time
import urllib3
import spidev


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)


spi=spidev.SpiDev()
spi.open(0,0) 

def read_data(channel):
  spi.max_speed_hz=1350000
  if channel>7 or channel <0:
    return
  r=spi.xfer2([1,8+channel<<4,0])
  data=((r[1]&3)<<8)+r[2]
  return data

def temp(channel):
  temp=read_data(0)
  temp=(temp/204.6)*100
  return temp


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
    r = http_pool.urlopen('SET',url+(data))


try:
    while 1:
       GPIO.output(29,ord(read_data_base("IOTCMP00126"))-48)
       GPIO.output(31,ord(read_data_base("IOTCMP00127"))-48)
       GPIO.output(33,ord(read_data_base("IOTCMP00128"))-48)
       value=temp(0)
       value=str(value)
       Write_Database(write_link,value[:5]+'c',)
       time.sleep(1)

except Exception:
    print("Program Terminated!")
