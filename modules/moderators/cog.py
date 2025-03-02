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