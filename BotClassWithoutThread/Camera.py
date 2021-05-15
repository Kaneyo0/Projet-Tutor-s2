from picamera import PiCamera
from time import sleep
from discord.ext import commands
import discord

Image = "image.jpeg"

class Camera():
    def __init__(self):
        super(Camera, self).__init__(camera=PiCamera())
        self.camera = PiCamera()

    def prendrePhoto(self, PiCamera):
        try:
            camera = PiCamera()
            camera.resolution = (500, 500)
            camera.rotation = 180
            sleep(5)
            camera.capture(Image)
            camera.close()
        except:
            camera.close()
            #print("Erreur : La camera n'est pas branchée")
            
    def fermerCamera(self):
        camera.close()