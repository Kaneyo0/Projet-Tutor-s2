from picamera import PiCamera
from time import sleep

Photo = "media/image.jpeg"

class Camera():
    def __init__(self):
        super(Camera, self).__init__(camera=PiCamera())
        self.camera = PiCamera()

    def prendrePhoto(self, PiCamera):
        camera = PiCamera()
        camera.resolution = (1920, 1080)
        camera.rotation = 180
        sleep(5)
        camera.capture(Photo)
        camera.close()