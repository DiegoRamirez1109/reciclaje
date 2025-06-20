import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot (command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} esta conectado y listo para reducir la contaminacion")

@bot.command()
async def hola (ctx):
    await ctx.send("¡Hola! soy tu bot para ayudarte a reducir la contaminacion")

@bot.command()
async def clasificar(ctx, residuo: str):
    residuo = residuo.lower()
    if residuo in ["papel", "carton"]:
        await ctx.send(f"El {residuo} va al contenedor AZUL para reciclaje")
    elif residuo in ["plastico" , "botella"]:
        await ctx.send(f"El{residuo} va al contenedor AMARILLO para reciclaje")
    else:
        await ctx.send(f"No tengo informacion para el residuo: {residuo}")    
    

bot.run("")
