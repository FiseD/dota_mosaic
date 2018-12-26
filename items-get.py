import os
import sys
import requests

import dota2api


STEAM_KEY = 'your_steam_key'


if __name__ == "__main__":
	api = dota2api.Initialise(STEAM_KEY)

	prefix = "images/"

	items = api.get_game_items()

	for item in items["items"]:
		url = item["url_image"]
		title = item["name"]
		id = item["id"]

		path = os.path.join(prefix, "{}_{}.png".format(title, id))

		img = requests.get(url)
		out = open(path, "wb")
		out.write(img.content)
		out.close

		print("Saving {} icon as {}".format(title, path))