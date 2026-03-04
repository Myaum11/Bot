import discord
from discord.ext import commamds
from discord import app_commands

from myserver import server_on

bot = commamds.Bot(commamds_prefix='!', intents=discord.Intents.all()
                   

TOKEN ='MTQ3ODQ3NzAxNDM4NTI5OTQ4Ng.GqfJmz.jUFl3OwdysJWDa-YPMjRRj_rVdLOTN6rYuO4LY





   @bot.Event 
   async def on_ready() 
       print("Bot Online!")
       synced = await bot.tree.sync()
       print(f"{len(synced)} command(s)")           
    