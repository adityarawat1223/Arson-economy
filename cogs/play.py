
import random
import discord
from discord import File
from discord import Embed, Interaction, app_commands
from discord.ext import commands

animals = ["Bird", "Deer", None, "Insect",  None,None, "Insect",  None,"Deer", None,"Rabbit" , "Bird", "Deer" , "Insect","Rabbit" , None, "Bird", "Deer",  None, "Insect","Rabbit" ,  None,"Bird", "Deer" , "Insect",
           "Bird", None, "Gamabunta", "Rabbit", None, "Rabbit", None, None , "Rabbit" , "Bird", "Deer" , "Insect","Rabbit" ,  None,"Bird", "Deer" , "Insect", None]




class play(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    

    @app_commands.command(name="hunt", description="hunt some magical beast in jungle")
    @app_commands.guild_only()
    @app_commands.checks.cooldown(1, 30.0, key=lambda i: (i.guild_id, i.user.id))
    async def anime(self, interaction: discord.Interaction) -> None:
        await interaction.response.defer(ephemeral=False, thinking=True)
        author = interaction.user.id

        user = await self.bot.db.fetch("SELECT * FROM user_info WHERE user_id = $1", author)
        if not user:
            await interaction.followup.send("Imagine Trying to play without a profile , Someone needs a memory pill")

        else:
            
            huntk = random.choice(animals)
            print(huntk)
            
            if huntk == None:
                await interaction.followup.send("You found Nothing , Dont Be sad atleast you are alive ")

            else:
                item = await self.bot.db.fetchval("SELECT item_id FROM item_info WHERE item_name = $1", huntk)
                emote = await self.bot.db.fetchval("SELECT emote_id FROM item_info WHERE item_name = $1", huntk)
                
                await self.bot.db.execute("INSERT INTO user_inventory (user_id,item_id,count,emote) VALUES($1,$2,$3,$4) ON CONFLICT (user_id,item_id) DO UPDATE SET count = user_inventory.count + 1",author,item,1,emote)
                embed = discord.Embed(colour = 000000,description=f"Congratulation You got A {huntk} {emote}")
                await interaction.followup.send(embed=embed)


    @anime.error
    async def on_hunt_error(self,interaction: discord.Interaction, error: app_commands.AppCommandError):
        await interaction.response.defer(ephemeral=False, thinking=True)
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.followup.send("command is on 30 second cooldown Try again later")


# end
async def setup(bot) -> None:
    await bot.add_cog(play(bot))
