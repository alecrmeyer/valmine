<h1>1 Background</h1>
VALORANT is a free-to-play first-person tactical hero shooter video games developed and published by Riot Games. In recent years, VALORANT has become one of the most watched and played competetive video games. Competetive VALORANT is 5v5 and first to 13. There are 25 competetive rankings in VALORANT which are:

* Iron 1-3
* Bronze 1-3
* Silver 1-3
* Gold 1-3
* Platinum 1-3
* Diamond 1-3
* Ascendant 1-3
* Immortal 1-3
* Radiant

(((Add rank distribution chart here)))

<h1>2 Overview</h1>
The goal of this project is explore trends and correlations drived from competetive VALORANT match data. There are 1.1 million matches being used for analysis ranging from all skill levels in the game. The code used to gather this match data is provided in the repository and explained below. The data gathered is by a single players match statistics.

<h1>3 Goals</h1>
<h2>3.1 Smurf Detection</h2>
The main question being asked about this data is if we can use machine learning to determine if a user is a Smurf or not. A Smurf is a term used to describe a person who intentionally plays a video game at a lower skill level than their own to gain an competetive advantage. Smurfing over the years has become a controversial issue as it has proven to be nearly impossible to detect and many people believe it is not a concern (https://medium.com/illumination/lets-talk-about-smurfs-in-competitive-games-b1c7b13bb1c1#:~:text=A%20smurf%20is%20a%20term,play%20against%20lower%2Dranked%20players). 

Smurfing is very difficult to detect as natural human variation in performance hinders many machine learning models from accurate predictions. A few scenarios which make smurf detection difficult include:
* A user at their correct skill level, could play a game(or series of games) where they out-perform each other user.
* Smurfing is on a spectrum. For example, it is easier to detect a skill disparity between a high skilled and low skilled player than it is between an averagely skilled and high skilled player.
* Smurfs can easily mimic their new skill levels skill level. For example, a highly skilled smurf can attempt to fit into a low skill level by intentionally manipulating their stats to conform with other players at that level. 

A few Hypothesese about smurf detection:
* Generic stats such as kills and deaths can be easily manipulated by a smurfing user, but stats such as abilty usage, headshot percentage, damage dealt and receieved, might be less of a focus when trying to mimic skill level.
* ...
    
<h2>3.2 Match Outcome Prediction</h2>

Determine the outcome of a match based on all 10 players statistics.
* Predict a players performance based on the map and agent selected.
* Then average their performance with the rest of the team.
* Then determine which team has a higher chance to win based on their averaged  
stats.

<h1>4 Data</h1>
<h2>4.1 Obtaining Data</h2>
The data used in this project was obtained by scraping individual match data from https://tracker.gg. Riot Games does not provide an open API for VALORANT, instead they require a developers license to query user and match data. The algorithm used to gather match data follows a breadth-first approach and works like so:
```
Input a single users ID as the root node
Create a queue
Add the root user to the queue
While the queue is not empty:
    Pop current user from top of the queue
    For each of the current user's matches played:
        For each player in the match:
            Add the player to a queue
            Add the players stats from this match to the DB
```
This script was ran for about 16 hours total with two different root node users. The first user was currently ranked Ascendant 2 and the second user was ranked Platinum 1. Running the scrapper with these two unique nodes caused 2 gaussian peaks in the resulting competetive rank distribution. 

<h2>4.2 Format</h2>
The data is formated as:

