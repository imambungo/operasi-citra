# https://stackoverflow.com/a/138260/9157799

from PIL import Image

IMAGE = Image.open('gambar1.jpg')
PIXEL = IMAGE.load()
print(IMAGE.size)
print(IMAGE.size[0])  # ukuran horizontal
print(IMAGE.size[1])
print(PIXEL[3, 8])
print(PIXEL[3, 8][0])
print(PIXEL[3, 8][1])
print(PIXEL[3, 8][2])
PIXEL[3, 8] = (23, 83, 123)

for i in range(2500):
    for j in range(2880):
        PIXEL[i, j] = (23, 83, 123)

IMAGE.save('sample2.jpg')
IMAGE = Image.open('gambar1.jpg')
PIXEL = IMAGE.load()

IMAGE2 = Image.open('sample2.jpg')
PIXEL2 = IMAGE2.load()

IMAGE.save('image3.jpg')
IMAGE3 = Image.open('image3.jpg')
PIXEL3 = IMAGE3.load()

for i in range(5120):
    for j in range(2880):
        R = PIXEL[i, j][0] - PIXEL2[i, j][0]
        G = PIXEL[i, j][1] - PIXEL2[i, j][1]
        B = PIXEL[i, j][2] - PIXEL2[i, j][2]
        if R == 0 and G == 0 and B == 0:
            PIXEL3[i, j] = (255, 255, 255)
        else:
            PIXEL3[i, j] = (R, G, B)

IMAGE3.save('image3.jpg')
