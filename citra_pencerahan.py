from PIL import Image

def clipping(intensitas):
    if intensitas < 0:
        return 0
    if intensitas > 255:
        return 255
    return intensitas

def atur_pencerahan(nilai_pencerahan, nama_setelah_disave):
    CITRA = Image.open('gambar.jpg')
    PIXEL = CITRA.load()

    ukuran_horizontal = CITRA.size[0]
    ukuran_vertikal = CITRA.size[1]

    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            R = clipping(PIXEL[x, y][0] + nilai_pencerahan)
            G = clipping(PIXEL[x, y][1] + nilai_pencerahan)
            B = clipping(PIXEL[x, y][2] + nilai_pencerahan)
            PIXEL[x, y] = (R, G, B)

    CITRA.save(nama_setelah_disave)


atur_pencerahan(80, 'gambar_dicerahkan.jpg')
atur_pencerahan(-80, 'gambar_digelapkan.jpg')
