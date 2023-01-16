<h1>1 Background</h1>
VALORANT is a free-to-play first-person tactical hero shooter video games developed and published by Riot Games. In recent years, VALORANT has become one of the most watched and played competetive video games. Competetive VALORANT is 5v5 and first to 13.

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
