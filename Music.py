import discord
import youtube_dl
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '>')

players = {}
queues = {}

def check_queue(id):
	if queues[id] != []:
		player = queues[id].pop(0)
		players[id] = playerplayer.start()

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
    players[server.id] = player
    player.start()

@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()

@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

@client.command(pass_context=True)
async def queue(ctx, url):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = await voice_channel.create_ytdl_player(url, after=lambda: check_queue(server.id))
	
	if server.id in queues:
		queues[server.id].append(player)
	else:
		queues[server.id] = [player]
	await client.say('Queued Next Song.')
			

    
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='with Neppugear (´｡• ω •｡`) ', type=0))
    print('Bot is online')

client.run(os.getenv('TOKEN'))
