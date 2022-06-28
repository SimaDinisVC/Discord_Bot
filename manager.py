from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound


class Manager(commands.Cog):
    """Manage the bot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f">> I'm ready and connected like {self.bot.user}.")

    @commands.Cog.listener()
    async def on_message(self, message): # Here he read's every message that and analyse to see if have badwords in the message
        if message.author == self.bot.user: # We don't need analyse bot message's so I return the function
            return
        
        badwords = ["cabrão", "fdp"]
        have = False
        for badword in badwords:
            if badword in message.content:
                have=True
                bad = badword
        if have:
            await message.channel.send(
                f'{message.author.mention}, não pode dizer a palavra ||{bad}||', delete_after=10.0 , mention_author=True
            )
            await message.delete()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error): # Protection's for command's
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("É favor enviar todos os Argumentos. Introduza !help para ver os parâmetro de cada comando.")
        elif isinstance(error, CommandNotFound):
            await ctx.send("O comando não existe. Introduza !help para ver os comandos.")
        else:
            raise error

def setup(bot):
    bot.add_cog(Manager(bot))