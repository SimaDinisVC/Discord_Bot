import discord, json
from discord import File
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound

class Manager(commands.Cog):
    """Manage the bot"""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener() 
    async def on_ready(self): # When the bot start running
        print(f">> I'm ready and connected like {self.bot.user}.") # Notify the command center that it's ready
        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Game("VS CODE"))

    @commands.Cog.listener()
    async def on_message(self, message): # Here he read's every message and analyse to see if have badwords on the message
        if message.author == self.bot.user: # We don't need analyse bot message's so I return the function
            return
        
        badwords = [] # badword will be stored here
        for badword in badwords:
            if badword in message.content:
                await message.delete() # it delete the member message and 
                await message.channel.send(
                    f'{message.author.mention}, não podes dizer a palavra ||{badword}||', delete_after=10.0 , mention_author=True
                ) # send a message (that message autoremove on 10 sec) that he can't say that word

    @commands.Cog.listener()
    async def on_guild_join(self, guild): # When the bot enter to a Server
        default_channel = guild.system_channel
        embed = discord.Embed(
            color = 0x759b87,
            title = "Hey! Finalmente acordei!",
            description = "Adoro este espacinho para mim! Só precisa de ser ajustado, podes fazer isso por mim?"
        )
        embed.add_field(name="1º", value="Podes familiarizar-te com os meus comandos usando o !help. 😉", inline=True)
        embed.add_field(name="2º", value="Faz-me uma tour por este sítio e mostra-me tudo através do !config. 🗼", inline=True)
        embed.add_field(name="3º", value="Diverte-te! Eu aviso-te quando houver algum problema por perto. ✌️", inline=True)
        embed.set_footer(text=f"Em colaboração com {guild.name} | FriendBot.", icon_url=guild.icon)
        await default_channel.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_member_join(self, member): # Need get inicial roles
        data = json.load(open("data/config.json")) # Parse to Python the data
        guild = member.guild.id
        welcome = data.get(str(guild), False) # Check the guild is knowned
        if welcome:
            welcome = data[str(guild)].get("Welcome Mode", False) # Check the mode is able
            if welcome:
                welcome = data[str(guild)].get("Welcome Channel", False) # Check the welcome channel id is knowned
                rules = data[str(guild)].get("Rules Channel", False) # Check the rules channel id is knowned
                if welcome:
                    welcome = self.bot.get_channel(int(welcome))
                    background = Editor("images/amanhecer.png")
                    profile_img = await load_image_async(str(member.default_avatar))
                    profile = Editor(profile_img).resize((255, 250)).circle_image()
                    montserrat = Font.montserrat(size=50, variant="bold")
                    poppins_small = Font.poppins(size=20, variant="light")
                    background.paste(profile, (450, 150))
                    background.ellipse((450, 150), 255, 250, outline="white", stroke_width=5)
                    background.text((599, 450), f"BEM-VINDO(A) A {str(member.guild.name).upper()}!", color="white", font=montserrat, align="center")
                    background.text((599, 525), f"{member.name}#{member.discriminator}", color="white", font=poppins_small, align="center")
                    file = File(fp=background.image_bytes, filename="amanhecer.png")
                    if rules:
                        rules = self.bot.get_channel(int(rules))
                        await welcome.send(f"Olá {member.mention}! Bem-Vindo(a) ao {member.guild.name}, para mais info consulta as {rules.mention}.", file=file)
                    else:
                        await welcome.send(f"Olá {member.mention}! Bem-Vindo(a) ao {member.guild.name}, para mais info consulta as regras.", file=file)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error): # Protection's for command's
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("É favor enviar todos os Argumentos. Introduza !help para ver os parâmetro de cada comando.")
        elif isinstance(error, CommandNotFound):
            await ctx.send("O comando não existe. Introduza !help para ver os comandos.")
        else:
            raise error

async def setup(bot):
    await bot.add_cog(Manager(bot))