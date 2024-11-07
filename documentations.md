**Menggunakan Modul GoogleDork**
=============================

**Impor Modul**
---------------

Untuk menggunakan modul GoogleDork, Anda perlu mengimpornya terlebih dahulu:
```python
from google_dork import GoogleDork
```
**Membuat Instans GoogleDork**
-----------------------------

Untuk menggunakan modul GoogleDork, Anda perlu membuat instans dari kelas `GoogleDork`. Anda dapat membuat instans dengan beberapa parameter opsional:

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
**Metode Search**
-----------------

Metode `search()` melakukan pencarian menggunakan dork yang telah ditentukan dan mengembalikan hasil pencarian dalam bentuk daftar.

Contoh:
```python
results = dork.search()
```
**Metode Display Results**
-------------------------

Metode `display_results()` menampilkan hasil pencarian dalam bentuk yang lebih mudah dibaca.

Contoh:
```python
dork.display_results(results)
```
**Contoh Penggunaan**
----------------------

Berikut adalah contoh penggunaan modul GoogleDork:
```python
from google_dork import GoogleDork

dork = GoogleDork(
    domain="example.com",
    filetype="pdf",
    intext="konten yang dicari",
    intitle="judul yang dicari",
    inurl="url yang dicari"
)

results = dork.search()
dork.display_results(results)
```
