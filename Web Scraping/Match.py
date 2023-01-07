import json
import time
class Match:
    def __init__(self, uid, driver):
        self.uid = uid
        self.driver = driver

    def getAllPlayers(self):
        allPlayers = []

        self.driver.get("https://api.tracker.gg/api/v2/valorant/standard/matches/"+ self.uid)  
        jsonXpath = self.driver.find_element("xpath","/html/body/pre")
        
        data = json.loads(jsonXpath.text)

        count = 0
        for x in range(len(data["data"]["segments"])):
            if data["data"]["segments"][x]["type"] == "player-round":
                allPlayers.append(data["data"]["segments"][x]["attributes"]["platformUserIdentifier"])
                count+=1
                if count >= 10:
                    break
        return allPlayers

from selenium import webdriver

driver = webdriver.Chrome('Tools/chromedriver')
match = Match("65d8be75-b7fa-49d4-a8ce-d80d63876e9c", driver)
print(match.getAllPlayers())
            


    
    