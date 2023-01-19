import discord
import json
import requests


class Apex():

    def __init__(self) -> None:
        pass
  
    def get_stats(self, player_name, platform="PC"):
        with open('config.json', 'r') as f:
            data = json.load(f)
            API_KEY = data['als_api_key']
            TRN_API_KEY = data['trn_api_key']
        platform = platform.upper()
        url = f"https://api.mozambiquehe.re/bridge?auth={API_KEY}&player={player_name}&platform={platform}"
        response = requests.get(url)
        print(player_name, platform)

        if response.status_code == 200 :
            player_stats = json.loads(response.text)
            print(player_stats["global"]["rank"])

            if "global" in player_stats:
                #getting player info from the ALS API
                player_nickname = player_stats["global"]["name"]
                rank_value = int(player_stats["global"]["rank"]["rankScore"])
                rank_name = player_stats["global"]["rank"]["rankName"]
                rank_div = player_stats["global"]["rank"]["rankDiv"]
                rank_pos = player_stats["global"]["rank"]["ladderPosPlatform"]

                rank_thumbnail = player_stats["global"]["rank"]["rankImg"]
                prestige = player_stats["global"]["levelPrestige"]
                lvl = player_stats["global"]["level"]

                #getting player avatar from TRN API (impossible from ALS)
                trn_platform = 'origin'
                if platform == 'PS4':
                    trn_platform = 'psn'
                if platform == 'X1':
                    trn_platform = 'xbl'
                trn_resp = requests.get(f"https://public-api.tracker.gg/v2/apex/standard/profile/{trn_platform}/{player_name}", headers={'TRN-Api-Key': TRN_API_KEY})
                data = json.loads(trn_resp.text)

                if "data" in data: #creating the stats embed with pfp
                    print('TRN_FOUND')
                    player_avatar = data['data']['platformInfo']['avatarUrl']
                    embed = discord.Embed(title=f"Ranked stats", color=0x00ff00, description="")
                    embed.set_author(name=player_nickname, icon_url=player_avatar)
                else: #creating the stats embed without profile picture
                    print("DNF_TRN")
                    embed = discord.Embed(title=f"Ranked stats", color=0x00ff00, description="")
                    embed.set_author(name=player_nickname)

       
                embed.set_thumbnail(url=rank_thumbnail)
                embed.add_field(name="Current level :", value=f"Prestige {prestige} - {lvl} ({prestige*500+lvl})", inline=False)
                if rank_name == 'Apex Predator' or rank_name == 'Master':
                    embed.add_field(name=f"Current ranking : {rank_name} #{rank_pos}", value=str(rank_value) + " RPs", inline=True)
                else:
                    embed.add_field(name=f"Current ranking : {rank_name} {rank_div}", value=str(rank_value) + " RPs", inline=True)
                embed.set_footer(text="This bot was developped by OutlawOnApex and uses the ALS API")
                return embed

            else: #error 102 player doesn't exist
                embed = discord.Embed(title=f"Player not found", color=0xff0000, description="")
                embed.set_footer(text="This bot was developped by OutlawOnApex and uses the ALS API")
                return embed

        else: #error 404 player exists but doesn't play the game
            embed = discord.Embed(title=f"Player did not play", color=0xff0000, description="")
            embed.set_footer(text="This bot was developped by OutlawOnApex and uses the ALS API")
            return embed

