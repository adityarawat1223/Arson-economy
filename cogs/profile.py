
import discord
from discord import File
from discord import Embed, Interaction, app_commands
from discord.ext import commands









class anime(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    
    @app_commands.command(name="start", description="start you journey cmon we are waiting for you")
    @app_commands.guild_only()
    
    async def start(self, interaction: discord.Interaction) -> None:
        await interaction.response.defer(ephemeral=False, thinking=True)
        author = interaction.user.id
        user = await self.bot.db.fetch("SELECT * FROM user_info WHERE user_id = $1",author)
        if not user:
            await self.bot.db.execute("INSERT INTO user_info (user_id, name ,money) VALUES ($1,$2,$3)",author,interaction.user.name,10000)
            await interaction.followup.send("Done , Welcome To My World I can kill you Anytime So Beware **Stop forshadowing**")
        else:
            await interaction.followup.send("Checking Your profile , This profile already exist, deleting your profile for scamming me ,  3.. 2.. 1 Just kidding")


    
        
            


#end
async def setup(bot) -> None:
  await bot.add_cog(anime(bot))