import discord
from discord.ext import commands
import random

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
    if residuo in ["papel", "carton" , " cuadernos" , "revistas" , "periodicos" , "folletos" , "bolsas de papel" , "sobres"]:
        await ctx.send(f"El {residuo} va al contenedor AZUL para reciclaje")
    elif residuo in ["plastico" , "botella" , "bolsas plasticas" , "envases de yogurt" , "latas" , "tapas"]:
        await ctx.send(f"El{residuo} va al contenedor AMARILLO para reciclaje")
    elif residuo in ["pañal" , "cigarrillo" , "polvo"]:
        await ctx.send(f"El{residuo} va al contenedor NEGRO para ayudar al reciclaje")
    else:
        await ctx.send(f"No tengo informacion para el residuo: {residuo}")

@bot.command()
async def manualidadreciclable(ctx):
    manualidadreciclable= [
        "Macetas colgantes con botellas plásticas",
    "Portalápices con botellas plásticas",
    "Alcancía con forma de cerdito (botella plástica)",
    "Riego por goteo con botellas plásticas",
    "Portavelas decorativos con latas de aluminio",
    "Portalápices con latas de aluminio",
    "Organizadores con latas de aluminio",
    "Casitas de cartón para jugar",
    "Organizadores de escritorio con cajas de cartón",
    "Rompecabezas casero con cartón",
    "Animales decorativos con tubos de papel higiénico",
    "Organizador de cables con tubos de cartón",
    "Prismáticos (binoculares) de juguete con tubos de papel",
    "Monederos o billeteras con bricks (envases de jugo/leche)",
    "Organizadores inclinados con bricks",
    "Casitas para pájaros con bricks",
    "Cuadros o mosaicos con tapitas plásticas",
    "Imanes decorativos para nevera con tapitas",
    "Juegos de memoria con tapitas plásticas",
    "Bolsas reutilizables con camisetas viejas",
    "Cojines con retazos de ropa",
    "Pulseras o cintillos con tiras de tela"
]
    await ctx.send(random.choice(manualidadreciclable))

bot.run("")
