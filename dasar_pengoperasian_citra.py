from PIL import Image

CITRA = Image.open('gambar1.jpg')
PIXEL = CITRA.load()

print(CITRA.size)
print(CITRA.size[0])  # ukuran horizontal
print(CITRA.size[1])  # ukuran vertikal
