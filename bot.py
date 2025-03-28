import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from scraper import Scrapper

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot {bot.user} está online!")

@bot.command(name="promocoes")
async def listar_promocoes(ctx):
    promocoes = Scrapper().get_promotions() 
    if isinstance(promocoes, str):
        await ctx.send(promocoes) 
    else:
        if promocoes:
            promo = promocoes[0] 
            formatted_promo = f"**{promo['title']}**\nPreço: {promo['price']}\nMétodo de Pagamento: {promo['payment_method']}\nLink: {promo['link']}\nImagem: {promo['image']}\nCupom: {promo['coupon']}\n"
            await ctx.send(formatted_promo)
        else:
            await ctx.send("Não foi possível encontrar promoções.")

bot.run(TOKEN)
