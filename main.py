import discord
import json
import os

from keep_alive import keep_alive
from utils import *

def main():

    client = discord.Client(command_prefix = ">", intents = discord.Intents.all())
    utils = Utils()

    with open('config.json', 'r') as f:
        data = json.load(f)
        TOKEN = data['TOKEN']

    @client.event
    async def on_ready():
        await client.change_presence(status=discord.Status.online)
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return    
  


        if message.content.startswith('hey') or message.content.startswith('salut') or message.content.startswith('Hey') or message.content.startswith('bonjour'):
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=">help"))
            await message.channel.send(f"Hey {message.author.mention} !")

        if message.content.startswith('>help'):
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=">help"))
            await message.channel.send(f"Utilise >stats <pseudo> pour avoir les stats d'un joueur PC {message.author.mention} !")

        if message.content.startswith('>stats'):
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=">help"))
            args = message.content.split(" ")
            print(args)
            if len(args) > 1:
                player_name = args[1]
                await message.channel.send(embed = utils.get_stats(player_name=player_name))
            else:
                await message.channel.send("Veuillez ajouter le nom du joueur !")
            

        #utils.debug(message)





    #client.run(TOKEN)

    keep_alive()
    
    try:
        client.run(TOKEN)
    except discord.errors.HTTPException:
        print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
        os.system('kill 1')
        os.system("python restarter.py")


if __name__ == "__main__":
    main()
