import discord, json
from discord import activity
from discord.ext import commands, tasks
from itertools import cycle

status = cycle(['Blackjack with Satan', 'Tuber simulator with Pewdiepie', 'Guess who with Marshmello', 'Minecraft by myself', 'Snooker with God', 'Russian Roulette with Putin', 'Monopoly with Trump', 'Battleships with Britian', 'Cops and Robbers with America', 'Hide and Seek with the Mexican Cartel', 'Tag with Police dogs'])

class awake(commands.Cog):
    def __init__(self, c):
        self.c = c

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open('prefix.json', 'r') as f:
            prefix = json.load(f)
        prefix[str(guild.id)]='.'
        with open('prefix.json', 'w') as f:
            json.dump(prefix, f, indent=4)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open('prefix.json', 'r') as f:
            prefix = json.load(f)
        prefix.pop(str(guild.id))
        with open('prefix.json', 'w') as f:
            json.dump(prefix, f, indent=4)

    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()
        await self.c.change_presence(status=discord.Status.dnd)
        print('Python Bot Online')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has showed up!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left us')

    @tasks.loop(seconds=600)
    async def change_status(self):
        await self.c.change_presence(activity=discord.Game(next(status)))

def setup(c):
    c.add_cog(awake(c))
