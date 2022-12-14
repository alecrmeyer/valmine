from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from valmine2 import *
from Player import *

#SHOULD FIND PLAYERS BASED ON A USERS PLAYED GAMES NOT BASED ON THEIR MOST PLAYED TEAM MATES
#SMURFS ARE MORE LIKELY TO PLAY ALONE AND NOT WITH MANY PEOPLE

###Cloudflare blocked my previous attempt to curl by only allowing requests which could execute javascript (I believe)

# https://api.tracker.gg/api/v1/valorant/matches/riot/chy%2300000/aggregated?localOffset=300&playlist=competitive

###gets first page

## want to try breadthfirst search to minimize loop possiblity 
driver = webdriver.Chrome('/Users/alecrmeyer/Desktop/Projects/valmine/chromedriver')

name = input("name: ")
tag = input("tag: ")


def recur(name, tag):
     
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
                #print(name + tag + "added")
                print(queue)
            except:
                print("No matches/Private/Error")
         
recur(name, tag)


driver.close()