import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uOpen
from urllib.request import Request

filename = "players.csv"
f = open(filename, "w")

headers = "player, rating, price\n"

f.write(headers)

i = 0
while i < 31:

	my_url = 'https://www.futwiz.com/en/fifa18/players?page=' + str(i)

	pgdownload = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})

	page_html = uOpen(pgdownload).read()
	uOpen(pgdownload).close()

	page_soup = soup(page_html, "html.parser")

	containers = page_soup.findAll("tr", {"class": "table-row"})


	for container in containers:
		player_name = container.p.text.strip()

		rating_container = container.find("div", {"class": "otherversion18-txt"})
		rating = rating_container.text.strip()

		price_container = container.find("td", {"width": "30"})
		price = price_container.text.strip()

		f.write(player_name + "," + rating + "," + price.replace(',', '') + "\n")
	i += 1

f.close()

