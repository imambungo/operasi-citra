from PIL import Image

# konversi gambar RGB ke Pencerahan

CITRA = Image.open('gambar.jpg')

ukuran_horizontal = CITRA.size[0]
ukuran_vertikal = CITRA.size[1]

PIXEL = CITRA.load()
temp = 30
for x in range(ukuran_horizontal):
    for y in range(ukuran_vertikal):

        R = PIXEL[x, y][0] + temp
        if R < 0:
                R = 0
            
        else:
            if R > 255:
                R = 255
        
            else:
                R = R
        G = PIXEL[x, y][1] + temp
        if G < 0:
                G = 0
            
        else:
            if G > 255:
                G = 255
        
            else:
                G = G
        B = PIXEL[x, y][2] + temp
        if B < 0:
                B = 0
            
        else:
            if B > 255:
                B = 255
        
            else:
                B = B
        
        PIXEL[x, y] = (R, G, B)

CITRA.save('gambar_pencerahan.jpg')

