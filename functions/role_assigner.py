import discord
from discord.ext import commands

class RoleAssigner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="role")
    async def role(self, ctx, role_name: str):
        role = discord.utils.get(ctx.guild.roles, name=role_name)

        if role:
            try:
                await ctx.author.add_roles(role)
                await ctx.send(f"✅ **{ctx.author.mention}**, you have been assigned the role **{role.name}**!")
            except discord.Forbidden:
                await ctx.send("❌ I don't have permission to assign roles!")
            except Exception as e:
                await ctx.send("❌ Something went wrong!")
                print(f"Role Error: {e}")
        else:
            await ctx.send("❌ Role not found. Please check the role name!")

async def setup(bot):
    await bot.add_cog(RoleAssigner(bot))
