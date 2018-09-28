import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uOpen
from urllib.request import Request

filename = "playersFuthead.csv"
f = open(filename, "w", encoding='utf-8')

headers = "player, rating, price\n"

f.write(headers)

i = 1
while i < 11:
	my_url = 'https://www.futhead.com/18/players/?page=' + str(i)

	pgdownload = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})

	page_html = uOpen(pgdownload).read()
	uOpen(pgdownload).close()

	page_soup = soup(page_html, "html.parser")

	containers = page_soup.findAll("li", {"class":"list-group-item list-group-table-row player-group-item dark-hover"})

	for container in containers:

		player_name = container.find("span", {"class":"player-name"}).text
		#fof cards
		if container.find("span", {"class":"revision-gradient shadowed font-12 fut18 gold fof"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold fof"}).text
		#tots cards 
		elif container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold tots"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold tots"}).text
 		#toty cards
		elif container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold toty"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold toty"}).text
		#World Cup cards
		elif container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold worldcup-icon"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold worldcup-icon"}).text
		#potm
		elif container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold potm"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold potm"}).text
		#icon
		elif container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold icon"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold icon"}).text
		#if
		elif container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold if"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold if"}).text
		#eumotm
		elif container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold eumotm"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold eumotm"}).text
		#ptgs
		elif container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold ptgs"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold ptgs"}).text
		#sbc-premium
		elif container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold sbc-premium"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold sbc-premium"}).text
		#world cup
		elif container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold worldcup"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold worldcup"}).text
		#gold championship
		elif container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold championship"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold championship"}).text
		#motm
		elif container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold motm"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold motm"}).text
		#fut birthday
		elif container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold fut-birthday"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold fut-birthday"}).text
		#totgs
		elif container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold totgs"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold totgs"}).text
		#otw
		elif container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold otw"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold otw"}).text
		#nif
		elif container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold nif"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold nif"}).text
		#sbc
		elif container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold sbc"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold sbc"}).text	
		#rb
		elif container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold rb"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold rb"}).text
		#futtie-winner
		elif container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold futtie-winner"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold futtie-winner"}).text
		#ptg
		elif container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold ptg"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold ptg"}).text
		#futmas
		elif container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold futmas"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold futmas"}).text
		#scream
		elif container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold scream"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold scream"}).text

		elif container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold hero"}) is not None:
			rating = container.find("span", {"class": "revision-gradient shadowed font-12 fut18 gold hero"}).text

		else:
			rating = "None"

		price = container.find("span", {"data-platform":"xb"}).text

		f.write(player_name + "," + rating + "," + price + "\n")
	i += 1
f.close()