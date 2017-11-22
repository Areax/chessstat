from urllib.request import urlopen as uReq


from bs4 import BeautifulSoup as soup

url = "https://www.365chess.com/eco.php"

uClient = uReq(url)

page1= uClient.read()

uClient.close()

page_soup = soup(page1, "html.parser")

pgn = page_soup.findAll("div", {"class" : "opname"})
pgn1 = page_soup.findAll("div", {"id" : "opmoves"})
print(pgn[0].a, pgn1[5])

data = {}

lista=[]
listb=[]
complete={}
i=0
for a in pgn:
    title = a.string.strip()
    # data[title] = a.attrs[]
    lista.append(title)

for b in pgn1:
    title1 = b.string.strip()
    # data[title] = a.attrs[]
    listb.append(title1)

for list in lista:

    complete[listb[i]] = list
    i += 1
print (complete)