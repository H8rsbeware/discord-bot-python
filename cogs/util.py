from asyncio.windows_events import NULL
import discord, json, asyncio
from discord.ext import commands
from discord.ext.commands.core import command

class util(commands.Cog):
    def __init__(self, c):
        self.c = c

#CONVERTERS
    #TIME MANAGER
    class DurationConverter(commands.Converter):
        async def convert(self, ctx, argument):
            amount = argument[:-1]
            unit = argument[-1]
            if amount.isdigit() and unit in ['s','m', 'h','d']:
                return(int(amount),unit)
            raise commands.BadArgument(message = "Not a valid duration")

#COMMANDS
    #PING
    @commands.command(aliases=['latency', 'ms'])
    async def ping(self, ctx):
        await ctx.send(f'{round(self.c.latency*1000)}ms')
    #CLEAR
    @commands.command(aliases=['purge', 'c', 'p'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, a : int):
        if a > 0:
            await ctx.channel.purge(limit=a+1)
            await ctx.send(f'{a} messages have been removed.', delete_after=5)
        else:
            await ctx.send(f'{a} is not a valid amount.')
    #KICK
    @commands.command(aliases = ['k', 'boot'])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, m : commands.MemberConverter, *, r=None):
        await m.kick(reason = r)
        if r != None:
            await ctx.send(f'{m} has been kicked from the server for: "{r}".')
        else:
            await ctx.send(f'{m} has been kicked from the server.')
    #BAN
    @commands.command(aliases = ['b'])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, m : commands.MemberConverter, *, r=None):
        await m.ban(reason = r)
        if r != None:
            await ctx.send(f'{m} has been banned from the server for: "{r}".')
        else:
            await ctx.send(f'{m} has been banned from the server.')
    #TEMPBAN
    @commands.command(aliases = ['tb','tempBan'])
    @commands.has_permissions(ban_members=True)
    async def tempban(self, ctx, m : commands.MemberConverter, time: DurationConverter, *, r=None):
        multi = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
        amount, unit = time
        await ctx.guild.ban(m)
        if r != None:
            await ctx.send(f'{m.name} recieved a {amount}{unit} ban from the server for: "{r}".')
        else:
            await ctx.send(f'{m.name} recieved a {amount}{unit} ban from the server.')
        await asyncio.sleep(amount * multi[unit])
        await ctx.guild.unban(m)
    #UNBAN
    @commands.command(aliases = ['ub'])
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, m):
        bans = await ctx.guild.bans()
        name, disc = m.split('#')
        for ban in bans:
            user = ban.user
            if(user.name, user.discriminator) == (name, disc):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.name}#{user.discriminator} has been unbanned.')
                return
    #MUTE
    @commands.command(aliases = ['m'])
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, m : commands.MemberConverter, *, r=None):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, name="Muted")
        if not role:
            role = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(role, speak=False, send_messages=False, add_reactions = False)
        embed = discord.Embed(description= f"Muted {m.name}", color = discord.Colour.blue())
        if r != None:
            embed.add_field(name=f"reason: {r}", inline=False)
        await ctx.send(embed=embed)
        await m.add_roles(role)
    #TEMPMUTE
    @commands.command(aliases=['tm','tempMute'])
    @commands.has_permissions(manage_messages=True)
    async def tempmute(self, ctx, m: commands.MemberConverter, time: DurationConverter, *, r = None):
        multi = {'s':1, 'm':60, 'h':3600, 'd':86400}
        amount, unit = time

        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await m.add_roles(role)
        if r != None:
            await ctx.send(f' Muted {m.name} for {amount}{unit}, reason: "{r}".')
        else:
            await ctx.send(f'Muted {m.name} for {amount}{unit}.')
        await asyncio.sleep(amount*multi[unit])
        await m.remove_roles(role)
    #UNMUTE
    @commands.command(aliases=['um'])
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, m: commands.MemberConverter):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, name="Muted")
        if not role:
            ctx.send(f"A Muted role does not exist, It will automatically be created once the {ctx.prefix}mute command is used for the first time!")
            return
        if role in m.roles:
            embed = discord.Embed(description= f"Unmute {m.name}", color = discord.Colour.blue())
            await ctx.send(embed=embed)
            await m.remove_roles(role)
        else:
            embed = discord.Embed(description= f"{m.name} isnt muted, use {ctx.prefix}mute to mute them.", color = discord.Colour.blue())
            await ctx.send(embed=embed)
    #PREFIX
    @commands.command(aliases=["Prefix","prefix","pfx"])
    @commands.has_permissions(administrator=True)
    async def change_prefix(self, ctx, pfx):
        if pfx != '"' and len(pfx) == 1:
            with open('prefix.json', 'r') as f:
                prefix = json.load(f)
            prefix[str(ctx.guild.id)]=pfx
            with open('prefix.json', 'w') as f:
                json.dump(prefix, f, indent=4)
            await ctx.send(f"Prefix changed to: {pfx}")
        else:
            await ctx.send("Dont try and mess with my files.")
    #USER-INFO
    @commands.command(aliases=["user","info","user-info"])
    @commands.has_permissions(manage_messages=True)
    async def view(self, ctx, m : commands.MemberConverter):
        embed = discord.Embed(title = m.name, description = m.mention, color = discord.Colour.blue())
        embed.add_field(name = "ID", value = m.id, inline = True)
        embed.set_thumbnail(url = m.avatar_url)
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    
    
#ERROR HANDLERS
    @clear.error
    async def clearErr(self,ctx, err):
        if isinstance(err, commands.MissingRequiredArgument) or isinstance(err, commands.BadArgument):
            await ctx.send("Please specify an amount as a valid integer.", delete_after=5)
        if isinstance(err, commands.MissingPermissions):
            await ctx.send("You don't have permissions to use this command.", delete_after=5)
    
    @tempban.error
    async def tempBanErr(self,ctx, err):
        if isinstance(err, commands.MissingRequiredArgument) or isinstance(err, commands.BadArgument):
            await ctx.send("Please mention a member.", delete_after=5)
        if isinstance(err, commands.MissingPermissions):
            await ctx.send("You don't have permissions to use this command.", delete_after=5)
    
    @kick.error
    async def kickErr(self,ctx, err):
        if isinstance(err, commands.MissingRequiredArgument) or isinstance(err, commands.BadArgument):
            await ctx.send("Please mention a member.", delete_after=5)
        if isinstance(err, commands.MissingPermissions):
            await ctx.send("You don't have permissions to use this command.", delete_after=5)
    
    
    @ban.error
    async def banErr(self,ctx, err):
        if isinstance(err, commands.MissingRequiredArgument) or isinstance(err, commands.BadArgument):
            await ctx.send("Please mention a member.", delete_after=5)
        if isinstance(err, commands.MissingPermissions):
            await ctx.send("You don't have permissions to use this command.", delete_after=5)
    
    
    @unban.error
    async def unbanErr(self,ctx, err):
        if isinstance(err, commands.MissingRequiredArgument) or isinstance(err, commands.BadArgument):
            await ctx.send("Please mention a member.", delete_after=5)
        if isinstance(err, commands.MissingPermissions):
            await ctx.send("You don't have permissions to use this command.", delete_after=5)
    
    @mute.error
    async def muteErr(self, ctx, err):
        if isinstance(err, commands.MissingPermissions):
            await ctx.send("You don't have permissions to use this command.", delete_after=5)
        if isinstance(err, commands.MissingRequiredArgument) or isinstance(err, commands.BadArgument):
            await ctx.send("Please mention a member.", delete_after=5) 
    
    @tempmute.error
    async def tempmuteErr(self,ctx, err):
        if isinstance(err, commands.MissingRequiredArgument) or isinstance(err, commands.BadArgument):
            await ctx.send("Please mention a member.", delete_after=5)
        if isinstance(err, commands.MissingPermissions):
            await ctx.send("You don't have permissions to use this command.", delete_after=5)
        
    @unmute.error
    async def unmuteErr(self, ctx, err):
        if isinstance(err, commands.MissingPermissions):
            await ctx.send("You don't have permissions to use this command.", delete_after=5)
        if isinstance(err, commands.MissingRequiredArgument) or isinstance(err, commands.BadArgument):
            await ctx.send("Please mention a member.", delete_after=5)              
    
    @change_prefix.error
    async def pfxErr(self,ctx, err):
        if isinstance(err, commands.MissingPermissions):
            await ctx.send("You don't have permissions to use this command.", delete_after=5)

    @view.error
    async def viewErr(self, ctx, err):
        if isinstance(err, commands.MissingPermissions):
            await ctx.send("You don't have permissions to use this command.", delete_after=5)


def setup(c):
    c.add_cog(util(c))


