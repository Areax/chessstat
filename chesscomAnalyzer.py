"""Requests PNG files from lichess.org"""

import requests 
import time
import json
from pathlib import Path

pre_analyzed = []

USERNAME = input('chess.com username: ')

player_information = requests.get("https://api.chess.com/pub/player/" + USERNAME).json()
print (player_information)
online_pgns = open('allGames.pgn', 'w')
games = {}
games["games"] = []

openings = json.loads(Path('dictOfOpenings.txt').read_text())
opening_keys = sorted(list(openings.keys()), key=len)
opening_keys.reverse()


for page in [1,2,3]:
	temp = requests.get("https://api.chess.com/pub/player/" + USERNAME + "/games/2017/" + str(11 - page + 1)).json()
	if("games" in temp.keys()):
		games["games"] = games["games"] + temp["games"]
	time.sleep(2)

	 
	for game in games["games"]:
		for key in opening_keys:
			try:
				if(key in game["pgn"]):
					game["Opening"] = openings[key]
			except Exception as e:
				game["Opening"] = "unknown"
	
online_pgns.write(json.dumps(games, indent=4, sort_keys=True))
#for game in games["currentPageResults"]: 

#print (games)
	
online_pgns.close() #finishes writing game into pgn file and closes,,,