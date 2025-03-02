"""
Admin Cog for managing bot extensions.
This cog provides commands for listing and reloading bot extensions (cogs).
It includes the following commands:
- listmods: Lists all available cogs in the 'cogs' directory.
- reload: Reloads a specified cog.
Classes:
    Admin: A class that contains commands for managing bot extensions.
Methods:
    __init__(self, bot): Initializes the Admin cog with the bot instance.
    listmods(self, ctx): Lists all available cogs and sends the list to the debug channel or the invoking context.
    reload(self, ctx, cog: str): Reloads the specified cog and sends a success or error message to the debug channel or the invoking context.
Attributes:
    bot: The bot instance that the cog is attached to.
"""

import os

import nextcord
from nextcord.ext import commands

class Admin(commands.Cog, name="Admin"):
    '''Admin commands'''
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='listmods')
    @commands.has_role(1335846620885024778)
    async def listmods(self, ctx):
        '''List all cogs available'''
        cogs = [f[:-3] for f in os.listdir('./cogs') if f.endswith('.py')]
        embed = nextcord.Embed(title="Available Cogs", description="\n".join(cogs), color=0x00ff00)
        channel = self.bot.get_channel(int(os.getenv('DEBUG_CHAN')))
        if channel:
            await channel.send(embed=embed)
        else:
            await ctx.send("Debug channel not found.")

    @commands.command(name='reload')
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, cog: str):
        '''Reload the cog specified with !reload <cog>'''
        try:
            self.bot.reload_extension(f'cogs.{cog}')
            channel = self.bot.get_channel(int(os.getenv('DEBUG_CHAN')))
            if channel:
                await channel.send(f'Cog {cog} reloaded successfully.')
            else:
                await ctx.send("Debug channel not found.")
        except Exception as e:
            channel = self.bot.get_channel(int(os.getenv('DEBUG_CHAN')))
            if channel:
                await channel.send(f'Error reloading cog {cog}: {e}')
            else:
                await ctx.send(f'Error reloading cog {cog}: {e}')

def setup(bot):
    bot.add_cog(Admin(bot))