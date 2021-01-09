import discord
import os

client = discord.Client()

token = ''  # Enter your token id here
name = 'Alfred'  # Name of the bot


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    sender = str(message.author.id)
    mention = '<@' + sender + '>'

    if message.author == client.user:
        return

    if message.content.startswith('?hello'):
        await message.channel.send('Hello ' + mention + '! I am', name)
    if message.content.startswith('?info'):

        await message.channel.send('Made by A Law#7777 (<@186870407738032129>)')


client.run()
