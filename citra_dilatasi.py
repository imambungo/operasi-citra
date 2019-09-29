from PIL import Image
from math import floor

def skala(s):
    CITRA = Image.open('gambar2.jpg')
    PIXEL = CITRA.load()

    ukuran_horizontal = CITRA.size[0]
    ukuran_vertikal = CITRA.size[1]

    ukuran_horizontal_baru = floor(ukuran_horizontal * s)
    ukuran_vertikal_baru = floor(ukuran_vertikal * s)
    
    CITRA_BARU = Image.new("RGB", (ukuran_horizontal_baru, ukuran_vertikal_baru))
    PIXEL_BARU = CITRA_BARU.load()

    for x in range(ukuran_horizontal_baru):
        for y in range(ukuran_vertikal_baru):
            x_lama = ukuran_horizontal * x / ukuran_horizontal_baru
            y_lama = ukuran_vertikal * y / ukuran_vertikal_baru
            PIXEL_BARU[x, y] = PIXEL[x_lama, y_lama]

    nama_setelah_disave = 'gambar_dilatasi_skala_' + str(s).replace('.', ',') + '.jpg'
    CITRA_BARU.save(nama_setelah_disave)


skala(0.7)
skala(1.6)
