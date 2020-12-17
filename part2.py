import discord
from discord.ext import commands
import random
import asyncio

bot = commands.Bot(command_prefix="?")
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Bot is now online!")

answers = ["Yes", "No", "Maybe", "maybe not", "Probably", "Probably not"]


@bot.command(pass_context=True)
async def help(ctx):
    await ctx.send("Help\r\n"
                   "?help - shows all commands\r\n"
                   "?hello - greeats you")

@bot.command(pass_context=True)
async def hello(ctx):
    await ctx.send(f"Hey {ctx.message.author.name}!")

@bot.command(pass_context=True)
async def eightball(ctx, *, arg):
    msg = await ctx.send(f"You asked me: {arg}")
    await asyncio.sleep(2)
    await msg.edit(content="Contacting the oracle...")
    await asyncio.sleep(2)
    await msg.edit(content=f"I think the answer is: {random.choice(answers)}")








bot.run("token")
