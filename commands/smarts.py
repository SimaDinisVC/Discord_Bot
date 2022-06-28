from discord.ext import commands


class Smarts(commands.Cog):
    """A lot of Smart Commands"""

    def __init__(self, bot):
        self.bot = bot

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

def setup(bot):
    bot.add_cog(Smarts(bot))