import discord, datetime, json
from discord.ext import commands

class Bugg(discord.ui.Modal, title='Reportar um Erro!'):
    subject = discord.ui.TextInput(label='Assunto', placeholder="Titulo do Report")
    answer = discord.ui.TextInput(label='Detalhes', style=discord.TextStyle.paragraph, placeholder="Descreve detalhadamente o erro")
    
    async def on_submit(self, interaction):
        user = interaction.client.get_user(619620655322890241)
        embed = discord.Embed(
            color=0xe10505, 
            title=self.subject, 
            description=self.answer,
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_author(name="Formulário de Report",url=f"https://discordapp.com/users/{interaction.user.id}", icon_url=interaction.user.avatar)
        await user.send(f"Novo Report Submetido por {interaction.user.mention}", embed=embed)
        await interaction.response.send_message(f'Obrigado pela tua cooperação, {interaction.user.mention}!',embed=embed, ephemeral=True)

    async def on_error(self, interaction, error: Exception):
        await interaction.response.send_message('Oops! Algo correu mal, fica para a próxima!', ephemeral=True)

class Member(discord.ui.Modal, title="Reportar um Membro!"):
    member = discord.ui.TextInput(label='ID do Membro', placeholder="Tem que ter o modo desenvolvedor ativo para obter o id")
    answer = discord.ui.TextInput(label='Detalhes', style=discord.TextStyle.paragraph, placeholder="Descreve detalhadamente o que aconteceu")

    async def on_submit(self, interaction):
        guild = interaction.guild.id
        data = json.load(open("data/config.json"))
        user = interaction.client.get_user(int(str(self.member)))
        logs = data.get(str(guild), False)
        if logs and data[str(guild)].get("Logs Mode", False):
            logs = data[str(guild)].get("Logs Channel", False) # NEED Change
        if logs == False:
            await interaction.response.send_message(f'Os Superiores do Server ainda não habilitaram/configuraram o Canal de Logs terão de o fazer usando o !config para poderes dar report!')
        elif user == None:
            await interaction.response.send_message(f'ID de Membro é inválido! Clique com o botão direito no membro a reportar e > Copiar ID.')
        else:
            logs_channel = interaction.client.get_channel(int(logs))
            embed = discord.Embed(
                color=0xe10505, 
                title=self.answer,
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_author(name="Formulário de Report",url=f"https://discordapp.com/users/{user.id}", icon_url=interaction.user.avatar)
            embed.set_thumbnail(url=user.avatar)
            embed.add_field(name="Membro Reportado:", value=user.mention)
            embed.add_field(name="Reportador:", value=interaction.user.mention)
            await logs_channel.send(embed=embed)
            await interaction.response.send_message(f'Obrigado pela tua cooperação, {interaction.user.mention}!',embed=embed, ephemeral=True)

    async def on_error(self, interaction, error: Exception):
        await interaction.response.send_message('Oops! Algo correu mal, fica para a próxima!', ephemeral=True)


class Reports(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="bugg_report", help="Cria um formulário onde podes reportar um bugg do bot!")
    async def bugg(self, ctx):
        button = discord.ui.Button(label="Reportar um Erro?", style=discord.ButtonStyle.danger)

        async def callback(interaction):
            await interaction.response.send_modal(Bugg())

        button.callback = callback
        view = discord.ui.View()
        view.add_item(button)

        await ctx.send(view=view, delete_after=20.0)
        await ctx.message.delete()

    @commands.command(name="member_report", help="Cria um formulário onde podes reportar um membro para os Superiores!")
    async def member(self, ctx):
        button = discord.ui.Button(label="Reportar um Membro?", style=discord.ButtonStyle.danger)

        async def callback(interaction):
            await interaction.response.send_modal(Member())

        button.callback = callback
        view = discord.ui.View()
        view.add_item(button)

        await ctx.send(view=view, delete_after=20.0)
        await ctx.message.delete()

async def setup(bot):
    await bot.add_cog(Reports(bot))