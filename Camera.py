from picamera import PiCamera
from time import sleep

try :
    camera = PiCamera()
    camera.resolution = (1920,1080)
    camera.rotation = 180 
    camera.start_preview(fullscreen = False, window = (50,50,640,480))
    sleep(5)
    camera.capture('/home/pi/Pictures/image.jpeg')
    camera.stop_preview()
    camera.close()
except :
    print('La camera n est pas branchee')
