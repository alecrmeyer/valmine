from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from valmine2 import *

###Cloudflare blocked my previous attempt to curl by only allowing requests which could execute javascript (I believe)

# https://api.tracker.gg/api/v1/valorant/matches/riot/chy%2300000/aggregated?localOffset=300&playlist=competitive

###gets first page
driver = webdriver.Chrome('/Users/alecrmeyer/Desktop/Projects/valmine/chromedriver')


name = input("name: ")
tag = input("tag: ")

players = {}



def recur(name, tag):
     

     driver.get("https://api.tracker.gg/api/v1/valorant/matches/riot/" + str(name) + "%23" + str(tag) + "/aggregated?localOffset=300&playlist=competitive")
     jsonXpath = driver.find_element_by_xpath("/html/body/pre")
     teammates = open("/Users/alecrmeyer/Desktop/Projects/valmine/teammates.json", "w")
     teammates.write(jsonXpath.text)
     teammates.close()

     teammates = get_teammates()
     
     for i in range(len(teammates)):
          try:
               name = teammates[i+1][0]
               tag = teammates[i+1][1]
               driver.get("https://api.tracker.gg/api/v2/valorant/standard/matches/riot/" + str(name) + "%23" + str(tag) + "?type=competitive")  
               jsonXpath = driver.find_element_by_xpath("/html/body/pre")
               f = open("/Users/alecrmeyer/Desktop/Projects/valmine/valdataa.json", "w")
               f.write(jsonXpath.text)
               f.close()
               import_data()

               ###gets all pages besides first
               for i in range(15): 

                    driver.get("https://api.tracker.gg/api/v2/valorant/standard/matches/riot/" + str(name) + "%23" + str(tag) + "?type=competitive&next=" + str(i))    

                    jsonXpath = driver.find_element_by_xpath("/html/body/pre")

                    f = open("/Users/alecrmeyer/Desktop/Projects/valmine/valdataa.json", "w")
                    f.write(jsonXpath.text)
                    f.close()
                    import_data()
          except:
               print("probably no matches")
    
          for i in range(len(teammates)):
               try:
                    name = teammates[i+1][0]
                    tag = teammates[i+1][1]
                    fullname = str(name) + str(tag)
                    if fullname not in players:
                         print(fullname)
                         players[fullname] = len(players)
                         recur(name, tag)
                    else:
                         print("In List")
               except:
                    print("Skipped Teammate")
     
     
recur(name, tag)

driver.close()