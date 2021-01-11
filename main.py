import discord
import os
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions

bot = Bot(command_prefix='?')
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


@bot.command(name='say')
async def say(ctx, *, text):
    message = ctx.message
    await message.delete()
    await ctx.send(f"{text}")


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
