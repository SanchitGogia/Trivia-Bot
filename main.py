import discord

client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event 
async def on_message(message):
    if message.author == client.user:
        return 
    if message.content.startswith("$hello"):
        await message.channel.send("hello!")

client.run("OTU0NTMxMDQ3NTQ5MzMzNTg0.YjUeUA.EkEyN4m7YRCFzQVV1WJOomW3A64")