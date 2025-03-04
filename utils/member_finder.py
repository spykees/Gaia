import nextcord

async def find_member(ctx, name):
    member = None
    if name.isdigit():
        member = ctx.guild.get_member(int(name))
    if not member:
        member = nextcord.utils.get(ctx.guild.members, name=name)
    if not member:
        member = nextcord.utils.get(ctx.guild.members, display_name=name)
    if not member:
        member = nextcord.utils.get(ctx.guild.members, nick=name)
    return member
