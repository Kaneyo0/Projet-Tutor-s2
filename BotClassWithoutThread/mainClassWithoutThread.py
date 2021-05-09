from time import sleep
from dotenv import load_dotenv
import alarme
import camera
import nasapy
import os
import urllib.request
import RPi.GPIO as GPIO
import discord
from discord.ext import commands
from picamera import PiCamera

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

buzzer = 6
bouton = 23
led = 5
GPIO.setup(led, GPIO.OUT)
GPIO.setup(bouton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzzer, GPIO.OUT)

BestFish = "poisson.jpg"
Image = "image.jpeg"
load_dotenv(dotenv_path="config")
key = os.environ.get(os.getenv("NASATOKEN"))
nasa = nasapy.Nasa(key=key)

class Bot(commands.Bot, discord.Client):

    def __init__(self):
        super(Bot, self).__init__(command_prefix="!")
        self.add_command(commands.Command(self.bestfish, name="bestfish"))
        self.add_command(commands.Command(self.fish, name="fish"))
        self.add_command(commands.Command(self.nasa, name="nasa"))

    async def on_ready(self):
        print(f"{self.user.display_name} est connecté")

    async def bestfish(self, msg):
        try:
            file = discord.File(BestFish, filename=BestFish)
            await msg.channel.send("Neuneuil : ", file=file)
        except:
            await msg.channel.send("Erreur : la photo n'a pas pu être envoyée.")

    async def fish(self, msg):
        #try:
            print("test")
            camera.Camera().prendrePhoto(PiCamera)
            print("la camera fonctionne")
            file = discord.File(Image, filename=Image)
            await msg.channel.send("Image de la rasberry : ", file=file)
        #except:
            await msg.channel.send("Erreur : La camera n'est pas branchée")
            try:
                alarme.Alarme().activationAlarme(buzzer)
            except:
                await msg.channel.send("Erreur : le buzzer n'est pas branché.")
            try:
                alarme.Alarme().activationLed(led, bouton)
            except:
                await msg.channel.send("Erreur : la led n'est pas branchée.")
            try:
                file = discord.File(BestFish, filename=BestFish)
                await msg.channel.send("Voici votre image préféré de Neuneuil par défaut : ", file=file)
            except:
                await msg.channel.send("Erreur : la photo n'a pas pu être envoyée.")

    async def nasa(self, msg):
        try:
            await msg.channel.send(nasa.picture_of_the_day()["hdurl"])
        except:
            await msg.channel.send("Une erreur est survenue")
            
disc_Bot = Bot()
disc_Bot.run(os.getenv("TOKEN"))
