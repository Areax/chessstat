from pathlib import Path
import json
import re
import sys

USERNAME = input('chess.com username: ')
games = json.loads(Path('allGames.pgn').read_text())

seen_games = {}

pgn_info = {}
counter = 0;

openings = json.loads(Path('dictOfOpenings.txt').read_text())
opening_keys = sorted(list(openings.keys()), key=len)
opening_keys.reverse()
#print(opening_keys)

g_opening = []
g_won = []
g_draw = []
g_lost = []
g_c = 0




for game in games["games"]:
	if(not "pgn" in game):
		continue	
	pgn = game["pgn"].split("\n")
	pgn_game = 0
	pgn_info[counter] = {}
	for line in pgn:
		key_value = line.split(" ", 1)
		if(len(key_value) == 1):
			pgn_game = 1
			continue
		if(pgn_game == 1):
			#game found
			temp = re.sub(r'\{.+?\} ', '', game["pgn"])
			pgn_info[counter]["pgn"] = re.sub(r' [0-9]+\.\.\.', '', temp)
			#print(pgn_info[counter]["pgn"])
			
			for key in opening_keys:
				if(key in pgn_info[counter]["pgn"]):
					pgn_info[counter]["Opening"] = openings[key]
					#print(openings[key])
					#will be more than one
					break
			break
		else:
			pgn_info[counter][key_value[0][1:]] = re.search(r'\"(.*)\"', key_value[1]).group()
	counter += 1

online_pgns = open('test.txt', 'w')
online_pgns.write(json.dumps(pgn_info, indent=4, sort_keys=True))
online_pgns.close()


for key in pgn_info.keys():
	if(pgn_info[key]):
		if(not(pgn_info[key]["Opening"] in seen_games)):
			seen_games[pgn_info[key]["Opening"]] = {
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
			
		print()
		is_white = games["games"][key]["white"]["username"].lower() == USERNAME
		if(is_white):
			seen_games[pgn_info[key]["Opening"]]["user_is_white"]["total"] += 1
			
			if("win" == games["games"][key]["white"]["result"]):
				seen_games[pgn_info[key]["Opening"]]["user_is_white"]["wins"] += 1
			elif("draw" == games["games"][key]["white"]["result"]):
				seen_games[pgn_info[key]["Opening"]]["user_is_white"]["draws"] += 1
			else:
				seen_games[pgn_info[key]["Opening"]]["user_is_white"]["losses"] += 1
			
		else:
			seen_games[pgn_info[key]["Opening"]]["user_is_black"]["total"] += 1
			
			if("win" == games["games"][key]["black"]["result"]):
				seen_games[pgn_info[key]["Opening"]]["user_is_black"]["wins"] += 1
			elif("draw" == games["games"][key]["black"]["result"]):
				seen_games[pgn_info[key]["Opening"]]["user_is_black"]["draws"] += 1
			else:
				seen_games[pgn_info[key]["Opening"]]["user_is_black"]["losses"] += 1
			
			
	else: 
		print("opening not found")

for opening in seen_games.keys():
	print(opening + ":")
	if(seen_games[opening]["user_is_white"]["total"] != 0):
		print("number of games played: " + 
			str(seen_games[opening]["user_is_white"]["total"]) +
			" with wins % as white: " + str(
			(seen_games[opening]["user_is_white"]["wins"] / 
				seen_games[opening]["user_is_white"]["total"])*100) + "%\n")
	if(seen_games[opening]["user_is_black"]["total"] != 0):
		print("number of games played: " + 
			str(seen_games[opening]["user_is_black"]["total"]) +
			" with wins % as black: " + str(
			(seen_games[opening]["user_is_black"]["wins"] / 
				seen_games[opening]["user_is_black"]["total"])*100) + "%\n")

				
def create_graph():
	false_c = 0
	for g_keys in seen_games.keys():
		false_c += 1
		if(false_c == 3):
			break
		g_opening.append("White: " + g_keys)
		g_won.append(seen_games[g_keys]["user_is_white"]["wins"])
		g_lost.append(seen_games[g_keys]["user_is_white"]["losses"])
		g_draw.append(seen_games[g_keys]["user_is_white"]["draws"])
		
		g_opening.append("Black: " + g_keys)
		g_won.append(seen_games[g_keys]["user_is_black"]["wins"])
		g_lost.append(seen_games[g_keys]["user_is_black"]["losses"])
		g_draw.append(seen_games[g_keys]["user_is_black"]["draws"])
		
		
	import piePlots as plot
	plot.graph(g_opening, g_won, g_lost, g_draw)
	
	
	
	
	
def get_path_from_info(info, gametype):
    """
    Determines, from the given game information, where
    its PGN file would be saved and returns its
    expected location.
    
    The path returned would be
    `type/subtype/year/month`, where "type" is either
    "live" or "correspondence", and the subtype is either
    "chess960" or "standard" for correspondence games
    or "bullet", "blitz", or "standard" for live games.
    """

    path = ""

    if gametype == 'echess':
        if info["is960"] == True: # if this is a 960 game
            path = "/correspondence/chess960"
        else:
            path = "/correspondence/standard"
                        
    elif gametype == 'live_bullet':
        path = "/live/bullet"
                    
    elif gametype == 'live_blitz':
        path = "/live/blitz"
                    
    elif gametype == 'live_standard':
        path = "/live/standard"
        
    # Add the year and month to the end of the path
    path = "{0}/{1}/{2}".format(path, info['year'], info['month']) 
        
    return path

	
