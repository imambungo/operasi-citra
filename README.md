# Tugas Operasi-operasi Citra

Anggota:
- Defrian Afandi (09021281722075)
- Farhan Furqan (09021281722045)
- M Imam Pratama (09021281722063)

Untuk implementasi operasi-operasi citra pada program, kami menggunakan bahasa
pemrograman Python 3 dan module/library PIL/Pillow pada python.

untuk menginstall library-nya, jalankan command berikut:

```
pip3 install pillow
```

Untuk menggunakannya pada program python, masukkan snippet berikut pada bagian atas program

```python
from PIL import Image
```

Sebelum melakukan operasi terhadap citra digital, kita harus mengaksesnya dulu seperti berikut:

```python
CITRA = Image.open('gambar1.jpg')
PIXEL = CITRA.load()
```