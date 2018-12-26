import os
import sys

from PIL import Image

if __name__ == "__main__":
	img_dir = sys.argv[1]
	out_dir = sys.argv[2]

	for name in os.listdir(img_dir):
		path = os.path.join(img_dir, name)
		try:
			image = Image.open(path)
		except IOError:
			print("Image {} can not be opened".format(path))
			continue

		# crop image to square (anchor at center)
		w, h = image.size
		if w != h:
			if w > h:
				d = float(w - h) / 2
				box = (d, 0, w - d, h)
			elif h > w:
				d = float(h - w) / 2
				box = (0, d, w, h - d)

			box = map(lambda x: int(x), box)
			image = image.crop(box=box)

		# resize
		image = image.resize(size=(64, 64))

		# write imagex
		image.save(os.path.join(out_dir, name))