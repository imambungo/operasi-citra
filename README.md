# Tugas Operasi-operasi Citra

Anggota:
- Defrian Afandi (09021281722075)
- Farhan Furqan (09021281722045)
- M Imam Pratama (09021281722063)

## Dasar Pengoperasian Citra pada Python 3

Untuk implementasi operasi-operasi citra pada program, kami menggunakan bahasa
pemrograman Python 3 dan library PIL (Python Image Library) pada python.

untuk menginstall library-nya, jalankan command berikut:

```
pip3 install pillow
```

Untuk menggunakannya pada program python, masukkan snippet berikut pada bagian
atas program

```python
from PIL import Image
```

Sebelum melakukan operasi terhadap citra digital, kita harus mengaksesnya dulu
seperti berikut:

```python
CITRA = Image.open('gambar1.jpg')
PIXEL = CITRA.load()
```

Untuk mengetahui ukuran gambar yang akan kita olah, gunakan variable `size`
seperti berikut:

```python
print(CITRA.size)
print(CITRA.size[0])  # ukuran horizontal
print(CITRA.size[1])  # ukuran vertikal
```

Berikut contoh outputnya:

```
(5120, 2880)
5120
2880
```

Untuk mengkonversi suatu citra RGB ke grayscale, berikut caranya:

```python
# sumber: https://stackoverflow.com/a/18778280/9157799
CITRA_GRAYSCALE = Image.open('gambar1.jpg').convert('L')
```

Jika kita telah selesai melakukan operasi-operasi terhadap suatu citra, kita
perlu menyimpan hasil pengolahan citranya dengan cara berikut:

```python
CITRA_GRAYSCALE.save('gambar2.jpg')
```

## Operasi pada aras titik

Berikut cara mengakses pixel dan nilai RGB dari suatu citra:

```python
x = 3
y = 8
print(PIXEL[x, y])   # nilai RGB dari pixel (x, y)
print(PIXEL[x, y][0])  # nilai R dari pixel (x, y)
print(PIXEL[x, y][1])  # nilai G dari pixel (x, y)
print(PIXEL[x, y][2])  # nilai B dari pixel (x, y)
```

Dan berikut cara mengubah RGB dari suatu pixel:

```python
PIXEL[3, 8] = (0, 0, 0)  # mengubah pixel (3, 8) menjadi warna hitam
```

Untuk citra grayscale, berikut caranya:

```python
# jangan lupa akses pixel dari citra grayscale
PIXEL_GRAYSCALE = CITRA_GRAYSCALE.load()

PIXEL_GRAYSCALE[3, 8] = 128
print(PIXEL_GRAYSCALE[3, 8])
```
