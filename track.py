import discord
import math
from discord.ext import commands, tasks


class Tracks(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def math(self, ctx):
        embed = discord.Embed(title="Math/Computer Science Track",
                              description="AP Calculus BC\nAP Computer Science A\nCalculus III\nAP Statistics\nAP Physics C",
                              color=discord.Color.blue())
        embed.set_image(
            url="https://www.openaccessgovernment.org/wp-content/uploads/2020/08/dreamstime_l_124110584.jpg")
        await ctx.send(embed=embed)

    @commands.command()
    async def life(self, ctx):
        embed = discord.Embed(title="Life Science",
                              description="AP Calculus AB\nAP Biology\nAP Chemistry\nHuman Anatomy\nAP Statistics",
                              color=discord.Color.green())
        embed.set_image(url="https://home.edweb.net/wp-content/uploads/20180226-science-event.jpg")
        await ctx.send(embed=embed)

    @commands.command()
    async def engineering(self, ctx):
        embed = discord.Embed(title="Engineering",
                              description="AP Calculus BC\nCalculus III\nApplied Engineering\nAP Physics C\nAP Chemistry/Waves and Modern Physics",
                              color=discord.Color.light_grey())
        embed.set_image(
            url="https://gps.uml.edu/images/2015/programs/online-mechanical-engineering-technology-bachelor-image.jpg")
        await ctx.send(embed=embed)

    @commands.command()
    async def contact_advisors(self, ctx):
        embed = discord.Embed(title="Emails of STEM Advisors",
                              description="email of both, i'm too lazy to find it now",
                              color=discord.Color.default())
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Tracks(client))
