"""
moderator.py
This module contains the Moderator cog for handling moderation commands in a Discord bot using the nextcord library.
Classes:
    Moderator(commands.Cog): A class that defines moderation commands such as kick and ban.
Functions:
    setup(bot): A function that adds the Moderator cog to the bot.
Moderator class:
    Methods:
        __init__(self, bot): Initializes the Moderator cog with the bot instance.
        kick(self, ctx, member: commands.MemberConverter, *, reason=None): Kicks a member from the server with an optional reason.
        ban(self, ctx, member: commands.MemberConverter, *, reason=None): Bans a member from the server with an optional reason.
Usage:
    - !kick username reason: Kicks the specified user with an optional reason.
    - !ban username reason: Bans the specified user with an optional reason.
"""

from nextcord.ext import commands

class Moderator(commands.Cog, name="Moderation"):
    '''Moderation commands'''
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: commands.MemberConverter, *, reason=None):
        '''Usage !kick username reason. Reason is optional'''
        await member.kick(reason=reason)
        await ctx.send(f'{member} has been kicked for {reason}')

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: commands.MemberConverter, *, reason=None):
        '''Usage !ban username reason. Reason is optional'''
        await member.ban(reason=reason)
        await ctx.send(f'{member} has been banned for {reason}')

def setup(bot):
    bot.add_cog(Moderator(bot))