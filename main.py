import discord
from pycoingecko import CoinGeckoAPI

from keep_alive import keep_alive

import os

client = discord.Client()
cg = CoinGeckoAPI()

def get_info(ids):
  response = cg.get_price(ids=ids, vs_currencies='usd', include_market_cap=True, include_24hr_vol=True, include_24hr_change=True, include_last_updated_at=True)

  print(response)
  return response

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$info'):
      coin_list = get_info(message.content[5:])
      await message.channel.send(coin_list)

keep_alive()
client.run(os.getenv('TOKEN'))