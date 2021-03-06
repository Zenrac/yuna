import discord
from discord.ext import commands
import nekos
import aiohttp

class Anime():
    """These commands work with nekos.life api."""
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['animesearch'])
    async def anime(self, ctx, *, query=None):
        """Search for anime"""
        if not query:
            await ctx.send(f"{ctx.tick(False)} You need to specify what anime you want to search for!")
        else:
            try:
                async with aiohttp.ClientSession(headers={'content-type': 'application/json'}) as s:
                    q = query.replace(" ", "+")
                    async with s.get(f"https://kitsu.io/api/edge/anime?page[limit]=1&filter[text]={q}") as r:
                        s.close()
                        resp = await r.json()
                        syn = str(resp['data'][0]['attributes']['synopsis'])
                        e = discord.Embed(title=resp['data'][0]['attributes']['titles']['en'], colour=0xff9f68, description=f"{syn[:-180]}...")
                        e.set_author(name="Anime Search", icon_url="https://lh3.googleusercontent.com/fJbHIg6QrqzVD18nUvHXDHA-l3X9FVz5qUNhESnKKRdCspaUnXt4L83eD7nnWZZyzw")
                        #e.add_field(name="Synopsis:", value=f"{syn[:-90]}...")
                        try:
                            e.add_field(name="Rated:", value=f"{resp['data'][0]['attributes']['ageRating']} ({resp['data'][0]['attributes']['ageRatingGuide']})")
                        except:
                            pass
                        try:
                            e.add_field(name="Episodes:", value=resp['data'][0]['attributes']['episodeCount'])
                        except:
                            pass
                        e.add_field(name="Aired:", value=resp['data'][0]['attributes']['startDate'])
                        try:
                            e.set_thumbnail(url=resp['data'][0]['attributes']['posterImage']['medium'])
                        except:
                            pass
                        try:
                            e.set_image(url=resp['data'][0]['attributes']['coverImage']['tiny'])
                        except:
                            pass
                        await ctx.send(embed=e)
            except:
                await ctx.send("Couldn't find that anime!")
            

    @commands.command()
    async def tickle(self, ctx, *, member: discord.Member=None):
        """Ticles a member you specify."""
        if member is None:
            await ctx.send(f'{ctx.tick(False)} You need to specify a user you want to tickle.')
            return
        e = discord.Embed(title="{} has been tickled by {}. UwU".format(member.name, ctx.author.name), color=ctx.author.top_role.color)
        e.set_image(url=nekos.img('tickle'))
        await ctx.send(embed=e)

    @commands.command()
    async def feed(self, ctx, *, member: discord.Member=None):
        """Feeds a member you specify."""
        if member is None:
            await ctx.send(f'{ctx.tick(False)} You need to specify a user you want to feed.')
            return
        if member.id == ctx.author.id:
            await ctx.send('Go eat on your own you don\'t need help with that.')
            return
        e = discord.Embed(title="{} has been fed by {}. OwO".format(member.name, ctx.author.name), color=ctx.author.top_role.color)
        e.set_image(url=nekos.img('feed'))
        await ctx.send(embed=e)

    @commands.command()
    async def gecg(self, ctx):
        """Gives you a gecg image."""
        e = discord.Embed(color=ctx.author.top_role.color)
        e.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        e.set_image(url=nekos.img('gecg'))
        await ctx.send(embed=e)

    @commands.command()
    async def kemonomimi(self, ctx):
        """Gives you a kemonomimi image."""
        e = discord.Embed(color=ctx.author.top_role.color)
        e.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        e.set_image(url=nekos.img('kemonomimi'))
        await ctx.send(embed=e)

    @commands.command()
    async def gasm(self, ctx):
        """Gives you a gasm image."""
        e = discord.Embed(color=ctx.author.top_role.color)
        e.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        e.set_image(url=nekos.img('gasm'))
        await ctx.send(embed=e)

    @commands.command()
    async def avatar(self, ctx):
        """Gives you an avatar image."""
        e = discord.Embed(color=ctx.author.top_role.color)
        e.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        e.set_image(url=nekos.img('avatar'))
        await ctx.send(embed=e)

    @commands.command()
    async def wallpaper(self, ctx):
        """Gives you a wallpaper image."""
        e = discord.Embed(color=ctx.author.top_role.color)
        e.set_image(url=nekos.img('wallpaper'))
        e.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=e)

    @commands.command()
    async def poke(self, ctx, member: discord.Member=None):
        """Pokes someone you mention."""
        if member is None:
            await ctx.send(f'{ctx.tick(False)} You need to specify who to poke.')
            return
        if member.id == ctx.author.id:
            await ctx.send('I find this very weird. I mean like even weirder than me...')
            return
        e = discord.Embed(title="{} has been poked by {}. >w<".format(member.name, ctx.author.name), color=ctx.author.top_role.color)
        e.set_image(url=nekos.img('poke'))
        await ctx.send(embed=e)

    @commands.command()
    async def slap(self, ctx, member: discord.Member=None):
        """Slaps someone you mention."""
        if member is None:
            await ctx.send(f'{ctx.tick(False)} You need to specify who to slap.')
            return
        if member.id == ctx.author.id:
            await ctx.send('I find this very weird. Why would you slap yourself?\nDid you do something stupid?')
            return
        e = discord.Embed(title="{} has been slapped by {}. XwX".format(member.name, ctx.author.name), color=ctx.author.top_role.color)
        e.set_image(url=nekos.img('slap'))
        await ctx.send(embed=e)

    @commands.command()
    async def pat(self, ctx, member: discord.Member=None):
        """Pats someone you mention."""
        if member is None:
            await ctx.send(f'{ctx.tick(False)} You need to specify who to pat.')
            return
        if member.id == ctx.author.id:
            await ctx.send('Why would you pat yourself? Are you lonely?')
            return
        e = discord.Embed(title="{} has pat by {}.".format(ctx.author.name, member.name), color=ctx.author.top_role.color)
        e.set_image(url=nekos.img('pat'))
        await ctx.send(embed=e)

    @commands.command()
    async def kiss(self, ctx, member: discord.Member=None):
        """Kisses someone you mention."""
        if member is None:
            await ctx.send(f'{ctx.tick(False)} You need to specify who to kiss.')
            return
        if member.id == ctx.author.id:
            await ctx.send('How is that even possible?')
            return
        e = discord.Embed(title="{} has been kissed by {}. ^W^".format(member.name, ctx.author.name), color=ctx.author.top_role.color)
        e.set_image(url=nekos.img('kiss'))
        await ctx.send(embed=e)

    @commands.command()
    async def hug(self, ctx, member: discord.Member=None):
        """Hugs someone you mention."""
        if member is None:
            await ctx.send(f'{ctx.tick(False)} You need to specify who to hug.')
            return
        if member.id == ctx.author.id:
            await ctx.send('You can try to put your arms around you if you think it is enough to hug yourself?')
            return
        e = discord.Embed(title="{} has been hugged by {}. UwU".format(member.name, ctx.author.name), color=ctx.author.top_role.color)
        e.set_image(url=nekos.img('hug'))
        await ctx.send(embed=e)

    @commands.command()
    async def cuddle(self, ctx, member: discord.Member=None):
        """Cuddles someone you mention."""
        if member is None:
            await ctx.send(f'{ctx.tick(False)} You need to specify who to cuddle with.')
            return
        if member.id == ctx.author.id:
            await ctx.send('How is that even possible?')
            return
        e = discord.Embed(title="{} has cuddled with {}. *W*".format(member.name, ctx.author.name), color=ctx.author.top_role.color)
        e.set_image(url=nekos.img('cuddle'))
        await ctx.send(embed=e)

    @commands.command()
    async def neko(self, ctx):
        """Gives you a neko image."""
        e = discord.Embed(color=ctx.author.top_role.color)
        e.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        e.set_image(url=nekos.img('neko'))
        await ctx.send(embed=e)

    @commands.command()
    async def holo(self, ctx):
        """Gives you a holo image."""
        e = discord.Embed(color=ctx.author.top_role.color)
        e.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        e.set_image(url=nekos.img('holo'))
        await ctx.send(embed=e)

    @commands.command()
    async def waifu(self, ctx):
        """Gives you a waifu image."""
        e = discord.Embed(colour=ctx.author.top_role.color)
        e.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        e.set_image(url=nekos.img('waifu'))
        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Anime(bot))
