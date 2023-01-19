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
      if random.randint(1, 500) == 1:
        await message.channel.send(f"[INSERT EASTER EGG] {message.author.mention}")


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
      stk = [discord.utils.get(message.guild.stickers, name='bonk')]
      await message.channel.send(f"Go to horny jail <@{ayer_id}>", stickers=stk)

    if message.content.startswith('>help'):
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=">help"))
      await message.channel.send(f"Utilise `>stats <pseudo> <plateforme>` pour avoir les stats d'un joueur Apex {message.author.mention} !")


    if message.content.startswith('>stats'):
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=">help"))
      args = message.content.split(" ")
      #print(args)
      if len(args) > 1:
        if len(args) == 2:
          player_name = args[1]
          await message.channel.send(embed=utils.get_stats(player_name=player_name))
        elif len(args) == 3:
          player_name = args[1]
          platform = args[2]
          await message.channel.send(embed=utils.get_stats(player_name=player_name, platform=platform))
        else:
          await message.channel.send(f"Utilise `>stats <pseudo> <PC/PS4/X1>`` pour avoir les stats d'un joueur Apex {message.author.mention} !")
      else:
        await message.channel.send(embed=utils.get_stats(player_name=player_name, platform=platform))

    #CHANGEMENTS DE COUSIN -- A TESTER

    #CHANGEMENT 1: ego lt -- devrait être fonctionnel
    if (message.content.find(
        'ego') != -1) and message.author.id == 445835527413956608:
      ltx_id = 882719651119898656
      #Tests momentanés, remettre LT une fois testé
      cousin_id = 445835527413956608
      await message.channel.send(f"T'es full ego lt <@{ltx_id}>")

    #CHANGEMENT 2: Taille Bite bot -- des mots augmentent la taille de bite et d'autres la réduise, faut garder la recette secrète
    #">taille_bite" sert à s'intégrer à l'enregistrement de taille de bite, ">stats_bite" servira à prendre des nouvelles sur sa taille de bite
    if (message.content.startswith('>taille_bite') != -1):
      #A faire: une boucle pour ajouter nouvel id (au lieu d'author1) au json à chaque fois qu'un nouvel utilisateur fait >taille_bite
      author1 = message.author.id
      taille_peni = 15 #taille de base pour tous
      await message.channel.send(f"Ta bite fait 15 cm <@{author1}>, beau péni")
      
      
      #Pour prendre les stats de la bite (si tu trouve une commande plus agréable à écrire que >stats_bite hésite pas à modif)
    if (message.content.startswith('>stats_bite') != -1):
      taille_peni = 
      if (taille_peni > 15):
        await message.channel.send(f"Beau péni <@{author1}>")
      elif (taille_peni > 12):
        await message.channel.send(f"Petit péni <@{author1}>")
      else:
        await message.channel.send(f"Micro péni <@{author1}>")





  keep_alive()

  try:
    client.run(TOKEN)
  except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    os.system('kill 1')
    os.system("keep_alive.py")


if __name__ == "__main__":
  main()

