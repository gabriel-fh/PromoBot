import discord
from discord import Embed

def format_discord_message(offer: dict) -> Embed:
    embed = discord.Embed(title=f"**{offer['title']}**", color=discord.Color.blue())
    
    embed.set_thumbnail(url=offer["image"])
    
    details = (
        f"💸 ***Preço:*** {offer['price']}\n\n💳 ***Método de Pagamento:*** {offer['payment_method']}\n\n"
        + (f"🎁 ***Cupom:*** {offer['coupon']}\n\n" if offer["coupon"] else "")
        + f"🔗 **[Ir para a Loja]({offer['link']})**"
    )
    
    embed.add_field(name="\u200b", value=details, inline=False)
    return embed
