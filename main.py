
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv(dotenv_path="config")


class Bot(commands.Bot, discord.Client):

    def __init__(self):
        super().__init__(command_prefix=";")

    async def on_ready(self):
        print(f"{self.user.display_name} est connecté")

    async def on_disconnect(self):
        print(f"{self.user.display_name} c'est déconnecté")

    async def on_message(self,msg):
        if(msg.content.lower() == "poisson"):
            file = discord.File("media\poisson.jpg", filename="poisson.jpg")
            await msg.channel.send("Neuneuil : ", file=file)
        if (msg.content.lower() == "sah"):
            await msg.channel.send("Quelle plaisir")

disc_Bot = Bot()
disc_Bot.run(os.getenv("TOKEN"))
