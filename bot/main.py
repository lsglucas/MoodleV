import discord
from discord.ext import commands, tasks
from itertools import cycle
from commandslist import *
from secret import Bot_token


Prefix = 'm-'
client = commands.Bot(command_prefix=Prefix)
status = cycle(['Procurando atualizações...', 'Olhando para o Moodle', 'Descobrindo tarefas', 'Destruindo a casa do Jamil'])
PATH = 'C:\\Users\\lukep\\Projects\\Discord Bot\\DiscordMackBot\\template.csv'


@client.event
async def on_ready():
    change_status.start()
    print('We have logged in as {0.user}'.format(client))


@tasks.loop(seconds=10)
async def change_status():
    print("next status")
    await client.change_presence(activity=discord.Game(next(status)))


@client.command()
async def clear(ctx, amount=10):
    print("clear command")
    await ctx.channel.purge(limit=amount)


@client.command()
async def print_data():
    print('print_data')
    with open(PATH, "r") as data:
        for line in range(1, len(data)):
            await channel.send(f"# {line}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return


client.run(Bot_token)
