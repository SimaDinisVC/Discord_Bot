from discord.ext import commands
import discord

class Talks(commands.Cog):
    """Talks with the user"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="olá", help="Dá as boas-vindas (Sem argumentos)")
    async def send_hello(self, ctx):
        name = ctx.author.name
        response = "Olá, " + name + "!"
        
        await ctx.send(response)

    @commands.command(name="boa_noite", help="Dá as boas noites (Sem argumentos)")
    async def send_goodNight(self, ctx):
        name = ctx.author.name
        response = "Boa noite, " + name + "!"
        
        await ctx.send(response)
    @commands.command(name="segredo", help="Envia um segredo em privado ao usuário (Sem argumentos)")
    async def secret(self, ctx):
        try:
            await ctx.author.send("xD")
        except discord.errors.Forbidden:
            await ctx.send("Não te consigo contactar, habilita a opção de 'qualquer pessoa do servidor pode mandar mensagem'! - (Opções > Privacidade)")

def setup(bot):
    bot.add_cog(Talks(bot))