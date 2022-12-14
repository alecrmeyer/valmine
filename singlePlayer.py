from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from valmine2 import *

###Cloudflare blocked my previous attempt to curl by only allowing requests which could execute javascript (I believe)

# https://api.tracker.gg/api/v1/valorant/matches/riot/chy%2300000/aggregated?localOffset=300&playlist=competitive

###gets first page
driver = webdriver.Chrome('/Users/alecrmeyer/Desktop/Projects/valmine/chromedriver')

name = input("name: ")
tag = input("tag: ")
smurf = input("smurf: ")

if smurf == "yes":
    smurf = True
else: 
    smurf = False

players = {}

def recur(name, tag):   
   # try:
    driver.get("https://api.tracker.gg/api/v2/valorant/standard/matches/riot/" + str(name) + "%23" + str(tag) + "?type=competitive")  
    jsonXpath = driver.find_element("xpath","/html/body/pre")
    f = open("/Users/alecrmeyer/Desktop/Projects/valmine/valdataa.json", "w")
    f.write(jsonXpath.text)
    f.close()
    import_data(smurf)

    ###gets all pages besides first
    for i in range(15): 

        driver.get("https://api.tracker.gg/api/v2/valorant/standard/matches/riot/" + str(name) + "%23" + str(tag) + "?type=competitive&next=" + str(i))    

        jsonXpath = driver.find_element("xpath","/html/body/pre")

        f = open("/Users/alecrmeyer/Desktop/Projects/valmine/valdataa.json", "w")
        f.write(jsonXpath.text)
        f.close()
        import_data(smurf)
    #except:
        #print("probably no matches")
    
         
recur(name, tag)

driver.close()