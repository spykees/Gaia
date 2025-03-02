import os
from datetime import datetime
import asyncio
from dotenv import load_dotenv

import nextcord
from nextcord.ext import commands

last_triggered = {}
last_ping = {}
load_dotenv()


intents = nextcord.Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
        print(f"{bot.user.name} has connected")

for folder in os.listdir("modules"):
     if os.path.exists(os.path.join("modules", folder, "cog.py")):
          bot.load_extension(f"modules.{folder}.cog")

@bot.event
async def on_message(ctx):
    user_id = ctx.author.id
    current_time = datetime.now()

    # Check if the user has triggered the bot recently
    if user_id in last_triggered:
        time_since_last_trigger = (current_time - last_triggered[user_id]).total_seconds()
        if time_since_last_trigger < 60:
            return  # Ignore the message if it was sent within the last 60 seconds

    if ctx.content.startswith(("hello", "Hello", "coucou", "Coucou", "salut", "Salut")):
        await ctx.channel.send(f"Coucou {ctx.author.mention}")
        last_triggered[user_id] = current_time  # Update the last triggered time
    
    await bot.process_commands(ctx) # Allow the bot to process other commands



bot.run(os.getenv('TOKEN'))