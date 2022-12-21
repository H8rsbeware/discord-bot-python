from asyncio.windows_events import NULL
import discord, random 
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument

class fun(commands.Cog):
    def __init__(self, c):
        self.c = c
    
    @commands.command(aliases=['8ball','8'])
    async def _8ball(self, ctx, *, q):
        res = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.",
                "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", 
                "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
        await ctx.send(f'Question: {q}\nAnswer: {random.choice(res)}')
    
    @commands.command(aliases=['av'])
    async def avatar(self, ctx, *, m : commands.MemberConverter = NULL):
        if m == NULL:
            m = ctx.author

        embed = discord.Embed(title = f"{m.name}'s Avatar", color = discord.Colour.blue())
        embed.set_image(url = m.avatar_url)
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    
    @_8ball.error
    async def _8ballErr(self, ctx, err):
        if isinstance(err, commands.MissingRequiredArgument):
            await ctx.send("A question is required for the 8ball command.",delete_after=5)


def setup(c):
    c.add_cog(fun(c))