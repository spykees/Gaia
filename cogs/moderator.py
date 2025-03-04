import nextcord
from nextcord.ext import commands
from utils.lng import translate
from utils.logger import log_command
from utils.member_finder import find_member

class Moderator(commands.Cog, name="Moderation"):
    '''Moderation commands'''
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', help=translate("kick_help"))
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, name: str, *, reason=None):
        '''Usage !kick username reason. Reason is optional'''
        member = await find_member(ctx, name)
        if not member:
            await ctx.send(translate("member_not_found"))
            return
        log_command('kick', ctx.author, target=member, reason=reason)
        #await member.kick(reason=reason)
        if reason:
            await ctx.send(translate("kick_message", member=member, reason=reason))
        else:
            await ctx.send(translate("kick_message_no_reason", member=member))

    @commands.command(name="ban", help=translate("ban_help"))
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, name: str, *, reason=None):
        '''Usage !ban username reason. Reason is optional'''
        member = await find_member(ctx, name)
        if not member:
            await ctx.send(translate("member_not_found"))
            return
        log_command('ban', ctx.author, target=member, reason=reason)
        #await member.ban(reason=reason)
        if reason:
            await ctx.send(translate("ban_message", member=member, reason=reason))
        else:
            await ctx.send(translate("ban_message_no_reason", member=member))

def setup(bot):
    bot.add_cog(Moderator(bot))