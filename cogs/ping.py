from nextcord.ext import commands

class Ping(commands.Cog, name = "Ping"):
    ''' Recevive ping command ans respond with pong'''
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        '''Bot respond with Pong !'''
        await ctx.send("Pong")
    
def setup(bot: commands.Bot):
    bot.add_cog(Ping(bot))