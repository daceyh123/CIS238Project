import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uOpen
from urllib.request import Request

filename = "playersFutbin.csv"
f = open(filename, "w")

headers = "player, rating, price\n"

f.write(headers)

i = 1
while i < 3:

	my_url = 'https://www.futbin.com/19/players?page=' + str(i)

	pgdownload = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})

	page_html = uOpen(pgdownload).read()
	uOpen(pgdownload).close()

	page_soup = soup(page_html, "html.parser")

	containers = page_soup.findAll("tr", {"class": "player_tr_1"})
	containers2 = page_soup.findAll("tr", {"class": "player_tr_2"})
	containers.extend(containers2)

	for container in containers:

		player_name = container.find("a", {"class": "player_name_players_table"}).text

		if container.find("span", {"class": "form rating ut19 icon gold rare"}) is not None:
			rating = container.find("span", {"class": "form rating ut19 icon gold rare"}).text
		elif container.find("span", {"class": "form rating ut19 gold rare"}) is not None:
			rating = container.find("span", {"class": "form rating ut19 gold rare"}).text
		elif container.find("span", {"class": "form rating ut19 ucl_rare gold rare"}) is not None:
			rating = container.find("span", {"class": "form rating ut19 ucl_rare gold rare"}).text
		elif container.find("span", {"class": "form rating ut19 if gold rare"}) is not None:
			rating = container.find("span", {"class": "form rating ut19 if gold rare"}).text
		else:
			rating = "None"

		price = container.find("span", {"class": "ps4_color font-weight-bold"}).text.strip()

		f.write(player_name + "," + rating + "," + price + "\n")
	i += 1

f.close()
	