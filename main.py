import os
from datetime import datetime
import asyncio
from dotenv import load_dotenv

import nextcord
from nextcord.ext import commands
from lng import translate

last_triggered = {}

load_dotenv()

intents = nextcord.Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents, description=translate("bot_description"))

@bot.event
async def on_ready():
    print(f"{bot.user.name}{translate('has connected')}")

# Load all cogs in ./cogs folder if files end with .py and print "nameofthefile" (without .py) is loaded
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        cog_name = filename[:-3]
        bot.load_extension(f'cogs.{cog_name}')
        print(f'{cog_name} {translate("is loaded")}')

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
        await ctx.channel.send(translate("greeting", user=ctx.author.mention))
        last_triggered[user_id] = current_time  # Update the last triggered time
    
    await bot.process_commands(ctx)  # Allow the bot to process other commands

@bot.event
async def on_member_join(member):
    channel_id = os.getenv('WELCOME_CHANNEL_ID')  # Ensure you have set this in your .env file
    channel = bot.get_channel(int(channel_id))
    if channel:
        await channel.send(translate("greeting", user=member.mention))

bot.run(os.getenv('TOKEN'))