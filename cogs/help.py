import discord, json
from discord.ext import commands



class help(commands.Cog):
    def __init__(self, c):
        self.c = c
    
#HELP ROOT
    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(title = "Help", description = f"Use {ctx.prefix}help <command> for more info.", color = discord.Colour.gold())
        em.add_field(name = "Utility", value="ping, clear, kick, ban, tempban, unban, prefix, view")
        em.add_field(name = "Fun", value="_8ball, avatar")
        em.add_field(name = "Bot Control", value="load, unload, reload, shutdown")
        await ctx.send(embed = em)
#UTILITY
    #KICK
    @help.command()
    async def kick(self, ctx):
        em = discord.Embed(title="**Kick**", description = "Kicks a specified member from the server", color = discord.Colour.gold())
        em.add_field(name= "*Syntax*", value=f"{ctx.prefix}kick <member> [reason]")
        em.add_field(name= "**Aliases**", value = "kick, boot, k" )
        em.set_footer(text="•<member> can be inputed as a mention, id, name and discriminator, or nickname")
        await ctx.send(embed = em)
    #BAN
    @help.command()
    async def ban(self, ctx):
        em = discord.Embed(title="**Ban**", description = "Bans a specified member from the server", color = discord.Colour.gold())
        em.add_field(name="**Syntax**", value=f"{ctx.prefix}ban <member> [reason]")
        em.add_field(name="**Aliases**", value = "ban, b")
        em.set_footer(text="•<member> can be inputed as a mention, id, name and discriminator, or nickname")
        await ctx.send(embed = em)
    #TEMPBAN
    @help.command()
    async def tempban(self, ctx):
        em = discord.Embed(title="**Temp Ban**", description = "Bans a member from the server for a specified amount of time (in s/m/h/d)", color = discord.Colour.gold())
        em.add_field(name="**Syntax**", value=f"{ctx.prefix}tempban <member> <duration> [reason]")
        em.add_field(name="**Aliases**", value = "tempban, tb, tempBan")
        em.set_footer(text="•<member> can be inputed as a mention, id, name and discriminator, or nickname")
        await ctx.send(embed = em)
    #UNBAN
    @help.command()
    async def unban(self, ctx):
        em = discord.Embed(title="**Unban**", description = "Unbans a specified member from the server", color = discord.Colour.gold())
        em.add_field(name="**Syntax**", value=f"{ctx.prefix}unban <member>")
        em.add_field(name="**Aliases**", value = "unban, ub")
        em.set_footer(text="•<member> can be inputed as a mention, id, name and discriminator, or nickname")
        await ctx.send(embed = em)
    #VIEW
    @help.command()
    async def view(self, ctx):
        em = discord.Embed(title="**View**", description = "Views extra information on a specified member", color = discord.Colour.gold())
        em.add_field(name="**Syntax**", value=f"{ctx.prefix}view <member>")
        em.add_field(name="**Aliases**", value = "view, user-info, user, info")
        em.set_footer(text="•<member> can be inputed as a mention, id, name and discriminator, or nickname")
        await ctx.send(embed = em)
    #CLEAR
    @help.command()
    async def clear(self, ctx):
        em = discord.Embed(title="**Clear**", description = "Clears a specified amount of messages", color = discord.Colour.gold())
        em.add_field(name="**Syntax**", value=f"{ctx.prefix}clear <amount>")
        em.add_field(name="**Aliases**", value = "clear, purge, c, p")
        await ctx.send(embed = em)
    #PING
    @help.command()
    async def ping(self, ctx):
        em = discord.Embed(title="**Ping**", description = "Returns the bot latency", color = discord.Colour.gold())
        em.add_field(name="**Syntax**", value=f"{ctx.prefix}ping")
        em.add_field(name="**Aliases**", value = "ping, latency, ms")
        await ctx.send(embed = em)        
#FUN
    #_8BALL
    @help.command()
    async def _8ball(self, ctx):
        em = discord.Embed(title="**8 Ball**", description = "Returns a random reply to a question", color = discord.Colour.gold())
        em.add_field(name="**Syntax**", value=f"{ctx.prefix}_8ball <question>")
        em.add_field(name="**Aliases**", value = "_8ball, 8ball, 8")
        await ctx.send(embed = em)    
    #Avatar
    @help.command()
    async def avatar(self, ctx):
        em = discord.Embed(title="**Avatar**", description = "Gets the avatar of you or a member", color = discord.Colour.gold())
        em.add_field(name="**Syntax**", value=f"{ctx.prefix}avatar [member]")
        em.add_field(name="**Aliases**", value = "avatar, av")
        await ctx.send(embed = em)
#AWAKE/OWNER ONLY
    #LOAD
    @help.command()
    async def load(self, ctx):
        em = discord.Embed(title="**Load**", description = "Loads a python cog file to allow use", color = discord.Colour.gold())
        em.add_field(name="**Syntax**", value=f"{ctx.prefix}load <cog>")
        em.set_footer(text="•Bot Controls can only be used by the H8rs#8504")
        await ctx.send(embed = em)
    #UNLOAD
    @help.command()
    async def unload(self, ctx):
        em = discord.Embed(title="**Unload**", description = "Unloads a python cog file, disabling it", color = discord.Colour.gold())
        em.add_field(name="**Syntax**", value=f"{ctx.prefix}unload <cog>")
        em.set_footer(text="•Bot Controls can only be used by the H8rs#8504")
        await ctx.send(embed = em)       
    #RELOAD
    @help.command()
    async def reload(self, ctx):
        em = discord.Embed(title="**Reload**", description = "Reloads a python cog file, allowing it to update", color = discord.Colour.gold())
        em.add_field(name="**Syntax**", value=f"{ctx.prefix}reload <cog>")
        em.set_footer(text="•Bot Controls can only be used by the H8rs#8504")
        await ctx.send(embed = em)
    #SHUTDOWN
    @help.command()
    async def shutdown(self, ctx):
        em = discord.Embed(title="**Shutdown**", description = "Pulls the plug on the bot, entirely", color = discord.Colour.gold())
        em.add_field(name="**Syntax**", value=f"{ctx.prefix}shutdown <cog>")
        em.set_footer(text="•Bot Controls can only be used by the H8rs#8504")
        await ctx.send(embed = em)
def setup(c):
    c.add_cog(help(c))