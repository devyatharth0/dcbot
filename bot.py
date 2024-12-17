import discord
from discord.ext import commands
import os
from config import BOT_TOKEN

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ {bot.user.name} has connected to Discord!")

async def load_functions():
    for filename in os.listdir("./functions"):
        if filename.endswith(".py"):
            await bot.load_extension(f"functions.{filename[:-3]}")
            print(f"🔹 Loaded function: {filename}")

async def main():
    async with bot:
        await load_functions()
        await bot.start(BOT_TOKEN)

import asyncio
asyncio.run(main())
