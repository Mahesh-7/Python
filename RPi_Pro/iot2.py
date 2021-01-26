import spidev
import RPi.GPIO as GPIO
import urllib3
import time

spi = spidev.SpiDev()
spi.open(0, 0)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.IN)

Read_Link1 = "http://azetech.in/office/scripts/IoT.php?api=ReadValue&ID=IOTCMP00126"
Read_Link2 = "http://azetech.in/office/scripts/IoT.php?api=ReadValue&ID=IOTCMP00127"
Read_Link3 = "http://azetech.in/office/scripts/IoT.php?api=ReadValue&ID=IOTCMP00128"
Write_Link = "http://azetech.in/office/scripts/IoT.php?api=UpdateValue&ID=IOTCMP00129&value="

def Read_Database(url):
    http_pool = urllib3.connection_from_url(url)
    r = http_pool.urlopen('GET', url)
    data = r.data.decode("utf-8-sig")
    # print(data)
    return data

def Write_Database(url, data):
    http_pool = urllib3.connection_from_url(url)
    r = http_pool.urlopen('SET', url + str(data))

def readadc(adcnum):
        # read SPI data from the MCP3008, 8 channels in total
        if adcnum > 7 or adcnum < 0:
            return -1
        r = spi.xfer2([1, 8 + adcnum << 4, 0])
        data = ((r[1] & 3) << 8) + r[2]
        return data

def get_temperature(adc_channel):
        temp = readadc(adc_channel)
        temp /= 204.559
        temp *= 100
        return temp

#Read_Database(Read_Link1)


while 1:
    GPIO.output(29, Read_Database(Read_Link1))
    time.sleep(1)

    GPIO.output(31, Read_Database(Read_Link2))
    time.sleep(1)

    GPIO.output(33, Read_Database(Read_Link3))
    time.sleep(1)

    GPIO.output(35, 1)

    Write_Database(Write_Link, get_temperature(0))
    print(get_temperature(0))
    time.sleep(1)





