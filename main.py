import discord
from datetime import datetime
from scraper import get_featured
from decouple import config
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
    if message.content.startswith("!trivia"):
        if message.content == "!trivia":
            x = datetime.today().strftime('%m-%d').split('-')
            date_string = '{0}-{1}'.format(MONTHS[int(x[0])-1], x[1])
            await message.channel.send(get_featured(date_string))
        else:
            try:
                await message.channel.send(get_featured(message.content[8:]))
            except:
                await message.channel.send("Date invalid, Please try again in the format \"!trivia \{Month\}-\{day\}")
    

client.run(config('TOKEN'))
