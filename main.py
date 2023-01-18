import discord
import json
import os
import random

from keep_alive import keep_alive
from utils import *


def main():

  client = discord.Client(command_prefix="-", intents=discord.Intents.all())
  utils = Utils()

  with open('config.json', 'r') as f:
    data = json.load(f)
    TOKEN = data['TOKEN']

  @client.event
  async def on_ready():
    #await client.change_presence(status=discord.Status.online)
    print('We have logged in as {0.user}'.format(client))

  @client.event
  async def on_message(message):
    # Make sure bot doesn't get stuck in an infinite loop
    if message.author == client.user:
      return

    if message.content.startswith('') and message.author != client.user:
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=">help"))
      #print(message.content)
      if random.randint(1, 500) == 1:
        await message.channel.send(f"Belle bite {message.author.mention}")


    if message.content.startswith('hey') or message.content.startswith(
        'salut') or message.content.startswith(
        'Salut') or message.content.startswith(
        'hey') or message.content.startswith(
        'Hey') or message.content.startswith(
        'bonjour') or message.content.startswith(
        'Bonjour'):
      await message.channel.send(f"Hey {message.author.mention} !")


    if message.content.find('ratio') != -1 :
      await message.add_reaction('👍')


    if message.content.startswith('ça va ?') or message.content.startswith(
        'comment ça va') or message.content.startswith(
        'ça va') or message.content.startswith(
        'Comment ça va') or message.content.startswith(
        'Comment ça va ?') or message.content.startswith(
        'cv') or message.content.startswith(
        'cv ?'):
      await message.channel.send(
        f"Moi ça chill écoutes {message.author.mention}")


    if (message.content.find(
        'je t\'aime') != -1 or message.content.find(
        'luxiie') != -1 or message.content.find(
        'Luxiie') != -1 or message.content.find(
        'jetaime') != -1 or message.content.find(
        'je taime') != -1 or message.content.find(
        'simp') != -1) and message.author.id == 216707116369444864:
      ayer_id = 216707116369444864
      #moi_id = 785316706884911134
      stk = [discord.utils.get(message.guild.stickers, name='bonk')]
      await message.channel.send(f"Go to horny jail <@{ayer_id}>", stickers=stk)


    if message.content.startswith('>help'):
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=">help"))
      await message.channel.send(f"Utilise >stats <pseudo> pour avoir les stats d'un joueur PC {message.author.mention} !")


    if message.content.startswith('>stats'):
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=">help"))
      args = message.content.split(" ")
      #print(args)
      if len(args) > 1:
        player_name = args[1]
        await message.channel.send(embed=utils.get_stats(player_name=player_name))
      else:
        await message.channel.send("Veuillez ajouter le nom du joueur !")


    #utils.debug(message)

  client.run(TOKEN)

  #keep_alive()

  # try:
  #   client.run(TOKEN)
  # except discord.errors.HTTPException:
  #   print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
  #   os.system('kill 1')
  #   os.system("python restarter.py")


if __name__ == "__main__":
  main()
