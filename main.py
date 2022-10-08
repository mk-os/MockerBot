import random
import discord

token = "MTAyODQzNTczOTk5OTk5Nzk2Mw.G546px.JdXaRLB_5OD9ynk0FeD34dTPMspsj6WQGFZmJU"

def mocked(text):
    c = []
    for t in text:
        r = random.randint(0, 1)
        if r == 0:
            c.append(t.lower())
        else:
            c.append(t.upper())
    return ''.join(c)
