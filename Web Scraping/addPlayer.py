from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from valmine2 import *
from Player import *


#Cloudflare blocked my previous attempt to curl by only allowing requests which could execute javascript (I believe)
driver = webdriver.Chrome('Tools/chromedriver')

name = input("name: ")
tag = input("tag: ")

#BFS for all users
def addPlayers(name, tag):
     
    player = Player(name, tag, driver)
    teammates = get_teammates(player.getTeammates())

    queue = []
    queue.append(player)

    while queue:

        player = queue.pop(0)

        for i in range(len(get_teammates(player.getTeammates()))):  
            try:
                name = teammates[i+1][0]
                tag = teammates[i+1][1]
                player = Player(name, tag, driver)
                queue.append(player)

                matches = player.getAllMatches()
                for match in matches:
                    import_data(False, match)
                print(name +"#"+ tag + " added")
            except IndexError as e:
                print(e)
                print("No teammates")

        
addPlayers(name, tag)


driver.close()