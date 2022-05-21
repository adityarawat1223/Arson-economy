from http import client
import discord
from discord.ext import commands
import asyncio
import os
import asyncpg
from asyncpg import create_pool
from utilis.sql import create_tables



class myBot(commands.Bot):

    def __init__(self):
        super().__init__(
        command_prefix =commands.when_mentioned_or ("Arson"),case_insensitive=False,activity = discord.Streaming(name='arson help', url='https://www.twitch.tv/burstingfire355'),
            intents=discord.Intents.all(),
            application_id = 975296001273368606,help_command=None )

    #async def startup(self):
        #await bot.wait_until_ready()
        #await bot.tree.sync()  
        #print('Sucessfully synced applications commands')
        #print(f'Connected as {bot.user}')  
       


    
        
        

    async def setup_hook(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                try:
                    await bot.load_extension(f"cogs.{filename[:-3]}")
                    print(f"Loaded {filename}")
                except Exception as e:
                    print(f"Failed to load {filename}")
                    print(f"[ERROR] {e}")

            #await bot.tree.sync()
            #self.loop.create_task(self.startup())
        

     
   
        
 
    async def on_ready(self):
        await self.connect_db()
        print(f'{self.user} has connected to discord!')


    async def connect_db(self):
        self.db = await asyncpg.create_pool(dsn = os.environ["db"],ssl = "require" )
        await create_tables(self.db)
    


            

    
bot = myBot()
async def main():
    async with bot:
        
        

        

        
        
        
        await bot.start(os.environ["eco"])

asyncio.run(main())


        