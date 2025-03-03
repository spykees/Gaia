import os
import nextcord
from nextcord.ext import commands
from lng import translate
from utils.logger import log_command

class Admin(commands.Cog, name="Admin"):
    '''Admin commands'''
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='listmods', help=translate("listmods_help"))
    @commands.has_role(1335846620885024778)
    async def listmods(self, ctx):
        '''List all cogs available'''
        log_command('listmods', ctx.author)
        cogs = [f[:-3] for f in os.listdir('./cogs') if f.endswith('.py')]
        embed = nextcord.Embed(title=translate("available_cogs"), description="\n".join(cogs), color=0x00ff00)
        channel = self.bot.get_channel(int(os.getenv('DEBUG_CHAN')))
        if channel:
            await channel.send(embed=embed)
        else:
            await ctx.send(translate("debug_channel_not_found"))

    @commands.command(name='reload', help=translate("reload_help"))
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, cog: str):
        '''Reload the cog specified with !reload <cog>'''
        try:
            self.bot.reload_extension(f'cogs.{cog}')
            channel = self.bot.get_channel(int(os.getenv('DEBUG_CHAN')))
            if channel:
                await channel.send(translate("cog_reloaded", cog=cog))
            else:
                await ctx.send(translate("debug_channel_not_found"))
        except Exception as e:
            channel = self.bot.get_channel(int(os.getenv('DEBUG_CHAN')))
            if channel:
                await channel.send(translate("error_reloading_cog", cog=cog, error=e))
            else:
                await ctx.send(translate("error_reloading_cog", cog=cog, error=e))

    @commands.command(name="setmodo", help=translate("setmodo_help"))
    @commands.has_permissions(administrator=True)
    async def setmodo(self, ctx, member: nextcord.Member):
        '''Add a member to the moderator role'''
        log_command('setmodo', ctx.author)
        role_id = int(os.getenv('MODO_ID_ROLE'))
        role = ctx.guild.get_role(role_id)
        if role:
            if role in member.roles:
                await ctx.send(translate("already_moderator", user=member.mention))
            else:
                await member.add_roles(role)
                await ctx.send(translate("added_to_moderator", user=member.mention))
        else:
            await ctx.send(translate("moderator_role_not_found"))

    @commands.command(name="unsetmodo", help=translate("unsetmodo_help"))
    @commands.has_permissions(administrator=True)
    async def unsetmodo(self, ctx, member: nextcord.Member):
        log_command('unsetmodo', ctx.author)
        role_id = int(os.getenv('MODO_ID_ROLE'))
        role = ctx.guild.getrole(role_id)
        if role:
            if role in member.roles:
                await member.remove_roles(role)
                await ctx.send(translate('remove_to_moderator', user=member.mention))
            else:
                await ctx.send(translate("not_moderator", user=member.mention))
        else:
            await ctx.send(translate("moderator_role_not_found"))

def setup(bot):
    bot.add_cog(Admin(bot))