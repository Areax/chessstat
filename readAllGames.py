from pathlib import Path
import json

USERNAME = input('Lichess username: ')
games = json.loads(Path('allGames.pgn').read_text())

openings = {}

for page in games.keys():
	for game in games[page]["currentPageResults"]:
		if(game["variant"] == "standard" and "opening" in game):
			if(not(game["opening"]["name"] in openings)):
				openings[game["opening"]["name"]] = {
					"user_is_white": {
						"wins": 0, 
						"draws": 0,
						"losses": 0,
						"total": 0
					},
					"user_is_black": {
						"wins": 0, 
						"draws": 0,
						"losses": 0,
						"total": 0
					}
				}
				
			is_white = game["players"]["white"]["userId"] == USERNAME
			if(is_white):
				openings[game["opening"]["name"]]["user_is_white"]["total"] += 1
				
				if("winner" in game):
					if(game["winner"] == "white"):
						openings[game["opening"]["name"]]["user_is_white"]["wins"] += 1
					else:
						openings[game["opening"]["name"]]["user_is_white"]["losses"] += 1
				else:
					openings[game["opening"]["name"]]["user_is_white"]["draws"] += 1
				
			else:
				openings[game["opening"]["name"]]["user_is_black"]["total"] += 1
				
				if("winner" in game):
					if(game["winner"] == "black"):
						openings[game["opening"]["name"]]["user_is_black"]["wins"] += 1
					else:
						openings[game["opening"]["name"]]["user_is_black"]["losses"] += 1
				else:
					openings[game["opening"]["name"]]["user_is_black"]["draws"] += 1
				
				
		else: 
			print("opening not found")

for opening in openings.keys():
	
	if(openings[opening]["user_is_white"]["total"] <= 5 and openings[opening]["user_is_black"]["total"] <= 5):
		continue
	print(opening + ":")
	if(openings[opening]["user_is_white"]["total"] != 0):
		print("number of games played: " + 
			str(openings[opening]["user_is_white"]["total"]) +
			" with wins % as white: " + str(
			(openings[opening]["user_is_white"]["wins"] / 
				openings[opening]["user_is_white"]["total"])*100) + "%\n")
	if(openings[opening]["user_is_black"]["total"] != 0):
		print("number of games played: " + 
			str(openings[opening]["user_is_black"]["total"]) +
			" with wins % as black: " + str(
			(openings[opening]["user_is_black"]["wins"] / 
				openings[opening]["user_is_black"]["total"])*100) + "%\n")
	
	
	
