import discord, requests, datetime
from discord.ext import commands, tasks

class Epic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @tasks.loop(time=datetime.time(second=1))       ###Developing###
    async def loop(self):
        date = datetime.datetime.now()
        if date.strftime("%A") == "Monday":
            data = requests.get("https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=pt-PT&country=PT&allowCountries=PT")
            data = data.json()
            print(data)
            data = data["data"]["Catalog"]["searchStore"]["elements"]  # Cleans the data
            # processed_data = []
            # for i in raw_data:
            #                 try:
            #                     if i["promotions"]["promotionalOffers"]:
            #                         game = i["title"] 
            #                         processed_data.append(game)
            #                 except TypeError:
            #                     pass
            # channel = self.bot.get_channel(1002990647831175320)
            # await channel.send("**{}** is now free on the Epic store!".format(processed_data[0]))
async def setup(bot):
    await bot.add_cog(Epic(bot))