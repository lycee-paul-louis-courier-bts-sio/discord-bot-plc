import discord
import os
from discord.ext import commands 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create a Discord client instance and set the command prefix
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

# Set the confirmation message when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
# Set the commands for your bot
@bot.command()
async def bonjour(ctx):
    response = 'Bonjour, je suis Paul Louis Courier !'
    await ctx.send(response)

# Retrieve token from the .env file
bot.run(os.getenv('DISCORD_BOT_TOKEN'))