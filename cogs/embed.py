
from discord import File
import discord
from discord import Embed, Interaction, app_commands
from discord.ext import commands
from utilis.sql import get , add , invent


class embed(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="shop", description="dont be shy gimme your mana nad coins")
    @app_commands.guild_only()
    
    async def shop(self, interaction: discord.Interaction) -> None:
        await interaction.response.defer(ephemeral=False, thinking=True)
        embed1 = discord.Embed(title = "Shop" , description="\n <:chadness:977382544775458856> Rox Chadness <a:arrow:977461040033980428> 10000000 Coins \n\n<:bruh:977382543039012915> Shivam's Eye <a:arrow:977461040033980428> 1000 Mana \n\n <:f_:977382542699270145> Broken F Button <a:arrow:977461040033980428> 100000 Coins")
        embed1.set_footer(text="Page 1 OF 1")
        embed1.set_author(name="Kei Karuizawa" , url="https://discord.gg/enW9nYM4G9", icon_url="https://wallpapercave.com/wp/wp7985078.jpg")
        
        await interaction.followup.send(embed=embed1)

#end
async def setup(bot) -> None:
  await bot.add_cog(embed(bot))