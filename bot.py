import os

import discord
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_NAME')
FRIDAY_CHANNEL_ID = os.getenv('FRIDAY_CHANNEL_ID')
TESTING = os.getenv('TESTING')

intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
        print(f'{client.user} has connected to Discord!')
        await happy_friday()

async def is_it_friday():
        dt = datetime.now()
        day_of_week = dt.weekday()
        return day_of_week

async def get_guild():
        for guild in client.guilds:
                if guild.name == GUILD:
                        return guild
                        break

async def happy_friday():
        guild = await get_guild()
        if await is_it_friday() == 4:
             friday_channel = await guild.fetch_channel(FRIDAY_CHANNEL_ID)  
             await friday_channel.send(content='@everyone happy friday', file=discord.File('fridaynight.gif'))

client.run(TOKEN)

