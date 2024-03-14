import discord
from discord.ext import commands
import os
import asyncio

from help_cog import help_cog
from music_cog import music_cog

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all(), help_command=None)

# bot.remove_command("help")

# bot.add_cog(help_cog(bot))
# bot.add_cog(music_cog(bot))

# bot.run(os.getenv("TOKEN"))

async def main():
    async with bot:
        await bot.add_cog(help_cog(bot))
        await bot.add_cog(music_cog(bot))
        await bot.start(os.getenv("TOKEN"))

asyncio.run(main())


