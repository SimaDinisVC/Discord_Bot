from discord.ext import commands
import requests

class Converter(commands.Cog):
    """Works with an API "free.currconv.com/api" that convert a coin to another"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="conv", help="Converte uma moeda para outra (Argumentos: Moeda, Moeda Base)") # Using an API "free.currconv.com/api" we can convert a coin to another
    async def converter(self, ctx, coin, base):
        try:
            response = requests.get(f"https://free.currconv.com/api/v7/convert?q={coin.upper()}_{base.upper()}&compact=ultra&apiKey=cb5045d6da7ec34af679")
            data = response.json()
            price = round(float(data.get(f"{coin.upper()}_{base.upper()}")),3)

            if price:
                await ctx.send(f"O valor do par {coin}/{base} é {price}€")
            else:
                raise ValueError
        except:
            await ctx.send(f"O par {coin}/{base} é inválido.")

def setup(bot):
    bot.add_cog(Converter(bot))