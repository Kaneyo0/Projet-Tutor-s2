from picamera import PiCamera
from time import sleep
from discord.ext import commands
import discord

Image = "image.jpeg"

class Camera(PiCamera):
    def __init__(self):
        super(Camera, self).__init__(camera=PiCamera())
        self.camera = PiCamera()

    def prendrePhoto(self, PiCamera):
        try:
            camera = PiCamera()
            camera.resolution = (500, 500)
            camera.rotation = 180
            camera.start_preview(fullscreen=False, window=(1920, 1080, 640, 480))
            sleep(5)
            camera.capture(Image)
            camera.stop_preview()
            camera.close()
        except:
            print("Erreur : La camera n'est pas branchée")