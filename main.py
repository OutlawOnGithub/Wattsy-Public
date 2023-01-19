import discord
from discord.ext import commands
import json
import os
import random

from keep_alive import keep_alive
from utils.apex import *
from utils.league import *


def main():

    bot = commands.Bot(command_prefix=">", intents=discord.Intents.all(), activity=discord.Activity(type=discord.ActivityType.playing, name=">help", help_command = None))
    apexx = Apex()
    league = League()

    with open('config.json', 'r') as f:
        data = json.load(f)
        TOKEN = data['TOKEN']

    @bot.event
    async def on_ready():
        #await client.change_presence(status=discord.Status.online)
        print('We have logged in as {0.user}'.format(bot))

    @bot.event
    async def on_message(message):
        message.content = message.content.lower()
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == bot.user:
            return

        if message.content.startswith('') and message.author != bot.user:
        #print(message.content)
            if random.randint(1, 500) == 1:
                await message.channel.send(f"Belle bite {message.author.mention}")


        if message.content.startswith(('salut','hey','bonjour','yo')):
            answers = ["Yo", "Hey", "Salut", "Wesh", "Yo !"]
            await message.reply(f"{random.choice(answers)}")


        if message.content.find('ratio') != -1 :
            await message.add_reaction('👍')


        if message.content.startswith(('ça va ?', 'comment ça va', 'cv', 'cv ?')):
            answers = ["Moi ça chill", "Tranquille", "Tranquillou", "Moi ça va"]
            await message.reply(f"{random.choice(answers)}")


        if (x in message.content for x in ['je t\'aime','luxiie','jetaime','je taime','simp']) and message.author.id == 216707116369444864:
            ayer_id = 216707116369444864
            stk = [discord.utils.get(message.guild.stickers, name='bonk')]
            await message.channel.send(f"Go to horny jail <@{ayer_id}>", stickers=stk)
        
        await bot.process_commands(message)



    @bot.command()
    async def apex(ctx, player_name = None, platform = None):
        if platform:
            await ctx.send(embed=apexx.get_stats(player_name=player_name, platform=platform))
        elif player_name:
            await ctx.send(embed=apexx.get_stats(player_name=player_name))
        else:
            await ctx.send(f"Utilise `>apex <pseudo> <PC/PS4/X1>`` pour avoir les stats d'un joueur Apex {ctx.author.mention} !")

    @bot.command()
    async def lol(ctx, player_name = None, server = None):
        if server:
            await ctx.send(embed=league.get_stats(player_name=player_name, server=server))
        elif player_name:
            await ctx.send(embed=league.get_stats(player_name=player_name))
        else:
            await ctx.send(f"Utilise `>lol <pseudo> <EUW1/EUN1/NA1/KR>`` pour avoir les stats d'un joueur LoL {ctx.author.mention} !")



        
    keep_alive()

    try:
      bot.run(TOKEN)
    except discord.errors.HTTPException:
      print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
      os.system('kill 1')
      os.system("keep_alive.py")


if __name__ == "__main__":
    main()
