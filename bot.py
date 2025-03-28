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
            embed = discord.Embed(
                title=f"**{promo['title']}**", color=discord.Color.blue()
            )

            embed.set_thumbnail(url=promo["image"])

            details = (
                f"💸 ***Preço:*** {promo['price']}\n\n💳 ***Método de Pagamento:*** {promo['payment_method']}\n\n"
                + (f"🎁 ***Cupom:*** {promo['coupon']}\n\n" if promo["coupon"] else "")
                + f"🔗 **[Ir para a Loja]({promo['link']})**"
            )
            embed.add_field(name="\u200b", value=details, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("Não foi possível encontrar promoções.")


bot.run(TOKEN)
