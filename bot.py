import os, discord, asyncio # os - get the .env ; discord - discord.py v.2.0.0 ; asyncio - to run the bot ;
from discord.ext import commands # to use command's in the bot
from dotenv import load_dotenv # to load the .env

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), help_command=None) # Set "!" to prefix command; set all intents; remove help command;

load_dotenv() # load all env's

async def launcher():
# ↓↓↓↓ load all the cogs to simplify my code ↓↓↓↓
    await bot.load_extension("tasks.manager")
    await bot.load_extension("tasks.logs")
    await bot.load_extension("tasks.epicfreegames")
    await bot.load_extension("commands.smarts")
    await bot.load_extension("commands.config")
    await bot.load_extension("commands.reports")
    await bot.load_extension("commands.embeds")
    await bot.load_extension("commands.talks")

    await bot.start(os.getenv('TOKEN')) # will Launch the bot with the API TOKEN

asyncio.run(launcher()) # will Run actually the bot