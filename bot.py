from distutils import extension
from multiprocessing import managers
import os
from discord.ext import commands # to use commands and tasks with the bot
from dotenv import load_dotenv # to use load the .env

bot = commands.Bot("!") # the bot prefix is "!"

def load_cogs(bot):
    bot.load_extension("manager") # get the mana ger

    for file in os.listdir("commands"): # get the extensions in the folder tasks
        if file.endswith(".py"):
            cog = file[:-3:]
            bot.load_extension(f"commands.{cog}")
    
    for file in os.listdir("tasks"): # get the extensions in the folder tasks
        if file.endswith(".py"):
            cog = file[:-3:]
            bot.load_extension(f"tasks.{cog}")

load_cogs(bot)

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot.run(TOKEN) # the configs goes before of this line code^