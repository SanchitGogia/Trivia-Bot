import discord
from datetime import datetime
from scraper import get_featured
MONTHS = ['January','February','March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
flag  = 0
@client.event 
async def on_message(message):
    if message.author == client.user:
        return 
    if message.content == "!trivia":
        x = datetime.today().strftime('%m-%d').split('-')
        date_string = '{0}-{1}'.format(MONTHS[int(x[0])-1], x[1])
        await message.channel.send(get_featured(date_string))
    if flag == 1:
        flag = 0
        await message.channel.send(message.content)
    if message.content=="!trivia specific":
        flag = 1
        await message.channel.send("Please write the date in MM/DD format")
    

client.run("OTU0NTMxMDQ3NTQ5MzMzNTg0.YjUeUA.EkEyN4m7YRCFzQVV1WJOomW3A64")
