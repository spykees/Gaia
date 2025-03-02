from nextcord.ext import commands
from lng import translate

class Moderator(commands.Cog, name="Moderation"):
    '''Moderation commands'''
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', help=translate("kick_help"))
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: commands.MemberConverter, *, reason=None):
        '''Usage !kick username reason. Reason is optional'''
        await member.kick(reason=reason)
        await ctx.send(translate("kick_message", member=member, reason=reason))

    @commands.command(name="ban", help=translate("ban_help"))
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: commands.MemberConverter, *, reason=None):
        '''Usage !ban username reason. Reason is optional'''
        await member.ban(reason=reason)
        await ctx.send(translate("ban_message", member=member, reason=reason))

def setup(bot):
    bot.add_cog(Moderator(bot))