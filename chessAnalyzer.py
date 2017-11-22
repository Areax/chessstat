"""Requests PNG files from lichess.org"""

import requests 
import time
import json

pre_analyzed = []

USERNAME = input('Lichess username: ')

player_information = requests.get("https://lichess.org/api/user/"+USERNAME).json()
print (player_information)
online_pgns = open('allGames.pgn', 'w')
games = {}

for page in [1,2,3,4,5,6]:
	games[page] = requests.get("https://lichess.org/api/user/"+USERNAME+"/games?nb=100&page="+str(page)+"&with_moves=1&with_opening=1&with_analysis=1").json()
	time.sleep(2)

online_pgns.write(json.dumps(games, indent=4, sort_keys=True))
#for game in games["currentPageResults"]: 

print ('pgn file saved')
	
online_pgns.close() #finishes writing game into pgn file and closes,,,