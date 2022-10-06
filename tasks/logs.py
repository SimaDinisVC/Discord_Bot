import discord, json
from discord.ext import commands

class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_invite_create(self, invite):
        data = json.load(open("data/config.json"))
        logs = data.get(str(invite.guild.id), False) # Check the guild is knowned
        if logs:
            logs = data[str(invite.guild.id)].get("Logs Mode", False) # Check the mode is able
            if logs:
                logs = data[str(invite.guild.id)].get("Logs Channel", False) # Check the channel id is knowned
                if logs:
                    channel = self.bot.get_channel(int(logs)) # Get the channel
                    embed = discord.Embed(
                        color = 0x9dbb31,
                        title = "Novo convite gerado!",
                        description = f"Um novo convite foi gerado por {invite.inviter.mention}.",
                        url=f"{invite.url}"
                    )
                    formatdate = "%d/%m/%Y %H:%M"
                    embed.set_footer(text=f"Convite criado a {invite.created_at.strftime(formatdate)} • {invite.inviter}", icon_url=invite.inviter.avatar)
                    embed.add_field(name="Expira em:", value=f"{invite.expires_at.strftime(formatdate)}", inline=True)
                    if int(invite.max_uses) == 0:
                        embed.add_field(name="Máximo de Usos:", value=f"Ilimitado", inline=True)
                    else:
                        embed.add_field(name="Máximo de Usos:", value=f"{invite.max_uses}", inline=True)
                    embed.add_field(name="Criado para o canal:", value=f"{invite.channel}", inline=True)
                    await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Logs(bot))