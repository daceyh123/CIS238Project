Worksheet

if container.find("span", {"class": "form rating ut19 icon gold rare"}) is not None:
	rating = container.find("span", {"class": "form rating ut19 icon gold rare"}).text
else if: container.find("span", {"class": "form rating ut19  gold rare"}) is not None:
	rating = container.find("span", {"class": "form rating ut19  gold rare"}).text
else if: container.find("span", {"class": "form rating ut19 ucl_rare gold rare"}) is not None:
	rating = container.find("span", {"class": "form rating ut19 ucl_rare gold rare"}).text
else:
	rating = "None"









if container.find("span", {"class": "form rating ut19 icon gold rare"}) is None or container.find("span", {"class": "form rating ut19 icon gold rare"}) == 0:

			rating = "None"