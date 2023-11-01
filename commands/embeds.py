import discord
from discord.ext import commands
from discord import app_commands

class Embeds(commands.Cog):
    """Embeds Template"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="embed", help="Devolve um Embed de verificação (Sem argumentos)") # To send a Verification Embed
    async def verifier_embed(self, ctx):
        embed = discord.Embed(
            title = "**Reage para seres Verificado**",
            description = "Reage com este emoji ✅ a esta mensagem para teres acesso ao servidor.\nOu se vieste modificar a cor do nome e queres voltar para o servidor basta retirares a reação ✅ e acionares de novo.",
            color = 0x6DFF94
        )
        
        embed.set_author(name=self.bot.user.name, icon_url="https://www.pngmart.com/files/17/Verification-Logo-Transparent-PNG.png")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Embeds(bot))