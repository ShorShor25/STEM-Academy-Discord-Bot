import discord
import json
import os
from discord.ext import commands, tasks

client = commands.Bot(command_prefix=".")
meeting_id=0

@client.event
async def on_ready():
    # reminder.start()
    # await client.change_presence(status=discord.Status.online, activity=discord.activity("School in Session"))
    print("Bot is ready.")

# @client.command()
# async def clear(ctx,amount=5):
#   await ctx.channel.purge(limit=amount)

# @tasks.loop(minutes=1)
# async def reminder(self, ctx):
#     await ctx.send("Have you finished with those errands?")

@client.command()
async def load(ctx, extension):
  client.load_extension(f"cogs.{extension}")
  await ctx.send(f"{extension} has been loaded.")

@client.command()
async def unload(ctx, extension):
  client.unload_extension(f"cogs.{extension}")
  await ctx.send(f"{extension} has been unloaded")

@client.command()
async def reload(ctx, extension):
  client.unload_extension(f"cogs.{extension}")
  client.load_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    client.load_extension(f"cogs.{filename[:-3]}")

client.run("Nzk1MTM1MzE3NTA0OTUwMjgy.X_E9eA.kebpgRJkse5nsLkxEcSvJv2a5_Q")
