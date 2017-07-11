import discord
from discord.ext import commands
from riotwatcher import RiotWatcher

TOKEN = ''
lol = RiotWatcher('')

description = '''League of Legends bot - Coded in Python by Logicmn'''
bot = commands.Bot(command_prefix='.', description=description)

@bot.event
async def on_ready():
    print('----------------------------')
    print('Connected!')
    print('Logged in as: {0}'.format(bot.user.name))
    print('Bot ID: {0}'.format(bot.user.id))
    print('Requests left?: {0}'.format(lol.can_make_request()))
    print('----------------------------')

@bot.command()
async def hello():
    """Says world"""
    await bot.say("world")

'''
@bot.event
async def on_message(message):
    """
    Use this command to grab the id of a summoner.
    """
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    if message.content.startswith('!summonerid '):
        name = message.content.replace('!summonerid ', '')
        try:
            user = lol.get_summoner(name=name.replace(' ', '_'))
            await bot.send_message(message.channel, user['id'])
        except:
            await bot.send_message(message.channel, 'That summoner does not exist! Spooky...')
'''

@bot.command()
async def info(id: str):
    """
    Use this command to look up a summoner by id.
    """
    user = lol.get_summoner(_id=id)
    print(id)
    print(user)
    await bot.say(user)

@bot.command()
async def add(left: int, right: int):
    """Adds two numbers together."""
    await bot.say(left + right)

bot.run(TOKEN)
