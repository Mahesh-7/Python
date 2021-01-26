from picamera import PiCamera
from time import sleep

camera = PiCamera()
######for capture########
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/images2.jpg')
camera.stop_preview()
##########capture##########

######for video record###############

camera.start_recording('/home/pi/Desktop/video.h264')
sleep(5)
camera.stop_recording()
