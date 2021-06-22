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

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

# Second Test prints data from cmtest (Now need to export to discord)

    
result = subprocess.run(["python", "cmtest.py"], capture_output=True, encoding='UTF-8')

cmc = result.stdout

print(cmc)


@bot.command(name='awf', help='Responds with CMC data for $AWF')
async def cmc_data(ctx):
    awf = cmc    

    response = random.choice(cmc)
    await ctx.send(response)


bot.run(TOKEN)
