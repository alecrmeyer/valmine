The goal of this project is to analyze and explore correlations and trends derived from VALORANT match data. There are roughly 1.1 million recorded matches being used for analysis. The code for the webscraper used is in the Web Scraping directory of this project and performs a breadth-first-search approach to adding user matches to a MySQL DB. A mixture of machine learning and exploratory analysis is being conducted on this data. 

The main question being asked about this data is if we can use machine learning to determine if a user is a Smurf or not. A Smurf is a term used to describe a person who intentionally plays a video game at a lower skill level than their own to gain an competetive advantage. Smurfing over the years has become a controversial issue as it has proven to be nearly impossible to detect and many people believe it is not a concern (https://medium.com/illumination/lets-talk-about-smurfs-in-competitive-games-b1c7b13bb1c1#:~:text=A%20smurf%20is%20a%20term,play%20against%20lower%2Dranked%20players.). 

Smurfing is very difficult to detect as natural human variation in performance hinders many machine learning models from accurate predictions. A few scenarios which make smurf detection difficult include:
    -A user at their correct skill level, could play a game(or series of games) where they out-perform each other user.
    -Smurfing is on a spectrum. For example, it is easier to detect a skill disparity between a high skilled and low skilled player than it is between an averagely skilled and high skilled player. 
    -Smurfs can easily mimic their new skill levels skill level. For example, a highly skilled smurf can attempt to fit into a low skill level by intentionally manipulating their stats to conform with other players at that level. 

A few Hypothesese about smurf detection(in VALORANT):
    - Generic stats such as kills and deaths can be easily manipulated by a smurfing user, but stats such as abilty usage, headshot percentage, damage dealt and receieved, might be less of a focus when trying to mimic skill level. 
    - ...


Questions:

Ideas:
    -Outliers for kills/damage didnt have much to infer about, but splitting players with large rank increases could be interesting. 
    -Determine the outcome of a match based on all 10 players statistics. 
        -Predict a players performance based on the map and agent selected. 
        -Then average their performance with the rest of the team 
        -Then determine which team has a higher chance to win based on their averaged  
        stats