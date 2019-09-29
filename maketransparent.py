# https://stackoverflow.com/a/765774/9157799

from PIL import Image

img = Image.open('itachi3.jpg')
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] > 50 and item[1] > 50 and item[2] > 50:
        newData.append((255, 255, 255, 0))
    else:
        newData.append((19, 36, 46))

img.putdata(newData)
img.save("itachi.png", "PNG")
