import discord
import json
from main import meeting_id
import datetime
from discord.ext import commands


class Schedule(commands.Cog):
    def __init__(self, client):
        self.client = client

    meeting_id=meeting_id

    @commands.command()
    async def full(self, ctx):
        embed = discord.Embed(title="Full Day Schedule", color=discord.Color.purple())
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/733664773744492587/818474097439670282/Screen_Shot_2021-03-08_at_8.23.38_AM.png")
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author.name}')
        await ctx.send(embed=embed)

    @commands.command()
    async def half(self, ctx):
        embed = discord.Embed(title="Half Day Schedule",
                              description="Period 1: 7:57 AM - 8:20 AM\nPeriod 2: 8:22 AM - 8:45 AM\nPeriod 3: 8:47 AM - 9:10 AM\nPeriod 4: 9:12 AM - 9:35 AM\nPeriod 5: 9:37 AM - 10:00 AM\nPeriod 6: 10:02 AM - 10:25 AM\nPeriod 7: 10:27 AM- 10:50 AM\nPeriod 8: 10:52 AM - 11:15 AM\nPeriod 9: 11:17 AM - 11:40 AM",
                              color=discord.Color.red())
        embed.set_footer(icon_url=ctx.author.avatar_url,
                         text=f'Requested by {ctx.author.name}')
        await ctx.send(embed=embed)

    @commands.command()
    async def study_meet(self, ctx, *, input_des):
        global meeting_id
        str=""
        places=[]
        for s in input_des.split(','):
            if s.startswith(' '):
                places.append(s.lstrip(' '))
            else:
                places.append(s)
        with open("meeting_info.json", "r") as f:
            james = json.load(f)
        james[meeting_id] = {"Date": places[0],
                             "Time": places[1],
                             "Place": places[2],
                             "Meeting ID": meeting_id}
        with open("meeting_info.json", "w") as f:
            json.dump(james, f, indent=2)
        for x in james[meeting_id]:
            str+=f"{x}: {james[meeting_id][x]}\n"
        embed = discord.Embed(title="Study Meet Up",
                              description=str,
                              color=discord.Color.blue())
        embed.set_footer(icon_url=ctx.author.avatar_url,
                         text=f'Requested by {ctx.author.name}')
        await ctx.send(embed=embed)
        meeting_id += 1

def setup(client):
    client.add_cog(Schedule(client))
