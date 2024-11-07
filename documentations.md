**Penggunaan**
--------------

Untuk menggunakan library ini, kamu perlu membuat instance dari kelas `GoogleDork` dan memanggil metode `search()` untuk melakukan pencarian.

### Konstruktor

`GoogleDork` memiliki konstruktor yang membutuhkan beberapa parameter:

* `domain`: Domain yang ingin dicari (opsional)
* `filetype`: Jenis file yang ingin dicari (opsional)
* `intext`: Teks yang ingin dicari dalam konten halaman (opsional)
* `intitle`: Teks yang ingin dicari dalam judul halaman (opsional)
* `inurl`: Teks yang ingin dicari dalam URL halaman (opsional)

Contoh:
```python
dork = GoogleDork(
    domain="example.com",
    filetype="pdf",
    intext="konten yang dicari",
    intitle="judul yang dicari",
    inurl="url yang dicari"
)
```
### Metode Search

Metode `search()` melakukan pencarian menggunakan dork yang telah ditentukan dan mengembalikan hasil pencarian dalam bentuk daftar.

Contoh:
```python
results = dork.search()
```
### Metode Display Results

Metode `display_results()` menampilkan hasil pencarian dalam bentuk yang lebih mudah dibaca.

Contoh:
```python
dork.display_results(results)
```
**Contoh Penggunaan**
----------------------

Berikut adalah contoh penggunaan library ini:
```python
import argparse
from google_dork import GoogleDork

parser = argparse.ArgumentParser()
parser.add_argument("--domain", help="Domain yang ingin dicari")
parser.add_argument("--filetype", help="Jenis file yang ingin dicari")
parser.add_argument("--intext", help="Teks yang ingin dicari dalam konten halaman")
parser.add_argument("--intitle", help="Teks yang ingin dicari dalam judul halaman")
parser.add_argument("--inurl", help="Teks yang ingin dicari dalam URL halaman")

args = parser.parse_args()

dork = GoogleDork(
    domain=args.domain,
    filetype=args.filetype,
    intext=args.intext,
    intitle=args.intitle,
    inurl=args.inurl
)

results = dork.search()
dork.display_results(results)
```
