import random
import requests
import discord
from discord.ext import commands
import os

intents = discord.Intents.all()

Bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

#/echo hello

@Bot.command()
async def echo(ctx, *args) :
    m_args = " ".join(args)
    await ctx.send(m_args)
#/Hello

token = ""

with open("token.txt") as file:
    token = file.read()


Bot.run(token)
