from PIL import Image

# fungsi citra biner
def citra_biner(nilai_ambang):
    # konversi gambar RGB ke grayscale
    # https://stackoverflow.com/a/18778280/9157799
    CITRA_GRAYSCALE = Image.open('gambar.jpg').convert('L')
    PIXEL_GRAYSCALE = CITRA_GRAYSCALE.load()

    ukuran_horizontal = CITRA_GRAYSCALE.size[0]
    ukuran_vertikal = CITRA_GRAYSCALE.size[1]

    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            if PIXEL_GRAYSCALE[x, y] < nilai_ambang:
                PIXEL_GRAYSCALE[x, y] = 0
            else:
                PIXEL_GRAYSCALE[x, y] = 255

    nama_setelah_disave = 'gambar_biner_' + str(nilai_ambang) + '.jpg'
    CITRA_GRAYSCALE.save(nama_setelah_disave)


citra_biner(50)
citra_biner(128)
citra_biner(200)
citra_biner(230)
