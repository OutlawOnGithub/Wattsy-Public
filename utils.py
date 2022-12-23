import discord
import json
import requests

class Utils():

    def __init__(self):
        self.trn_api_url = "https://public-api.tracker.gg/v2/apex/standard/profile"
        self.wattsy_image = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2F736x%2Fa4%2F49%2F72%2Fa449725671e13b8911e0fdec33c8c8fd.jpg&f=1&nofb=1&ipt=dc0de350f6e8745f3cee2801619007265a225b907d6d16e48093cc9ee9c8a6c7&ipo=images"
        self.trn_api_key = "TRN_API_KEY"
        self.als_api_key = "ALS_API_KEY"


    def get_stats(self, player_name, platform="PC"): #didn't add the support for platform but not hard to add
        url = f"https://api.mozambiquehe.re/bridge?auth={self.als_api_key}&player={player_name}&platform={platform}"
        response = requests.get(url)
        if response.status_code == 200:
            player_stats = json.loads(response.text)      
               
            if "global" in player_stats:
                rank_value = int(player_stats["global"]["rank"]["rankScore"])
                rank_name = player_stats["global"]["rank"]["rankName"]
                rank_div = player_stats["global"]["rank"]["rankDiv"]
                se_kills_value = player_stats["total"]["specialEvent_kills"]["value"]
                kills_value = player_stats["total"]["kills"]["value"]
                kills = se_kills_value + kills_value
                player_rank = f"{rank_name} {rank_div}"
                rank_thumbnail = player_stats["global"]["rank"]["rankImg"]
                embed = discord.Embed(title=f"Ranked stats", color=0x00ff00, description="")
                embed.set_author(name=player_name, icon_url=self.wattsy_image)
                embed.set_thumbnail(url=rank_thumbnail)
                embed.add_field(name="Current ranking : " + str(player_rank), value=str(rank_value) + " RPs", inline=True)
                embed.add_field(name="Kill total", value=str(kills), inline=False)
                #embed.add_field(name="Nombres de matchs joués", value=f"{matches_value}", inline=False)
                embed.set_footer(text="This bot was developped by OutlawOnApex and uses the ALS API")
                return embed
            
            else:
                embed = discord.Embed(title=f"Player not found", color=0x00ff00, description="")
                embed.set_footer(text="This bot was developped by OutlawOnApex and uses the ALS API")
                return embed


    def debug(self, message):
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")
