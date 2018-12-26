import os
import sys
import requests

import dota2api


STEAM_KEY = 'your_steam_key'


if __name__ == "__main__":
	api = dota2api.Initialise(STEAM_KEY)

	prefix = "images/"

	heroes = api.get_heroes()

	for hero in heroes["heroes"]:
		url = hero["url_full_portrait"]
		title = hero["name"]
		id = hero["id"]

		path = os.path.join(prefix, "{}_{}.png".format(title, id))
		
		img = requests.get(url)
		out = open(path, "wb")
		out.write(img.content)
		out.close

		print("Saving {} portrait as {}".format(title, path))


