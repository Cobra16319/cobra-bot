# bot.py
import os
import random
# Testing new sub-processes
import subprocess
# Testing grabbing output
import sys

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')



# Second Test prints data from cmtest (Now need to export to discord)

    
result = subprocess.run(["python", "cmtest.py"], capture_output=True, encoding='UTF-8')

cmc = result.stdout

@bot.command(name='awf', help='Responds with CMC data for $AWF')
async def cmc_data(ctx):
    awf = cmc    
    await ctx.send(cmc)


bot.run(TOKEN)
