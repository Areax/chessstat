from parse import *
import re
import os


openingEco = {'E87': "King's Indian defence", 'E69': "King's Indian defence", 'E94': "King's Indian defence", 'E95': "King's Indian defence", 'E84': "King's Indian defence",
              'E74': "King's Indian defence", 'E70': "King's Indian defence", 'E97': "King's Indian defence", 'E92': "King's Indian defence", 'E67': "King's Indian defence",
              'E76': "King's Indian defence", 'E64': "King's Indian defence", 'E61': "King's Indian defence", 'E85': "King's Indian defence", 'E99': "King's Indian defence",
              'E86': "King's Indian defence", 'E60': "King's Indian defence", 'E77': "King's Indian defence", 'E93': "King's Indian defence", 'E63': "King's Indian defence",
              'E78': "King's Indian defence", 'E72': "King's Indian defence", 'E75': "King's Indian defence", 'E83': "King's Indian defence", 'E68': "King's Indian defence",
              'E96': "King's Indian defence", 'E90': "King's Indian defence", 'E65': "King's Indian defence", 'E88': "King's Indian defence", 'E89': "King's Indian defence",
              'E73': "King's Indian defence", 'E98': "King's Indian defence", 'E66': "King's Indian defence", 'E91': "King's Indian defence", 'E71': "King's Indian defence",
              'E79': "King's Indian defence", 'E81': "King's Indian defence", 'E82': "King's Indian defence", 'E80': "King's Indian defence", 'E62': "King's Indian defence",
              'E48': 'Nimzo-Indian defence', 'E50': 'Nimzo-Indian defence', 'E52': 'Nimzo-Indian defence',
              'E56': 'Nimzo-Indian defence', 'E36': 'Nimzo-Indian defence', 'E55': 'Nimzo-Indian defence',
              'E28': 'Nimzo-Indian defence', 'E44': 'Nimzo-Indian defence', 'E26': 'Nimzo-Indian defence',
              'E38': 'Nimzo-Indian defence', 'E29': 'Nimzo-Indian defence', 'E30': 'Nimzo-Indian defence',
              'E21': 'Nimzo-Indian defence', 'E34': 'Nimzo-Indian defence', 'E32': 'Nimzo-Indian defence',
              'E53': 'Nimzo-Indian defence', 'E37': 'Nimzo-Indian defence', 'E47': 'Nimzo-Indian defence',
              'E58': 'Nimzo-Indian defence', 'E49': 'Nimzo-Indian defence', 'E51': 'Nimzo-Indian defence',
              'E59': 'Nimzo-Indian defence', 'E57': 'Nimzo-Indian defence', 'E45': 'Nimzo-Indian defence',
              'E46': 'Nimzo-Indian defence', 'E43': 'Nimzo-Indian defence', 'E22': 'Nimzo-Indian defence',
              'E35': 'Nimzo-Indian defence', 'E31': 'Nimzo-Indian defence', 'E25': 'Nimzo-Indian defence',
              'E24': 'Nimzo-Indian defence', 'E42': 'Nimzo-Indian defence', 'E41': 'Nimzo-Indian defence',
              'E23': 'Nimzo-Indian defence', 'E39': 'Nimzo-Indian defence', 'E27': 'Nimzo-Indian defence',
              'E54': 'Nimzo-Indian defence', 'E33': 'Nimzo-Indian defence', 'E40': 'Nimzo-Indian defence',
              'E20': 'Nimzo-Indian defence', 'E18': "Queen's Indian defense", 'E16': "Queen's Indian defense",
              'E17': "Queen's Indian defense", 'E14': "Queen's Indian defense", 'E15': "Queen's Indian defense",
              'E19': "Queen's Indian defense", 'E12': "Queen's Indian defense", 'E13': "Queen's Indian defense",
              'E02': 'Catalan, closed', 'E03': 'Catalan, closed', 'E01': 'Catalan, closed', 'E04': 'Catalan, closed',
              'E06': 'Catalan, closed', 'E07': 'Catalan, closed', 'E05': 'Catalan, closed', 'E09': 'Catalan, closed',
              'E08': 'Catalan, closed','D88': 'Gruenfeld defence', 'D92': 'Gruenfeld defence', 'D93': 'Gruenfeld defence',
              'D90': 'Gruenfeld defence', 'D91': 'Gruenfeld defence', 'D85': 'Gruenfeld defence', 'D95': 'Gruenfeld defence',
              'D94': 'Gruenfeld defence', 'D87': 'Gruenfeld defence', 'D86': 'Gruenfeld defence', 'D89': 'Gruenfeld defence', 'D97': 'Gruenfeld defence', 'D84': 'Gruenfeld defence',
              'D96': 'Gruenfeld defence', 'D99': 'Gruenfeld defence',
              'D98': 'Gruenfeld defence', 'D83': 'Gruenfeld defence', 'D81': 'Gruenfeld defence', 'D80': 'Gruenfeld defence', 'D82': 'Gruenfeld defence',
              'D74': 'Neo-Gruenfeld defence', 'D71': 'Neo-Gruenfeld defence', 'D76': 'Neo-Gruenfeld defence', 'D77': 'Neo-Gruenfeld defence', 'D72': 'Neo-Gruenfeld defence',
              'D75': 'Neo-Gruenfeld defence', 'D70': 'Neo-Gruenfeld defence', 'D79': 'Neo-Gruenfeld defence', 'D73': 'Neo-Gruenfeld defence', 'D78': 'Neo-Gruenfeld defence',
              'D62': "Queen's Gambit Declined", 'D53': "Queen's Gambit Declined", 'D61': "Queen's Gambit Declined", 'D64': "Queen's Gambit Declined",
              'D54': "Queen's Gambit Declined", 'D59': "Queen's Gambit Declined", 'D68': "Queen's Gambit Declined",
              'D51': "Queen's Gambit Declined", 'D50': "Queen's Gambit Declined", 'D58': "Queen's Gambit Declined", 'D56': "Queen's Gambit Declined",
              'D69': "Queen's Gambit Declined", 'D55': "Queen's Gambit Declined", 'D67': "Queen's Gambit Declined", 'D52': "Queen's Gambit Declined",
              'D57': "Queen's Gambit Declined", 'D65': "Queen's Gambit Declined", 'D63': "Queen's Gambit Declined", 'D66': "Queen's Gambit Declined",
              'D60': "Queen's Gambit Declined", 'D44': "Queen's Gambit Declined semi-Slav", 'D46': "Queen's Gambit Declined semi-Slav", 'D47': "Queen's Gambit Declined semi-Slav",
              'D45': "Queen's Gambit Declined semi-Slav", 'D49': "Queen's Gambit Declined semi-Slav", 'D43': "Queen's Gambit Declined semi-Slav", 'D48': "Queen's Gambit Declined semi-Slav",
              'D41': "Queen's Gambit Declined", 'D35': "Queen's Gambit Declined", 'D37': "Queen's Gambit Declined", 'D34': "Queen's Gambit Declined", 'D30': "Queen's Gambit Declined",
              'D38': "Queen's Gambit Declined", 'D39': "Queen's Gambit Declined", 'D33': "Queen's Gambit Declined", 'D31': "Queen's Gambit Declined", 'D40': "Queen's Gambit Declined",
              'D36': "Queen's Gambit Declined", 'D32': "Queen's Gambit Declined", 'D42': "Queen's Gambit Declined", 'D21': "Queen's Gambit Accepted", 'D20': "Queen's Gambit Accepted", 'D28': "Queen's Gambit Accepted", 'D24': "Queen's Gambit Accepted", 'D25': "Queen's Gambit Accepted", 'D26': "Queen's Gambit Accepted", 'D27': "Queen's Gambit Accepted",
              'D23': "Queen's Gambit Accepted", 'D29': "Queen's Gambit Accepted", 'D22': "Queen's Gambit Accepted",
              'D17': "Queen's Gambit Declined Slav, Czech defence", 'D18': "Queen's Gambit Declined Slav, Czech defence",
              'D19': "Queen's Gambit Declined Slav, Czech defence",'D14': "Queen's Gambit Declined Slav defence", 'D11': "Queen's Gambit Declined Slav defence",
              'D13': "Queen's Gambit Declined Slav defence", 'D15': "Queen's Gambit Declined Slav defence", 'D12': "Queen's Gambit Declined Slav defence",
              'D10': "Queen's Gambit Declined Slav defence", 'D07': "Queen's Gambit Declined, Chigorin defence", 'D08': "Queen's Gambit Declined, Chigorin defence",
              'D09': "Queen's Gambit Declined, Chigorin defence", 'D05': "Queen's pawn game", 'D04': "Queen's pawn game", 'C88': 'Ruy Lopez (Spanish opening)', 'C99': 'Ruy Lopez (Spanish opening)', 'C70': 'Ruy Lopez (Spanish opening)', 'C82': 'Ruy Lopez (Spanish opening)', 'C96': 'Ruy Lopez (Spanish opening)', 'C95': 'Ruy Lopez (Spanish opening)', 'C91': 'Ruy Lopez (Spanish opening)', 'C67': 'Ruy Lopez (Spanish opening)', 'C81': 'Ruy Lopez (Spanish opening)', 'C61': 'Ruy Lopez (Spanish opening)', 'C68': 'Ruy Lopez (Spanish opening)', 'C80': 'Ruy Lopez (Spanish opening)', 'C87': 'Ruy Lopez (Spanish opening)', 'C94': 'Ruy Lopez (Spanish opening)', 'C73': 'Ruy Lopez (Spanish opening)', 'C84': 'Ruy Lopez (Spanish opening)', 'C69': 'Ruy Lopez (Spanish opening)', 'C98': 'Ruy Lopez (Spanish opening)', 'C63': 'Ruy Lopez (Spanish opening)', 'C93': 'Ruy Lopez (Spanish opening)', 'C86': 'Ruy Lopez (Spanish opening)', 'C60': 'Ruy Lopez (Spanish opening)', 'C76': 'Ruy Lopez (Spanish opening)', 'C66': 'Ruy Lopez (Spanish opening)', 'C83': 'Ruy Lopez (Spanish opening)', 'C89': 'Ruy Lopez (Spanish opening)', 'C85': 'Ruy Lopez (Spanish opening)', 'C71': 'Ruy Lopez (Spanish opening)', 'C72': 'Ruy Lopez (Spanish opening)', 'C75': 'Ruy Lopez (Spanish opening)', 'C78': 'Ruy Lopez (Spanish opening)', 'C97': 'Ruy Lopez (Spanish opening)', 'C92': 'Ruy Lopez (Spanish opening)', 'C62': 'Ruy Lopez (Spanish opening)', 'C64': 'Ruy Lopez (Spanish opening)', 'C77': 'Ruy Lopez (Spanish opening)', 'C74': 'Ruy Lopez (Spanish opening)',
              'C79': 'Ruy Lopez (Spanish opening)', 'C90': 'Ruy Lopez (Spanish opening)', 'C65': 'Ruy Lopez (Spanish opening)',
              'C57': 'Two knights defence', 'C55': 'Two knights defence', 'C56': 'Two knights defence', 'C58': 'Two knights defence', 'C59': 'Two knights defence',
              'C54': 'Giuoco Piano', 'C53': 'Giuoco Piano', 'C52': 'Evans gambit', 'C51': 'Evans gambit','C47': 'Four knights, Scotch variation',
              'C48': 'Four knights, Scotch variation', 'C49': 'Four knights, Scotch variation', 'C43': "Petrov's defence", 'C42': "Petrov's defence","C40" :"King's knight opening",
            'C41' :"Philidor's defence",
            "C44" :"King's pawn game",
            "C45" :"Scotch game",
            "C46" :"Three knights game",
            "C50" :"King's pawn game",
            "D00" :"Queen's pawn game",
            "D01" :"Richter-Veresov attack",
            "D02" :"Queen's pawn game",
            "D03" :"Torre attack (Tartakower variation)",
            "D06" :"Queen's Gambit",
            "D16": "Queen's Gambit Declined Slav accepted, Alapin variation",
            'E00': "Queen's pawn game",
            'E10': "Queen's pawn game",
            'E11' :"Bogo-Indian defence",'C31': "King's gambit", 'C33': "King's gambit",
              'C39': "King's gambit", 'C35': "King's gambit", 'C38': "King's gambit", 'C30': "King's gambit", 'C34': "King's gambit", 'C37': "King's gambit", 'C32': "King's gambit",
              'C36': "King's gambit", 'C28': 'Vienna game', 'C29': 'Vienna game', 'C27': 'Vienna game', 'C25': 'Vienna game', 'C26': 'Vienna game',
              'C23': "Bishop's opening", 'C24': "Bishop's opening", 'C21': 'Centre game', 'C22': 'Centre game','C05': 'French defence', 'C11': 'French defence', 'C10': 'French defence', 'C04': 'French defence', 'C13': 'French defence', 'C16': 'French defence', 'C18': 'French defence', 'C00': 'French defence', 'C17': 'French defence', 'C06': 'French defence', 'C01': 'French defence', 'C02': 'French defence', 'C08': 'French defence', 'C15': 'French defence', 'C14': 'French defence', 'C19': 'French defence', 'C09': 'French defence', 'C07': 'French defence', 'C03': 'French defence', 'C12': 'French defence',
              'B32': 'Sicilian defence', 'B70': 'Sicilian defence', 'B31': 'Sicilian defence', 'B88': 'Sicilian defence', 'B26': 'Sicilian defence',
              'B45': 'Sicilian defence', 'B49': 'Sicilian defence', 'B81': 'Sicilian defence', 'B20': 'Sicilian defence', 'B99': 'Sicilian defence',
              'B52': 'Sicilian defence', 'B42': 'Sicilian defence', 'B63': 'Sicilian defence', 'B84': 'Sicilian defence', 'B27': 'Sicilian defence',
              'B87': 'Sicilian defence', 'B56': 'Sicilian defence', 'B55': 'Sicilian defence', 'B97': 'Sicilian defence', 'B67': 'Sicilian defence',
              'B37': 'Sicilian defence', 'B91': 'Sicilian defence', 'B28': 'Sicilian defence', 'B73': 'Sicilian defence', 'B44': 'Sicilian defence',
              'B71': 'Sicilian defence', 'B62': 'Sicilian defence', 'B74': 'Sicilian defence', 'B48': 'Sicilian defence', 'B89': 'Sicilian defence',
              'B36': 'Sicilian defence', 'B80': 'Sicilian defence', 'B75': 'Sicilian defence', 'B93': 'Sicilian defence', 'B77': 'Sicilian defence',
              'B29': 'Sicilian defence', 'B98': 'Sicilian defence', 'B43': 'Sicilian defence', 'B33': 'Sicilian defence', 'B25': 'Sicilian defence',
              'B66': 'Sicilian defence', 'B53': 'Sicilian defence', 'B61': 'Sicilian defence', 'B22': 'Sicilian defence', 'B95': 'Sicilian defence',
              'B76': 'Sicilian defence', 'B69': 'Sicilian defence', 'B79': 'Sicilian defence', 'B92': 'Sicilian defence', 'B85': 'Sicilian defence',
              'B82': 'Sicilian defence', 'B57': 'Sicilian defence', 'B51': 'Sicilian defence', 'B86': 'Sicilian defence', 'B64': 'Sicilian defence',
              'B40': 'Sicilian defence', 'B94': 'Sicilian defence', 'B38': 'Sicilian defence', 'B65': 'Sicilian defence', 'B96': 'Sicilian defence',
              'B54': 'Sicilian defence', 'B90': 'Sicilian defence', 'B60': 'Sicilian defence', 'B34': 'Sicilian defence', 'B58': 'Sicilian defence',
              'B68': 'Sicilian defence', 'B47': 'Sicilian defence', 'B30': 'Sicilian defence', 'B24': 'Sicilian defence', 'B23': 'Sicilian defence',
              'B39': 'Sicilian defence', 'B83': 'Sicilian defence', 'B21': 'Sicilian defence', 'B35': 'Sicilian defence', 'B72': 'Sicilian defence',
              'B78': 'Sicilian defence', 'B41': 'Sicilian defence', 'B50': 'Sicilian defence', 'B46': 'Sicilian defence', 'B59': 'Sicilian defence',
              'B17': 'Caro-Kann defence', 'B11': 'Caro-Kann defence', 'B12': 'Caro-Kann defence', 'B10': 'Caro-Kann defence', 'B16': 'Caro-Kann defence', 'B13': 'Caro-Kann defence',
              'B14': 'Caro-Kann defence', 'B19': 'Caro-Kann defence', 'B15': 'Caro-Kann defence', 'B18': 'Caro-Kann defence','B05': "Alekhine's defence",
              'B02': "Alekhine's defence", 'B03': "Alekhine's defence", 'B04': "Alekhine's defence",'B08': 'Pirc defence', 'B07': 'Pirc defence', 'B09': 'Pirc defence',
              'A95': 'Dutch', 'A84': 'Dutch', 'A80': 'Dutch', 'A85': 'Dutch', 'A94': 'Dutch', 'A92': 'Dutch', 'A97': 'Dutch', 'A93': 'Dutch', 'A83': 'Dutch', 'A98': 'Dutch', 'A90': 'Dutch', 'A99': 'Dutch',
              'A82': 'Dutch', 'A89': 'Dutch', 'A96': 'Dutch', 'A91': 'Dutch', 'A86': 'Dutch', 'A87': 'Dutch', 'A81': 'Dutch', 'A88': 'Dutch', 'A71': 'Benoni defence', 'A69': 'Benoni defence', 'A60': 'Benoni defence',
              'A77': 'Benoni defence', 'A63': 'Benoni defence', 'A64': 'Benoni defence', 'A70': 'Benoni defence', 'A65': 'Benoni defence', 'A79': 'Benoni defence', 'A66': 'Benoni defence', 'A72': 'Benoni defence', 'A68': 'Benoni defence',
              'A73': 'Benoni defence', 'A75': 'Benoni defence', 'A67': 'Benoni defence', 'A78': 'Benoni defence', 'A61': 'Benoni defence', 'A62': 'Benoni defence', 'A76': 'Benoni defence', 'A74': 'Benoni defence',
              'A57': 'Benko gambit', 'A59': 'Benko gambit', 'A58': 'Benko gambit','A55': 'Old Indian defence', 'A54': 'Old Indian defence', 'A53': 'Old Indian defence','A51': 'Budapest defence', 'A52': 'Budapest defence',
              'A49': "King's Indian, East Indian defence", 'A48': "King's Indian, East Indian defence",'A46': "Queen's pawn game", 'A45': "Queen's pawn game",'A44': 'Old Benoni defence',
              'A43': 'Old Benoni defence','A41': "Queen's pawn", 'A40': "Queen's pawn", 'A16': 'English opening', 'A30': 'English opening', 'A13': 'English opening', 'A11': 'English opening', 'A32': 'English opening',
              'A36': 'English opening', 'A31': 'English opening', 'A10': 'English opening', 'A15': 'English opening', 'A29': 'English opening', 'A14': 'English opening', 'A39': 'English opening', 'A24': 'English opening', 'A22': 'English opening', 'A26': 'English opening', 'A27': 'English opening', 'A28': 'English opening', 'A18': 'English opening', 'A12': 'English opening', 'A21': 'English opening', 'A19': 'English opening', 'A17': 'English opening', 'A34': 'English opening', 'A38': 'English opening', 'A35': 'English opening', 'A25': 'English opening', 'A20': 'English opening', 'A37': 'English opening', 'A23': 'English opening', 'A33': 'English opening',
              'A09': 'Reti opening', 'A05': 'Reti opening', 'A04': 'Reti opening', 'A08': 'Reti opening', 'A06': 'Reti opening', 'A07': 'Reti opening','A02': "Bird's opening", 'A03': "Bird's opening", "A00":"Polish (Sokolsky) opening",
            "A01":"Nimzovich-Larsen attack",
            "A42":"Modern defence Averbakh system",
            "A47":"Queen's Indian defence",
            "A50":"Queen's pawn game",
            "A56":"Benoni defence",
            "B00": "King's pawn opening",
            "B01": "Scandinavian (centre counter)",
            "B06":"Robatsch (modern) defence",
            "C20": "King's  pawn game",

}


Alekhine = open('Alekhine.pgn','r').read()
Anand = open('Anand.pgn', 'r').read()
Capablanca = open('Capablanca.pgn', 'r').read()
Carlsen = open('Carlsen.pgn', 'r').read()
Fischer = open('Fischer.pgn', 'r').read()
Karpov = open('Karpov.pgn', 'r').read()
Kasparov = open('Kasparov.pgn', 'r').read()
Morphy = open('Morphy.pgn', 'r').read()


r=0
z=0


def eco_find(j,playername):
    pgnList = []
    pgnA = ''
    global z
    file = open('ChessGames.sql', 'w')
    file.write('USE chess_games;')
    for pgn in j.splitlines():

        if pgn == "":
            continue
        if pgn[0] == '[':
            if len(pgnA) >=1:
                pgnList.append(pgnA)
                pgnA=''
            continue
        else:
            pgnA += " " + pgn
    pgnList.append(pgnA)


    for c in re.findall(r'\[([^]]*)\]', j):

        global r

        if "Date" in c:
            GameYear = c[6:10]   # grabs the year

             # grabs opening code

        if "Result" in c and "1/2" not in c:  #  result
            result = c[8:9]

        if "Result" in c and "1/2" in c:
            result = "3"

        if "Result" in c and "*" in c:
            result = "4"

        if "White" in c and "Elo" not in c:   # Players color
            if playername in c:
                color="White"
            else:
                color = "Black"
            if playername not in c:
                opponentname1=(c[7:-1]).replace(",", "").replace("'","").replace(".", "")
                opponentname = re.sub('[^0-9a-zA-Z]+', ' ', opponentname1)


        if "Black" in c and "Elo" not in c:   # opponent name
            if playername in c:
                color ="Black"
            else:
                color = "White"
            if playername[2:6] not in c:
                opponentname1 = (c[7:-1]).replace(",", "").replace("'","").replace(".", "")
                opponentname = re.sub('[^0-9a-zA-Z]+', ' ', opponentname1)

        if "ECO" in c:
            Opening = openingEco[c[5:8]].replace("'", "").replace(".", "")
            file.write('INSERT INTO Games (PlayerName, OpponentsName, Color, Result, GameYear, Opening, PGN ) VALUES (' + "'"+ playername + "'" + ','+"'" + opponentname +"'"+ ","+ "'" + " " + color + "'"+"," + "'"+str(result)+"'"+ "," + "'" + GameYear + "'"+ "," +"'"+ Opening + "'"+"," + "'" + pgnList[z] +"'" + ");")
            # print('INSERT INTO Games (PlayerName, OpponentsName, Color, Result, GameYear, Opening, PGN ) VALUES (' + "'"+ playername + "'" + ','+"'" + opponentname +"'"+ ","+ "'" + " " + color + "'"+"," + "'"+str(result)+"'"+ "," + "'" + GameYear + "'"+ "," +"'"+ Opening + "'"+"," + "'" + pgnList[z] +"'" + ");")

            z += 1
    z=0
    print("Please enter password to finish uploading "+ playername + " games to database:")
    file.close()
    os.system("mysql -u root -p < ChessGames.sql")

eco_find(Alekhine, "Alexander Alekhine")
eco_find(Capablanca, "Capablanca Jose Raul")
eco_find(Anand, "Anand Viswanathan")
eco_find(Carlsen, "Carlsen Magnus")
eco_find(Fischer, "Fischer Robert James")
eco_find(Karpov, "Karpov Anatoly")
eco_find(Kasparov, "Kasparov Gary")
eco_find(Morphy, "Morphy Paul")
