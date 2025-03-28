from discord.ext import commands
from scraper import Scrapper
from discord.ext.commands import Context
from utils.formatter import format_discord_message

class Macbook(commands.Cog, name="macbook"):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.hybrid_command(
        name="macbook",
        description="Lista as offerções de macbooks se disponível",
    )
    async def get_macbook_offer(self, ctx: Context) -> None:
        req = Scrapper("/?s=macbook")
        offers = req.get_offers()

        if offers:
            macbooks = []

            for offer in offers:
                embed = format_discord_message(offer)
                macbooks.append(embed)

            for embed in macbooks:
                await ctx.send(embed=embed)
        else:
            await ctx.send("Não foi possível encontrar promoções de Macbook.")


async def setup(bot) -> None:
    await bot.add_cog(Macbook(bot))
