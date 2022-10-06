from discord.ext import commands
import discord

class Talks(commands.Cog):
    """Talks with the user"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="olá", help="Dá as boas-vindas (Sem argumentos)")
    async def send_hello(self, ctx):
        await ctx.send("Olá, {}!".format(ctx.message.author.mention))

    @commands.command(name="boa_noite", help="Dá as boas noites (Sem argumentos)")
    async def send_goodNight(self, ctx):
        await ctx.send("Boa noite, {}!".format(ctx.message.author.mention))

    @commands.command(name="segredo", help="Envia um segredo em privado ao usuário (Sem argumentos)")
    async def secret(self, ctx):
        try:
            await ctx.author.send("xD")
        except discord.errors.Forbidden:
            await ctx.send("Não te consigo contactar, habilita a opção de 'qualquer pessoa do servidor pode mandar mensagem'! - (Opções > Privacidade)")

async def setup(bot):
    await bot.add_cog(Talks(bot))