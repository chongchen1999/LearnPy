from PIL import Image

with open("data/Beauty.jpeg", "rb") as f:
    image = Image.open(f)
    image.show()