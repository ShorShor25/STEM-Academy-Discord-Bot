import discord
import json
from main import client
from discord.ext import commands


class Classes(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def studies(self, ctx):
        embed = discord.Embed(title="Program of Studies",
                              description="An access to the program of studies of 2020 - 2021.\nhttps://4.files.edl.io/dedc/02/24/21/161712-961cc860-cace-4ad6-b600-3a8501653ad6.pdf",
                              color=discord.Color.blue())
        embed.set_image(url="https://hs.pequannock.org/ourpages/auto/2018/1/5/49127649/books.jpg")
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author.name}')

        await ctx.send(embed=embed)

    @commands.command()
    async def hw_help(self, ctx, *, input_problem): #problem; assignment; channel
        hw_information=[]
        for s in input_problem.split(';'):
            if s.startswith(' '):
                hw_information.append(s.lstrip(' '))
            else:
                hw_information.append(s)

        if(not len(hw_information)==3):
            await ctx.send("Not the correct number of arguments.")
            return

        with open("class_channels.json", "r") as f:
            get_ID=json.load(f)
        channel_id=hw_information[2][2:-1]

        try:
            channel = client.get_channel(int(channel_id))
        except:
            await ctx.send("Not a class related channel!!!")
            return

        if(channel.name=="general"):
            await ctx.send("PLease don't ask help in general :pray: .")
            return

        embed = discord.Embed(title = f'{get_ID[channel_id]}\n{hw_information[1]}',
                              description=f'{hw_information[0]}',
                              color=discord.Color.dark_red())
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author.name}')
        await channel.send(embed=embed)

def setup(client):
    client.add_cog(Classes(client))