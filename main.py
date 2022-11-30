# With Markura's help, we were able to create this abomination of an image conversion tool

import os

from PIL import Image

path = "path"
convType = ".newtype"

files = []
for root, _, covers in os.walk(path):
    for i in filter(lambda a: not a.endswith(convType), covers):
        imgPath = os.path.join(root, i)
        print(imgPath + " -> " + imgPath.split(".")[0] + convType)

# Just for flex, the program in one line :)
# list(map(lambda a: Image.open(a).convert("RGB").save(a.split(".")[0] + ".jpg"), map(lambda a: os.path.join(next(os.walk("path"))[0], a), filter(lambda a: not a.endswith(".jpg"), next(os.walk("path"))[2]))))