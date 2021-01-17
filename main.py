import discord
import os
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions
import requests
from google_trans_new import google_translator
import asyncio


bot = Bot(command_prefix='?')
translator = google_translator()

TOKEN = ''  # Enter your bot token here


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="At your service, Master A Law#7777"))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot:
        return
    if 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')
    await bot.process_commands(message)


@bot.command(name='translate')
async def lang(ctx, arg1, *, text):
    try:
        user = ctx.author.mention
        message = ctx.message
        final = translator.translate(text, lang_tgt=arg1)
        await message.delete()
        await ctx.send(user + ': '+final)
    except:
        await ctx.send('Error in syntax (translate <language eg: en/fr>, text)')


@bot.command(case_insensitive=True, aliases=["remind", "remindme", "remind_me"])
async def reminder(ctx, time, *, reminder=None):
    user = ctx.message.author.id
    seconds = 0
    if reminder is None:
        # Error message
        await ctx.send("Please enter something to be reminded about")
    if time.lower().endswith("d"):
        seconds += int(time[:-1]) * 60 * 60 * 24
        counter = f"{seconds // 60 // 60 // 24} day(s)"
    if time.lower().endswith("h"):
        seconds += int(time[:-1]) * 60 * 60
        counter = f"{seconds // 60 // 60} hour(s)"
    elif time.lower().endswith("m"):
        seconds += int(time[:-1]) * 60
        counter = f"{seconds // 60} minute(s)"
    elif time.lower().endswith("s"):
        seconds += int(time[:-1])
        counter = f"{seconds} seconds"
    if seconds <= 0:
        await ctx.send("Please enter a valid amount of time")
    else:
        await ctx.send("Alright, " + '<@'+str(user)+'>' + f", I will remind you about {reminder} in {counter}.")
        await asyncio.sleep(seconds)
        await ctx.send('<@'+str(user)+'>' + f" you asked me to remind you about {reminder} {counter} ago.")
        return


@bot.command()
async def timer(ctx, arg1):
    await ctx.send("Timer for {} seconds has been set".format(arg1))
    await asyncio.sleep(int(arg1))
    await ctx.send("{} seconds have passed".format(arg1))


@bot.command(aliases=['feline', 'cat', 'cats'])
async def ca(ctx):
    response = requests.get('https://aws.random.cat/meow')
    data = response.json()
    embed = discord.Embed(
        title='Kitty Cat 🐈',
        description='Cats :star_struck:',
        colour=discord.Colour.purple()
    )
    embed.set_image(url=data['file'])
    embed.set_footer(text="")
    await ctx.send(embed=embed)


@bot.command(aliases=['echo', 'print'], description="say <message>")
async def say(ctx, channel: Optional[TextChannel], *, message=""):
    channel = channel or ctx  # default to ctx if we couldn't detect a channel
    await channel.send(message)
    await ctx.message.delete()


@bot.command(name='nick', pass_context=True)
async def chnick(ctx, member: discord.Member, *, nick):
    await member.edit(nick=nick)


@bot.command(name='server')
async def fetchServerInfo(context):
    guild = context.guild

    await context.send(f'Server Name: {guild.name}')
    await context.send(f'Server Size: {len(guild.members)}')
    await context.send(f'Server Name: {guild.owner.display_name}')


@bot.command(name='hello')
async def hello(message):
    await message.channel.send('Hello ' + message.author.mention + '! I am Alfred')


@bot.command(name='purge', pass_context=True)
@has_permissions(administrator=True)
async def clean(ctx, limit: int):
    limit = limit+1
    await ctx.channel.purge(limit=limit)
    await ctx.send('Cleared by {}'.format(ctx.author.mention))


@bot.command(name='mention')
async def args(ctx, arg1=None, arg2=None):
    try:
        if arg2 == None:
            arg2 = 1
        if arg1 == None:
            arg1 = ctx.author.mention
        if arg1 == ctx.guild.ownerID and ctx.author.mention != ctx.guild.ownerID:
            for x in range(int(arg2)):
                await ctx.send(ctx.author.mention)
        else:
            if int(arg2) > 5 and ctx.author.mention != ctx.guild.ownerID:
                arg2 = 10
                for x in range(int(arg2)):
                    await ctx.send(ctx.author.mention)
            else:
                for x in range(int(arg2)):
                    await ctx.send('Pinging {}'.format(arg1))
    except:
        print('hi')


bot.run(TOKEN)
