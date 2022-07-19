import json
import mysql.connector



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="valorant_tracker"
)

mycursor = mydb.cursor()

sql = """INSERT INTO stats (match_id, rounds, date, result, map, 
    agent, kills, headshots, deaths, assists, damage, damage_received, 
    econ_rating, plants, defuses, first_bloods, grenade_casts, ability_2_casts, 
    ability_1_casts, ultimate_casts, placement, kdratio, headshot_percentage, 
    first_deaths, last_deaths, current_rank) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
     ON DUPLICATE KEY UPDATE match_id=VALUES(match_id)"""   

def import_data():
    with open('/Users/alecrmeyer/Desktop/Projects/valmine/valdataa.json') as f:
        data = json.load(f)
    try:
        for i in range(len(data["data"]["matches"])):
            metadata = []
            metadata.append(data["data"]["matches"][i]["attributes"]["id"])

            
            metadata.append(data["data"]["matches"][i]["metadata"]["modeMaxRounds"])
            metadata.append(data["data"]["matches"][i]["metadata"]["timestamp"])
            metadata.append(data["data"]["matches"][i]["metadata"]["result"])
            metadata.append(data["data"]["matches"][i]["metadata"]["mapName"])

            metadata.append(data["data"]["matches"][i]["segments"][0]["metadata"]["agentName"])

            var = ["kills", "headshots", "deaths", "assists", "damage", 
                    "damageReceived", "econRating", "plants", "defuses", 
                    "firstBloods", "grenadeCasts", "ability1Casts", "ability2Casts", 
                    "ultimateCasts", "placement", "kdRatio", "headshotsPercentage", 
                    "deathsFirst", "deathsLast"]  
            for val in range(len(var)):
                metadata.append(data["data"]["matches"][i]["segments"][0]["stats"][var[val]]["value"])

            metadata.append(data["data"]["matches"][i]["segments"][0]["stats"]["rank"]["metadata"]["tierName"])
            mycursor.execute(sql, metadata)


            mydb.commit()

    except:
        print("Skipped")

        
def get_teammates():
    with open('/Users/alecrmeyer/Desktop/Projects/valmine/teammates.json') as f:
        data = json.load(f)
        players = [[]]
        for i in range(len(data["data"]["teammates"])):
            player = data["data"]["teammates"][i]["teammate"]
            name = player.split("#")[0]
            tag = player.split("#")[1]
            players.append([name, tag])
            
        return players

if __name__ == '__main__':
    # Script2.py executed as script
    # do something
    import_data()


