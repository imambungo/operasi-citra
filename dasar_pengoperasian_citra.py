from PIL import Image

CITRA = Image.open('gambar.jpg')
PIXEL = CITRA.load()

print(CITRA.size)
ukuran_horizontal = CITRA.size[0]
ukuran_vertikal = CITRA.size[1]
print(ukuran_horizontal)
print(ukuran_vertikal)

# konversi gambar RGB ke grayscale
# https://stackoverflow.com/a/18778280/9157799
CITRA_GRAYSCALE = Image.open('gambar.jpg').convert('L')

# save gambar hasil konversi
CITRA_GRAYSCALE.save('gambar_grayscale.jpg')
