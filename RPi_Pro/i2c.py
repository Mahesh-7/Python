import smbus
import time
bus=smbus.SMBus(1)
#bus.write_byte_data(0xc0,0x60,0x00)
#bus.write_byte_data(0xc0,0x60,0x01)
bus.write_byte_data(0xc0,0x60,0xff)
#datas=[0xff,0xf0]
#bus.write_i2c_block_data(0xc0,0x60,datas)
time.sleep(1)
while 1:
  data=bus.read_byte_data(0xc0,0x60,2)
  analog=((data[2])<<8)+(data[3])
  print(analog)
