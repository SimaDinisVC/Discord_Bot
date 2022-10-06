import discord, json
from discord.ext import commands

class Config(commands.Cog):
    """Configurate the Channel's"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="config", help="Configurate the channel's server.")
    async def configuration(self, ctx):
        if ctx.author.guild_permissions.administrator:
            await ctx.message.delete()
            selectdata = {"Welcome Channel":"Bem-Vindos","Logs Channel":"Logs","Announcement's Channel":"Anúncios", "Rules Channel":"Regras"} # To Set the next Select
            buttonsdata = {"Welcome Mode":"Boas-Vindas", "Logs Mode":"Registro de Auditoria"} # To Set the next Button
            btnsorder = list(buttonsdata)

            select = discord.ui.Select( #
                min_values=1, max_values=1,
                placeholder=f"Selecione o canal de Bem-Vindos!",
                options=[discord.SelectOption(label="❌Não configurar / Manter❌")]
            )
            for channel in ctx.guild.text_channels:
                select.options.append(discord.SelectOption(label=str(channel)))

            ButtonYes = discord.ui.Button(label="Ativar", style=discord.ButtonStyle.green, emoji="♻️")
            ButtonNo = discord.ui.Button(label="Desativar", style=discord.ButtonStyle.danger, emoji="🛑")

            async def select_callback(interaction):
                if ctx.author == interaction.user:
                    nonlocal msg
                    await msg.delete() # delete the select
                    order = list(selectdata) # Get the order non apered settings
                    data = json.load(open("data/config.json")) # Parse to Python the data
                    if select.values[0] != "❌Não configurar / Manter❌":
                        channel = discord.utils.get(ctx.guild.text_channels, name=select.values[0]) # Get the channel
                        if data.get(str(ctx.guild.id), None) == None: # Verify if the guild is unknowned
                            data[str(ctx.guild.id)] = {order[0]:channel.id}
                        else:                                             # Do alterations
                            data[str(ctx.guild.id)][order[0]] = channel.id
                        with open("data/config.json", "w") as file:
                            file.write(json.dumps(data)) # Parse to JSON an write in the file
                        await interaction.response.send_message(f"Canal de {selectdata[order[0]]} foi configurado para {channel.name}.", ephemeral=True)
                    else:
                        if data.get(str(ctx.guild.id), None) != None:
                            channel_id = data[str(ctx.guild.id)].get(order[0], None)
                            if channel_id != None:
                                channel = discord.utils.get(ctx.guild.text_channels, name=channel_id) # Get the channel
                                await interaction.response.send_message(f"Canal de {selectdata[order[0]]} está configurado para {channel.name}.", ephemeral=True)
                        await interaction.response.send_message(f"Canal de {selectdata[order[0]]} não foi configurado.", ephemeral=True)
                    if len(order) > 1:
                        select.placeholder = f"Selecione o canal de {selectdata[order[1]]}!" # If have other settings to set change the next placeholder
                        selectdata.pop(order[0]) # And remove the apered selection in the order non apered settings 
                        msg = await ctx.send(view=view, delete_after=20.0)
                    else:
                        selectdata.pop(order[0])
                        view.clear_items()
                        view.add_item(ButtonYes)
                        view.add_item(ButtonNo)
                        msg = await ctx.send(f"Ativar ou Desativar o modo de {buttonsdata[btnsorder[0]]}?", view=view, delete_after=20.0)
                else:
                    await interaction.response.send_message("Esta interação não é para ti!", ephemeral=True) # When an Admin open the command and a member interact

            async def ButtonYes_callback(interaction):
                if ctx.author == interaction.user:
                    nonlocal btnsorder, msg
                    data = json.load(open("data/config.json")) # Parse to Python the data
                    if data.get(str(ctx.guild.id), None) == None: # Verify if the guild is unknowned
                        data[str(ctx.guild.id)] = {btnsorder[0]:True}
                    else:                                             # Do alterations
                        data[str(ctx.guild.id)][btnsorder[0]] = True
                    with open("data/config.json", "w") as file:
                        file.write(json.dumps(data)) # Parse to JSON an write in the file
                    await msg.delete() # delete the select
                    await interaction.response.send_message(f"O modo de {buttonsdata[btnsorder[0]]} foi configurado para Ativado.", ephemeral=True)
                    if len(btnsorder) > 1:
                        btnsorder.pop(0) # And remove the apered selection in the order non apered settings
                        msg = await ctx.send(f"Ativar ou Desativar o modo de {buttonsdata[btnsorder[0]]}?", view=view, delete_after=20.0)
                    else:
                        await interaction.response.send_message("Configuração Concluida!", ephemeral=True) # When's done send a message!
                else:
                    await interaction.response.send_message("Esta interação não é para ti!", ephemeral=True) # When an Admin open the command and a member interact

            async def ButtonNo_callback(interaction):
                if ctx.author == interaction.user:
                    nonlocal btnsorder, msg
                    data = json.load(open("data/config.json")) # Parse to Python the data
                    if data.get(str(ctx.guild.id), None) == None: # Verify if the guild is unknowned
                        data[str(ctx.guild.id)] = {btnsorder[0]:False}
                    else:                                             # Do alterations
                        data[str(ctx.guild.id)][btnsorder[0]] = False
                    with open("data/config.json", "w") as file:
                        file.write(json.dumps(data)) # Parse to JSON an write in the file
                    await msg.delete() # delete the select
                    await interaction.response.send_message(f"O modo de {buttonsdata[btnsorder[0]]} foi configurado para Desativado.", ephemeral=True)
                    if len(btnsorder) > 1:
                        btnsorder.pop(0) # And remove the apered selection in the order non apered settings
                        msg = await ctx.send(f"Ativar ou Desativar o modo de {buttonsdata[btnsorder[0]]}?", view=view, delete_after=20.0)
                    else:
                        await interaction.response.send_message("Configuração Concluida!", ephemeral=True) # When's done send a message!
                else:
                    await interaction.response.send_message("Esta interação não é para ti!", ephemeral=True) # When an Admin open the command and a member interact

            select.callback = select_callback
            ButtonYes.callback = ButtonYes_callback
            ButtonNo.callback = ButtonNo_callback
            view = discord.ui.View()
            view.add_item(select)

            msg = await ctx.send(view=view, delete_after=20.0)
        else:
            await ctx.send("Apenas os administradores têm permissões para me configurar.", delete_after=10.0)

async def setup(bot):
    await bot.add_cog(Config(bot))
    