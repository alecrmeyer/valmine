class Player:
    def __init__(self, name, tag, driver):
        self.name = name
        self.tag = tag
        self.driver = driver

#returns an array of all matches 
    def getAllMatches(self):
        allMatches = []

        self.driver.get("https://api.tracker.gg/api/v2/valorant/standard/matches/riot/" + str(self.name) + "%23" + str(self.tag) + "?type=competitive")  
        jsonXpath = self.driver.find_element("xpath","/html/body/pre")
        allMatches.append(jsonXpath.text)

        for i in range(15): 
            self.driver.get("https://api.tracker.gg/api/v2/valorant/standard/matches/riot/" + str(self.name) + "%23" + str(self.tag) + "?type=competitive&next=" + str(i))    
            jsonXpath = self.driver.find_element("xpath","/html/body/pre")
            allMatches.append(jsonXpath.text)
        return allMatches

    def getTeammates(self):
        self.driver.get("https://api.tracker.gg/api/v1/valorant/matches/riot/" + str(self.name) + "%23" + str(self.tag) + "/aggregated?localOffset=300&playlist=competitive")
        jsonXpath = self.driver.find_element("xpath", "/html/body/pre")
        return jsonXpath.text
    
    