token = "not gonna work"

import discord, os, json
from discord.ext import commands


def get_prefix(c, message):
    with open('prefix.json', 'r') as f:
        prefix = json.load(f)
        
    return prefix[str(message.guild.id)]

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
c = commands.Bot(command_prefix = get_prefix, intents = intents)
c.remove_command("help")

@c.command(aliases=['l'])
@commands.has_permissions(administrator=True)
async def load(ctx, e):
    c.load_extension(f'cogs.{e}')
    await ctx.send(f"loaded {e}.py", delete_after=5)
@load.error
async def loadErr(ctx, err):
    if isinstance(err, commands.MissingRequiredArgument) or isinstance(err, commands.BadArgument):
        await ctx.send("Please specify a file.", delete_after=5)
    if isinstance(err, commands.MissingPermissions):
        await ctx.send("You don't have permissions to use this command.", delete_after=5)


@c.command(aliases=['ul'])
@commands.has_permissions(administrator=True)
async def unload(ctx, e):
    c.unload_extension(f'cogs.{e}')
    await ctx.send(f"unloaded {e}.py", delete_after=5)
@unload.error
async def unloadErr(ctx, err):
    if isinstance(err, commands.MissingRequiredArgument) or isinstance(err, commands.BadArgument):
        await ctx.send("Please specify a file.", delete_after=5)
    if isinstance(err, commands.MissingPermissions):
        await ctx.send("You don't have permissions to use this command.", delete_after=5)


@c.command(aliases = ['update','rl'])
@commands.has_permissions(administrator=True)
async def reload(ctx, e):
    c.unload_extension(f'cogs.{e}')
    c.load_extension(f'cogs.{e}')
    await ctx.send(f"reloaded {e}.py", delete_after=5)
@reload.error
async def reloadErr(ctx, err):
    if isinstance(err, commands.MissingRequiredArgument) or isinstance(err, commands.BadArgument):
        await ctx.send("Please specify a file.", delete_after=5)
    if isinstance(err, commands.MissingPermissions):
        await ctx.send("You don't have permissions to use this command.", delete_after=5)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        c.load_extension(f'cogs.{filename[:-3]}')

def meCheck(ctx):
    return ctx.author.id == 462267885042139156 or ctx.author.id == 709460152486723665

@c.command()
@commands.check(meCheck)
async def shutdown(ctx):
    await ctx.bot.logout()
@shutdown.error
async def shutdownErr(ctx, err):
    if isinstance(err, commands.CheckFailure):
        await ctx.send("You don't have permissions to use this command.")

c.run(token)
