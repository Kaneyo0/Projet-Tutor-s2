from time import sleep
from dotenv import load_dotenv
from PIL import Image
from Alarme import *
from Camera import *
import random
import nasapy
import os
import urllib.request
import RPi.GPIO as GPIO
import discord
import sys
from discord.ext import commands

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

BestFish = "media/poisson.jpg"
Photo = "media/image.jpeg"
ImgNasa = "media/imgNasa.png"
PoissonCoupe = "media/poissoncoupe.png"
ImgSuperposes = "imgSuperposes.png"
load_dotenv(dotenv_path="config")
key = os.environ.get(os.getenv("NASATOKEN"))
nasa = nasapy.Nasa(key=key)

class Bot(commands.Bot, discord.Client):

    def __init__(self):
        super(Bot, self).__init__(command_prefix="!")
        self.add_command(commands.Command(self.bestFish, name="bestFish"))
        self.add_command(commands.Command(self.fish, name="fish"))
        self.add_command(commands.Command(self.nasa, name="nasa"))
        self.add_command(commands.Command(self.spaceFish, name="spaceFish"))

    async def on_ready(self):
        print(f"{self.user.display_name} est connecté")

    async def bestFish(self, msg):
        try:
            file = discord.File(BestFish, filename=BestFish)
            await msg.channel.send("Neuneuil : ", file=file)
        except:
            await msg.channel.send("Erreur : Neuneuil est introuvable !")

    async def fish(self, msg):
        try:
            Camera.prendrePhoto(self, PiCamera)
            file = discord.File(Photo, filename=Photo)
            await msg.channel.send("Image de la rasberry : ", file=file)
            os.remove(Photo)
        except:
            await msg.channel.send("Erreur : La camera n'est pas branchée")
            
            try:
                file = discord.File(BestFish, filename=BestFish)
                await msg.channel.send("Voici votre image préféré de Neuneuil par défaut : ", file=file)
            except:
                await msg.channel.send("Erreur : la photo n'a pas pu être envoyée.")
            
            try:
                Alarme.activationAlarme(self, msg)
            except:
                await msg.channel.send("Erreur : le buzzer n'est pas branché.")
                
            try:
                Alarme.activationLed(self, msg)
            except:
                await msg.channel.send("Erreur : la led n'est pas branchée.")
                
    async def nasa(self, msg):
        try:
            await msg.channel.send(nasa.picture_of_the_day()["hdurl"])
        except:
            await msg.channel.send("Une erreur est survenue")
                
    async def spaceFish(self, msg):
        try:
            urllib.request.urlretrieve(nasa.picture_of_the_day()["url"], ImgNasa)
            background = Image.open(ImgNasa)
            img = Image.open(PoissonCoupe)
            
            diviseurLongueur = random.uniform(1.2, 5)
            diviseurHauteur = random.uniform(1.2, 5)
            longueurImg, hauteurImg = background.size
            longueurImg = int(longueurImg / diviseurLongueur)
            hauteurImg = int(hauteurImg / diviseurHauteur)

            background.paste(img, (longueurImg, hauteurImg), img)
            background.save(ImgSuperposes, filename=ImgSuperposes)
            file2 = discord.File(ImgSuperposes, filename=ImgSuperposes)
            await msg.channel.send("Photo : ", file=file2)
        except:
            await msg.channel.send("Une erreur est survenue")
            
disc_Bot = Bot()
disc_Bot.run(os.getenv("TOKEN"))