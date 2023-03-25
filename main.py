from multiprocessing import Event
import random
import discord

bot = discord.Client()
token = "" # Put your token here 

def mocked(text):
    c = []
    for t in text:
        r = random.randint(0, 1)
        if r == 0:
            c.append(t.lower())
        else:
            c.append(t.upper())
    return ''.join(c)

@bot.event
async def on_message(message):
    if message.author != bot.user:
        await message.channel.send('"' + mocked(message.content) + '" :nerd:', reference=message)
    
bot.run(token)
print("Bot online.")
