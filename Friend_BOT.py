# import os # for terminal access
# clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear') # It recognizes if you are on Windows or Linux and puts the correct command to clean the console 
# os.system("pip install discord") # to install discord library
# os.system("pip install requests") # to install requests library
# clearConsole()
# print(">> All libraries were successfully installed or updated.")
import discord, requests # to create a working bot
from discord.ext import commands, tasks # to use commands and tasks with the bot
# import datetime

bot = commands.Bot("!") # The bot prefix is "!"
badwords = []

@bot.event
async def on_ready():
    print(f">> I'm ready and connected like {bot.user}.")
    # current_time.start()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    for badword in badwords:
        if badword in message.content:
            await message.channel.send(
                f'@{message.author.name}, não ofenda os outros.'
            )
            await message.delete()

    await bot.process_commands(message)

@bot.command(name="olá")
async def send_hello(ctx):
    name = ctx.author.name

    response = "Olá, " + name + "!"
    
    await ctx.send(response)

@bot.command(name="boa_noite")
async def send_goodNight(ctx):
    name = ctx.author.name

    response = "Boa noite, " + name + "!"
    
    await ctx.send(response)

@bot.command(name="calc")
async def calculate_expression(ctx, *expression):
    try:
        for n in expression:
            if len(n) > 8:
                raise ValueError
        expression = "".join(expression)
        response = eval(expression)
        await ctx.send(f"O resultado é {response}.")
    except:
        await ctx.send(f"O resultado é N/A.")

@bot.command(name="conv")
async def binance(ctx, coin, base):
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

@bot.command(name="segredo")
async def secret(ctx):
    try:
        await ctx.author.send("xD")
    except discord.errors.Forbidden:
        await ctx.send("Não te consigo contactar, habilita a opção de 'qualquer pessoa do servidor pode mandar mensagem'! - (Opções > Privacidade)")

@bot.command(name="embed")
async def verifier_embed(ctx):
    embed = discord.Embed(
        title = "**Reage para seres Verificado**",
        description = "Reage com este emoji ✅ a esta mensagem para teres acesso ao servidor.\nOu se vieste modificar a cor do nome e queres voltar para o servidor basta retirares a reação ✅ e acionares de novo.",
        color = 0x6DFF94
    )
    
    embed.set_author(name=bot.user.name, icon_url="https://www.pngmart.com/files/17/Verification-Logo-Transparent-PNG.png")

    await ctx.send(embed=embed)

# @tasks.loop(hours=24)
# async def current_time():
#     now = datetime.datetime.now()
#     now = now.strftime("%d/%m/%Y ás %H:%M:%S")
#     channel = bot.get_channel(988151166057738252)
#     await channel.send("Data atual: " + now)

bot.run("OTg4MTQ5NTU2MjEyNTYzOTk4.GHJyaT.7OnQYIZ_g5qwVVz-zb_9IW5QaITtevNXwvL3Is") # The configs goes before of this line code