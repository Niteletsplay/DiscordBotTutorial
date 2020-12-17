import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="?") # replace >?< with the prefix you want
bot.remove_command("help")














bot.run("token") # replace >token< with your bots token
