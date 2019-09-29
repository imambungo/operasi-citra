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

## Operasi pada aras titik
