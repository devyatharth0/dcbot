import discord
from discord.ext import commands

BANNED_WORDS = ["boobs", "ass", "dick"]

class MessageFilter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        for word in BANNED_WORDS:
            if word in message.content.lower():
                await message.delete()
                await message.channel.send(f"🚫 **{message.author.mention}**, your message contained banned words!")
                return

async def setup(bot):
    await bot.add_cog(MessageFilter(bot))
