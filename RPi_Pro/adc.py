

import spidev
import time


#Define Variables
delay = 0.5


#Create SPI
spi = spidev.SpiDev()
spi.open(0, 0)

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

while True:
	print(get_temperature(0))
	time.sleep(3)

