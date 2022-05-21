
from discord import File
import discord
from discord import Embed, Interaction, app_commands
from discord.ext import commands
from utilis.sql import get , add , invent
import datetime
from cogs.play import animals


class basics(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @app_commands.command(name="daily", description="get daily rewards")
    @app_commands.guild_only()
    @app_commands.checks.cooldown(1, 86400, key=lambda i: (i.guild_id, i.user.id))
    async def daily(self, interaction: discord.Interaction) -> None:
        await interaction.response.defer(ephemeral=False, thinking=True)
        author = interaction.user.id

        user = await self.bot.db.fetch("SELECT * FROM user_info WHERE user_id = $1", author)
        if not user:
            await interaction.followup.send("Imagine Trying to play without a profile , Someone needs a memory pill")

        else:
            daily = 15000 
            await add(self,daily,interaction.user.id)
            embed = discord.Embed(title="Daily Reward" ,description=f"You Got 15000 Coins As Your Daily reward\n\nVote For Us to Get Some More Exciting Rewards\nJoin Our Support Server For Reporting Bugs And for Events",timestamp=datetime.datetime.utcnow())
            
            await interaction.followup.send(embed=embed)          



    @app_commands.command(name="balance", description="Check your balance")
    @app_commands.guild_only()
    @app_commands.checks.cooldown(1, 30, key=lambda i: (i.guild_id, i.user.id))
    async def balance(self, interaction: discord.Interaction) -> None:
        await interaction.response.defer(ephemeral=False, thinking=True)
        author = interaction.user.id
        bal =  await get(self,author)
        embed = discord.Embed(title=f"{interaction.user}'s Mana" , description=f"**Coins** - ``{bal}``\n**Mana** - ``0``")
        await interaction.followup.send(embed=embed)


    @balance.error
    async def on_balance_error(self,interaction: discord.Interaction, error: app_commands.AppCommandError):
        await interaction.response.defer(ephemeral=True, thinking=True)
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.followup.send("command is on 30 second cooldown Try again later")


    @daily.error
    async def on_daily_error(self,interaction: discord.Interaction, error: app_commands.AppCommandError):
        await interaction.response.defer(ephemeral=True, thinking=True)
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.followup.send("command is on 1 Day cooldown Try again later")


    @app_commands.command(name="inventory", description="check you inventory")
    @app_commands.guild_only()
   
   
    async def inventory(self, interaction: discord.Interaction) -> None:
        await interaction.response.defer(ephemeral=False, thinking=True)
        
        author = interaction.user.id
        lol = await self.bot.db.fetch("SELECT item_info.item_name,user_inventory.count,user_inventory.emote_id FROM user_inventory INNER JOIN item_info USING(item_id) WHERE  user_inventory.user_id = $1",author)
        embed=discord.Embed(title=f"{interaction.user.name}'s Inventory " , description="")
            
        for element in lol:
            embed.description += f"{element.get('emote_id', 'no id')} {element.get('item_name', 'no name')} - {element.get('count', 'NaN')}\n"
        await interaction.followup.send(embed=embed)
# end
async def setup(bot) -> None:
    await bot.add_cog(basics(bot))