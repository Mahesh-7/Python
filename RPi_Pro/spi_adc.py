import spidev
import time

spi=spidev.SpiDev()
spi.open(0,0) 

def read_data(channel):
  spi.max_speed_hz=1350000
  if channel>7 or channel <0:
    return
  r=spi.xfer2([1,8+channel<<4,0])
  data=((r[1]&3)<<8)+r[2]
#  print(data)
  return data

def temp(channel):
  temp=read_data(0)
  temp=(temp/204.6)*100
 # print(temp)
  return temp

while 1:
  value=temp(0)
  value=str(value)
  print(value[:5]+'c')
#  print(type(value))
  time.sleep(1)
