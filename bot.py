import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
# from scraper import Scrapper

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot {bot.user} está online!")


async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)


asyncio.run(main())

# @bot.command(name="offers")
# async def listar_offers(ctx):
#     offers = Scrapper().get_offers()
#     if isinstance(offers, str):
#         await ctx.send(offers)
#     else:
#         if offers:
#             offer = offers[0]
#             embed = discord.Embed(
#                 title=f"**{offer['title']}**", color=discord.Color.blue()
#             )

#             embed.set_thumbnail(url=offer["image"])

#             details = (
#                 f"💸 ***Preço:*** {offer['price']}\n\n💳 ***Método de Pagamento:*** {offer['payment_method']}\n\n"
#                 + (f"🎁 ***Cupom:*** {offer['coupon']}\n\n" if offer["coupon"] else "")
#                 + f"🔗 **[Ir para a Loja]({offer['link']})**"
#             )
#             embed.add_field(name="\u200b", value=details, inline=False)

#             await ctx.send(embed=embed)
#         else:
#             await ctx.send("Não foi possível encontrar promoções.")


# bot.run(TOKEN)
