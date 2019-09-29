from PIL import Image

CITRA = Image.open('gambar1.jpg')
PIXEL = CITRA.load()

print(CITRA.size)
ukuran_horizontal = CITRA.size[0]
ukuran_vertikal = CITRA.size[1]
print(ukuran_horizontal)
print(ukuran_vertikal)

# konversi gambar RGB ke grayscale
# https://stackoverflow.com/a/18778280/9157799
CITRA_GRAYSCALE = Image.open('gambar1.jpg').convert('L')

# save gambar hasil konversi
CITRA_GRAYSCALE.save('gambar2.jpg')

PIXEL_GRAYSCALE = CITRA_GRAYSCALE.load()

for x in range(ukuran_horizontal):
    for y in range(ukuran_vertikal):
        if PIXEL_GRAYSCALE[x, y] < 128:
            PIXEL_GRAYSCALE[x, y] = 0
        else:
            PIXEL_GRAYSCALE[x, y] = 255

CITRA_GRAYSCALE.save('gambar3.jpg')
