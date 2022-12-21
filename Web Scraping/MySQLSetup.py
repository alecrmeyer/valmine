import mysql.connector

_mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

sql = """CREATE DATABASE IF NOT EXISTS valorant_tracker;
USE valorant_tracker;
CREATE TABLE IF NOT EXISTS `stats` (
  `match_player_id` varchar(100) DEFAULT NULL,
  `rounds` int DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `result` varchar(45) DEFAULT NULL,
  `map` varchar(45) DEFAULT NULL,
  `smurf` tinyint(1) DEFAULT NULL,
  `agent` varchar(45) DEFAULT NULL,
  `kills` int DEFAULT NULL,
  `headshots` int DEFAULT NULL,
  `deaths` int DEFAULT NULL,
  `assists` int DEFAULT NULL,
  `damage` int DEFAULT NULL,
  `damage_received` int DEFAULT NULL,
  `econ_rating` int DEFAULT NULL,
  `plants` int DEFAULT NULL,
  `defuses` int DEFAULT NULL,
  `first_bloods` int DEFAULT NULL,
  `grenade_casts` int DEFAULT NULL,
  `ability_2_casts` int DEFAULT NULL,
  `ability_1_casts` int DEFAULT NULL,
  `ultimate_casts` int DEFAULT NULL,
  `placement` int DEFAULT NULL,
  `kdratio` int DEFAULT NULL,
  `headshot_percentage` double DEFAULT NULL,
  `first_deaths` int DEFAULT NULL,
  `last_deaths` int DEFAULT NULL,
  `current_rank` varchar(20) DEFAULT NULL,
  UNIQUE KEY `match_player_id` (`match_player_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"""

_cursor = _mydb.cursor()
_cursor.execute(sql)

_mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="valorant_tracker"
)

_mycursor = _mydb.cursor()

def sendQuery(sql, metadata):
        _mycursor.execute(sql, metadata)
        _mydb.commit()