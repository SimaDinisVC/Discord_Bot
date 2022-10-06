from discord.ext import commands
import requests

class Smarts(commands.Cog):
    """Works with an API's'"""

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

    @commands.command(name="calc", help="Calcula uma expressão matemática (Argumentos: Expressão matemática)") # it calculate mathmatic expression's
    async def calculate_expression(self, ctx, *expression):
        try:
            for n in expression:
                if len(n) > 8:
                    raise ValueError
            expression = "".join(expression)
            response = eval(expression)
            await ctx.send(f"O resultado é {response}.")
        except:
            await ctx.send(f"O resultado é N/A.")

    @commands.command(name="ping", help="Mostra a lantência do bot.")
    async def pong(self, ctx):
        await ctx.send(f'Pong! A minha lantência é de {round(self.bot.latency * 1000)}ms.')

async def setup(bot):
    await bot.add_cog(Smarts(bot))