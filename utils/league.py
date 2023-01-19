import discord
import json
import requests

class League():
    
    def __init__(self) -> None:
        self.emblems = {'iron' : 'https://cdn.discordapp.com/attachments/1065533237155348530/1065533317367218177/Emblem_Iron.png',
        'bronze' : 'https://media.discordapp.net/attachments/1065533237155348530/1065533316238934017/Emblem_Bronze.png',
        'silver' : 'https://cdn.discordapp.com/attachments/1065533237155348530/1065533318134775828/Emblem_Silver.png',
        'gold' : 'https://cdn.discordapp.com/attachments/1065533237155348530/1065533316905828392/Emblem_Gold.png',
        'platinum' : 'https://cdn.discordapp.com/attachments/1065533237155348530/1065533317878910996/Emblem_Platinum.png',
        'diamond' : 'https://cdn.discordapp.com/attachments/1065533237155348530/1065533316683546644/Emblem_Diamond.png',
        'master' : 'https://cdn.discordapp.com/attachments/1065533237155348530/1065533317639831582/Emblem_Master.png',
        'grandmaster' : 'https://cdn.discordapp.com/attachments/1065533237155348530/1065533317140713562/Emblem_Grandmaster.png',
        'challenger' : 'https://cdn.discordapp.com/attachments/1065533237155348530/1065533316457041990/Emblem_Challenger.png'}
        

    def get_stats(self, player_name, server='euw1'):
        with open('config.json', 'r') as f:
            data = json.load(f)
            API_KEY = data['lol_api_key']

        # Make a GET request to the API
        url = f"https://{server}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{player_name}?api_key={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200 :

            player_info = response.json()

            url = f"https://{server}.api.riotgames.com/lol/league/v4/entries/by-summoner/{player_info['id']}"
            response = requests.get(url, headers={"X-Riot-Token": API_KEY})

            # Get the JSON data from the response
            player_stats = response.json()

            summoner_name = player_info["name"]
            summoner_icon = player_info["profileIconId"]
            summoner_level = player_info["summonerLevel"]
            if player_stats:
                if len(player_stats) == 1:
                    if player_stats[0]['queueType'] == 'RANKED_SOLO_5x5':
                        queue_type = 'Ranked Solo/Duo'
                    else:
                        queue_type = 'Ranked Flex'
                    rank = player_stats[0]['tier']
                    tier = player_stats[0]['rank']
                    LP = player_stats[0]['leaguePoints']
                    wins = player_stats[0]['wins']
                    losses = player_stats[0]['losses']
                    hotstreak = player_stats[0]['hotStreak']
                    icon_url = f"http://ddragon.leagueoflegends.com/cdn/13.1.1/img/profileicon/{summoner_icon}.png"
                else:
                    queue_type = 'Ranked Solo/Duo'
                    rank = player_stats[0]['tier']
                    tier = player_stats[0]['rank']
                    LP = player_stats[0]['leaguePoints']
                    wins = player_stats[0]['wins']
                    losses = player_stats[0]['losses']
                    hotstreak = player_stats[0]['hotStreak']
                    icon_url = f"http://ddragon.leagueoflegends.com/cdn/13.1.1/img/profileicon/{summoner_icon}.png"

                embed = discord.Embed(title=f"Ranked stats", color=0x00ff00, description="")
                embed.set_author(name=summoner_name, icon_url=icon_url)
                embed.set_thumbnail(url=self.emblems[f'{rank.lower()}'])
                embed.add_field(name="Current level :", value=f"{summoner_level}", inline=False)
                if rank in ['CHALLENGER', 'GRANDMASTER', 'MASTER']:
                    embed.add_field(name=f"Current ranking in {queue_type} :", value=f"{rank} - {LP} LPs", inline=True)
                else:
                    embed.add_field(name=f"Current ranking in {queue_type} :", value=f"{rank} {tier} -  {LP} LPs", inline=True)
                embed.add_field(name="Winrate :", value=f"{wins}w/{losses}l - {round((wins/(wins+losses))*100)}%", inline=False)
                embed.set_footer(text="This bot was developped by OutlawOnApex and uses the Riot API")
                return embed


                    
            else:
                icon_url = f"http://ddragon.leagueoflegends.com/cdn/13.1.1/img/profileicon/{summoner_icon}.png"
                embed = discord.Embed(title=f"Player is unranked", color=0xff0000, description="")
                embed.set_author(name=summoner_name, icon_url=icon_url)
                embed.add_field(name="Current level :", value=f"{summoner_level}", inline=False)
                embed.set_footer(text="This bot was developped by OutlawOnApex and uses the Riot API")
                return embed

        else:
            embed = discord.Embed(title=f"Player does not exists", color=0xff0000, description="")
            embed.set_footer(text="This bot was developped by OutlawOnApex and uses the Riot API")
            return embed