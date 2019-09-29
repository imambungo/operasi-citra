from PIL import Image

CITRA = Image.open('gambar.jpg')
PIXEL = CITRA.load()

# cara mengakses aras titik
x = 3
y = 8
print(PIXEL[x, y])   # nilai RGB dari pixel (x, y)
print(PIXEL[x, y][0])  # nilai R dari pixel (x, y)
print(PIXEL[x, y][1])  # nilai G dari pixel (x, y)
print(PIXEL[x, y][2])  # nilai B dari pixel (x, y)
