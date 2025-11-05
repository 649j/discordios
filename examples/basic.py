

import discord
from discordios import apply_mobile_status

apply_mobile_status('ios')

bot = discord.Client(intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'now bot as running')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

# Put your discord bot token to function this
TOKEN = 'DISCORD_TOKEN'

if __name__ == '__main__':

    bot.run(TOKEN)





