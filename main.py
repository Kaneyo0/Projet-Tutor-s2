import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")


class Bot(commands.Bot, discord.Client):

    def __init__(self):
        super(Bot, self).__init__(command_prefix=";")
        self.add_command(commands.Command(self.poisson, name="poisson"))

    async def on_ready(self):
        print(f"{self.user.display_name} est connecté")

    async def poisson(self, msg):
        file = discord.File("media\poisson.jpg", filename="poisson.jpg")
        await msg.channel.send("Neuneuil : ", file=file)



disc_Bot = Bot()
disc_Bot.run(os.getenv("TOKEN"))
