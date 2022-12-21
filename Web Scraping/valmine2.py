import json
from MySQLSetup import *


#CREATE A MANY TO 1 RELATIONSHIP, A MATCH TABLE WITH MATCH ID THEN A PLAYERS TABLE WITH THEIR STATS FOR EACH MATCH?

sql = """INSERT INTO stats (match_player_id, rounds, date, result, map, smurf, 
    agent, kills, headshots, deaths, assists, damage, damage_received, 
    econ_rating, plants, defuses, first_bloods, grenade_casts, ability_2_casts, 
    ability_1_casts, ultimate_casts, placement, kdratio, headshot_percentage, 
    first_deaths, last_deaths, current_rank) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
     ON DUPLICATE KEY UPDATE match_player_id=VALUES(match_player_id)"""   

def import_data(smurf, data):
    try:
        data = json.loads(data)
        for i in range(len(data["data"]["matches"])):
            metadata = []
            match_id = data["data"]["matches"][i]["attributes"]["id"]
            player = data["data"]["matches"][i]["segments"][0]["attributes"]["platformUserIdentifier"]
            match_player_id = match_id + player
            metadata.append(match_player_id)

            metadata.append(data["data"]["matches"][i]["metadata"]["modeMaxRounds"])
            metadata.append(data["data"]["matches"][i]["metadata"]["timestamp"])
            metadata.append(data["data"]["matches"][i]["metadata"]["result"])
            metadata.append(data["data"]["matches"][i]["metadata"]["mapName"])
            metadata.append(smurf)

            metadata.append(data["data"]["matches"][i]["segments"][0]["metadata"]["agentName"])

            #add headshot dealt data
            var = ["kills", "headshots", "deaths", "assists", "damage", 
                    "damageReceived", "econRating", "plants", "defuses", 
                    "firstBloods", "grenadeCasts", "ability1Casts", "ability2Casts", 
                    "ultimateCasts", "placement", "kdRatio", "headshotsPercentage", 
                    "firstDeaths", "lastDeaths"]  
            for val in range(len(var)):
                metadata.append(data["data"]["matches"][i]["segments"][0]["stats"][var[val]]["value"])

            metadata.append(data["data"]["matches"][i]["segments"][0]["stats"]["rank"]["metadata"]["tierName"])

            sendQuery(sql, metadata)
    except KeyError as e:
        print(e)
        print("Private account or bad data")

        
def get_teammates(data):
    data = json.loads(data)
    players = [[]]
    try:
        for i in range(len(data["data"]["teammates"])):
            player = data["data"]["teammates"][i]["teammate"]
            print(player)
            name = player.split("#")[0]
            tag = player.split("#")[1]
            players.append([name, tag])
    except KeyError as e:
        print(e)
        print(" Possibly has no teammates")
        
    return players


