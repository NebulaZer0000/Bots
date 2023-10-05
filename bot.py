import random
import discord
from discord.ext import commands
import requests

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

@Bot.command()
async def pokemon(ctx):
    ranpoke = random.randint(1, 905)
    url = "https://pokeapi.co/api/v2/pokemon/"
    secs = 30
    
    try:
        r = requests.get(f"{url}{ranpoke}")
        packages_json = r.json()
        packages_json.keys

        napo = packages_json["name"]

        embed = discord.Embed(title = "Who's that pokemon?!", color = discord.Color.random())
        embed.set_image(url = f"https://play.pokemonshowdown.com/sprites/ani/{napo}.gif")
        await ctx.send(embed = embed)

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        user_ans = await Bot.wait_for("message", check=check)


        if user_ans.content == napo:
            await ctx.send("You are correct! :)")
        elif user_ans.content != napo:
            await ctx.send(f"You are incorrect :v The answer is {napo}")


    except:
        await ctx.send("bruh")

Bot.run(token)
