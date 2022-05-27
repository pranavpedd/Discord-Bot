import discord
import random
import resources
import important
from discord.ext import commands
from datetime import date

# creates our bot and makes it so that we can talk to it using the prefix ! followed by a command
client = commands.Bot(command_prefix='!')


# this method decorator lets us know that this is an event
@client.event
async def on_ready():
    # if the bot is ready, this message gets printed
    print('bot is ready')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.CommandNotFound):
        await ctx.send("I don't know how to do that!")


@client.command()
async def intro(ctx):
    await ctx.send('Hello there! My name is Zen! You can type "!help" to see all my commands!')


@client.command()
async def ping(ctx):
    msg = 'Latency: ' + str(round(client.latency * 1000)) + 'ms'
    await ctx.send(msg)


@client.command()
async def task(ctx):
    await ctx.send(resources.TASKS[random.randint(0, len(resources.TASKS) - 1)])


@client.command(aliases=['date'])
async def what_is_the_date(ctx):
    today = date.today()
    formatted_date = today.strftime('%B %d, %Y')
    await ctx.send("Today's date is: " + str(formatted_date))


@client.command(aliases=['moveIn'])
async def when_am_i_moving(ctx):
    curr = date.today()
    move = date(2021, 8, 26)
    delta = move - curr
    await ctx.send('You are moving to UMD in ' + str(delta.days) + ' days')


@client.command()
async def ask(ctx, *question):
    answer = resources.ANS[random.randint(0, len(resources.ANS) - 1)]
    await ctx.send(answer)


@client.command()
async def mock(ctx, *words):
    msg = ''
    joined = ' '.join(words)
    for word in joined:
        for char in word:
            case = random.randint(0, 1)
            if case == 0:
                msg += char.upper()
            else:
                msg += char.lower()

    await ctx.send(msg)


@client.command()
async def dogecoin(ctx):
    resources.AMOUNT += 1
    await ctx.send(file=discord.File('/Users/pranav/Documents/Pictures/dogecoin png.png'))
    await ctx.send('You have ' + str(resources.AMOUNT) + ' dogecoins')


@client.command()
async def amount(ctx):
    await ctx.send('You currently have ' + str(resources.AMOUNT) + ' dogecoins.')


@client.command()
async def sell(ctx, coins: int):
    resources.AMOUNT -= coins
    await ctx.send('You now have ' + str(resources.AMOUNT) + ' dogecoin(s) left in your account.')

# bot goes online in the discord server
client.run(important.token)
