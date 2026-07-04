---
judul: "Panduan Zettelkasten untuk Pemula"
tanggal: "2026-06-24"
tag:
  - panduan
  - moc
---

# 📘 Panduan Zettelkasten untuk Pemula

> [!tldr] Apa ini?
> Panduan langkah-demi-langkah menggunakan sistem Zettelkasten di vault Urban Farming. Setiap langkah disertai contoh yang bisa kamu praktikkan langsung.

---

## 🤔 Konsep Dasar (Baca Dulu 2 Menit)

Bayangkan otakmu adalah sebuah **kota**. Setiap catatan adalah satu **bangunan**, dan `[[wikilink]]` adalah **jalan** yang menghubungkannya.

| Konsep | Analogi | Contoh |
|--------|---------|--------|
| **Catatan Atomik** | Satu bangunan = satu ide | `[[Nutrisi Hidroponik]]` hanya berisi tentang itu, tidak bercampur dengan irigasi |
| **Wikilink** | Jalan antar bangunan | `[[Nitrogen]]` ditautkan dari catatan `[[Nutrisi Hidroponik]]` |
| **MOC (Map of Content)** | Peta kota | `[[Urban Farming]]` adalah peta besar yang menunjuk ke semua jalan |
| **Backlink** | Siapa yang menunjuk ke sini | Panel kanan Obsidian menunjukkan catatan mana yang merujuk ke halaman ini |
| **Tag** | Label longgar | `#hidroponik` `#nutrisi` — untuk kategorisasi fleksibel |

---

## 📋 Langkah 1: Menangkap Ide ke Inbox

Setiap kali dapat ide, bacaan baru, atau temuan riset — **jangan langsung ke catatan permanen**. Tulis dulu di Inbox.

### Contoh Praktik 👇

1. Buka Obsidian
2. Tekan `Ctrl+N` → ketik judul: **"Nutrisi AB Mix"**
3. Tulis apapun yang kamu tahu sekarang:

```
Nutrisi AB Mix itu pupuk hidroponik yang paling umum, 
terdiri dari larutan A (kalsium nitrat, kalium nitrat, Fe) 
dan larutan B (kalium fosfat, magnesium sulfat, mikronutrien). 
Nanti cari tahu soal ppm ideal untuk selada.
```

4. Simpan — selesai. Catatan ini ada di `0_Inbox/`.
5. **Jangan terlalu dipikirkan.** Tujuannya menangkap, bukan menyempurnakan.

> [!tip] Kapan ke Inbox?
> - Ide tiba-tiba muncul
> - Temuan menarik dari bacaan
> - Pertanyaan yang ingin dijawab nanti
> - Potongan informasi yang belum lengkap

---

## 🔄 Langkah 2: Memproses Inbox → Catatan Permanen

Setiap 2-3 hari, buka Inbox dan proses catatan yang sudah terkumpul. Di sinilah "keajaiban" Zettelkasten terjadi.

### Contoh Praktik 👇

**Catatan Inbox kita:** `Nutrisi AB Mix.md` (mentah)

Sekarang kita proses:

1. Buka `Nutrisi AB Mix.md`
2. Tekan `Ctrl+T` → pilih **tpl-catatan-permanen**
3. Isi metadata dan rapikan:

```markdown
---
judul: "Nutrisi AB Mix"
tanggal: "2026-06-24"
tag:
  - hidroponik
  - nutrisi
status: 🌿
referensi:
  - 
---

# Nutrisi AB Mix

> [!abstract] Ringkasan
> AB Mix adalah pupuk hidroponik dua larutan (A & B) 
> yang mengandung seluruh nutrisi esensial bagi tanaman.

## Isi

### Komposisi Larutan A
- Kalsium nitrat — sumber Ca dan N
- Kalium nitrat — sumber K
- Fe (kelat besi)

### Komposisi Larutan B
- Kalium fosfat — sumber P
- Magnesium sulfat — sumber Mg dan S
- Mikronutrien (Mn, Zn, Cu, B, Mo)

### PPM Ideal
- Selada: 560-840 ppm (fase vegetatif)

## Keterkaitan

- [[Nutrisi Hidroponik]] — konsep lebih luas
- [[Defisiensi Nutrisi]] — jika ppm tidak tepat
- [[Selada]] — tanaman contoh
```

4. **Pindahkan file** ke folder `2_Permanent/`
5. Hapus dari Inbox

> [!important] Aturan Emas
> **Satu catatan = satu konsep.** Kalau ada ide baru muncul saat menulis (misalnya "Defisiensi Kalsium"), buat catatan terpisah — jangan gabung.

---

## 🔗 Langkah 3: Menghubungkan Catatan (Linking)

Inilah inti Zettelkasten. Setiap kali menulis, tanyakan: **"Apa hubungannya dengan catatan lain?"**

### Contoh Praktik 👇

Kamu sudah punya catatan `[[Nutrisi AB Mix]]`. Sekarang buat catatan baru:

1. `Ctrl+N` → **"Defisiensi Kalsium pada Hidroponik"**
2. Gunakan template `tpl-catatan-permanen`
3. Di bagian **Keterkaitan**, tambahkan:

```markdown
## Keterkaitan

- [[Nutrisi AB Mix]] — kalsium berasal dari kalsium nitrat di larutan A
- [[Defisiensi Nutrisi]] — konsep umum defisiensi
- [[pH Larutan Nutrisi]] — pH tinggi menghambat serapan kalsium
```

4. Sekarang buka kembali `[[Nutrisi AB Mix]]` — lihat panel kanan **Backlink**: `Defisiensi Kalsium pada Hidroponik` akan muncul di sana!

> [!tip] Jenis Link di Obsidian
> - `[[Nama Catatan]]` — link ke catatan yang sudah ada
> - `[[Nama Catatan|teks tampilan]]` — link dengan teks berbeda
> - `[[Nama Catatan#subjudul]]` — link ke bagian spesifik
> - `[[Nama Catatan^blok]]` — link ke blok/paragraf spesifik

---

## 🗺️ Langkah 4: Membangun MOC (Map of Content)

Saat sudah punya 5-10 catatan tentang satu topik, saatnya buat MOC sebagai "peta navigasi".

### Contoh Praktik 👇

Kamu sudah punya catatan: `[[Nutrisi AB Mix]]`, `[[Defisiensi Kalsium pada Hidroponik]]`, `[[ppm Ideal Selada]]`, `[[pH Larutan Nutrisi]]`.

Buat MOC untuk menghubungkan semuanya:

1. `Ctrl+N` → **"Nutrisi Hidroponik"**
2. Gunakan template `tpl-moc`
3. Simpan di `1_Atlas/`
4. Isi:

```markdown
---
judul: "Nutrisi Hidroponik"
tanggal: "2026-06-24"
tag:
  - moc
  - hidroponik
  - nutrisi
---

# 🧪 Nutrisi Hidroponik

> [!tldr] Peta Konten
> Segala hal tentang nutrisi dalam sistem hidroponik.

## Subtopik

### Pupuk & Formula
- [[Nutrisi AB Mix]] — pupuk 2 larutan paling umum
- [[Alternatif AB Mix]] — MS media, Grow More

### Masalah Nutrisi
- [[Defisiensi Kalsium pada Hidroponik]]
- [[Defisiensi Nutrisi]]

### Parameter
- [[ppm Ideal Selada]]
- [[pH Larutan Nutrisi]]
- [[EC Meter dan Cara Pakainya]]

### Teori
- [[Makronutrien]]
- [[Mikronutrien]]
```

> [!tip] Kapan buat MOC?
> Saat satu topik sudah punya **5+ catatan anak** dan kamu mulai bingung mengelolanya. MOC adalah "daftar isi" yang hidup — bisa diedit kapan saja.

---

## 📅 Langkah 5: Catatan Harian (Daily Notes)

Gunakan untuk mencatat progres riset harian.

### Contoh Praktik 👇

1. Tekan **"Open Today's Daily Note"** dari ribbon kiri (atau command palette `Ctrl+P` → "daily")
2. Template otomatis terisi:

```markdown
---
tanggal: "2026-06-24"
tag:
  - harian
---

# 2026-06-24

## 📝 Catatan Riset
- Baca 3 jurnal tentang [[Nutrisi AB Mix]] untuk selada
- Mulai eksperimen 4 variasi ppm: 500, 650, 800, 950

## 🔗 Temuan / Ide Baru
- Selada dengan ppm 800 tumbuh lebih cepat 20% dari 500ppm
- Perlu baca lebih dalam tentang [[Rasio N-P-K]]

## 📚 Bacaan Hari Ini
- "Hydroponic Nutrient Solutions" oleh J. Smith (2023)
- Jurnal: "Optimal PPM for Lactuca sativa" → buat [[Catatan Literatur Jurnal PPM Selada]]

## 📅 Rencana Besok
- Ukur EC larutan setelah 24 jam
- Cari sumber [[Kalsium Nitrat]] lokal
```

> [!tip] Kenapa ini penting?
> Daily notes jadi **log riset** yang bisa direferensi nanti. Semua `[[wikilink]]` di daily notes otomatis terhubung ke catatan permanen.

---

## 📊 Langkah 6: Eksplorasi dengan Graph View

1. Buka `[[Urban Farming]]` (MOC utama)
2. Tekan `Ctrl+G` — **Graph View** muncul
3. Kamu akan melihat:
   - **Titik besar** = MOC utama
   - **Titik-titik kecil** = catatan anak
   - **Garis** = hubungan linking
   - **Warna** = semakin terang semakin banyak koneksi

> [!tip] Gunakan Graph View untuk:
> - Menemukan catatan "yatim" (belum terhubung)
> - Melihat kluster topik yang berkembang
> - Menemukan hubungan tak terduga antar topik

---

## 🔁 Siklus Kerja Harian (Rangkuman)

```
📥 TANGKAP          → 0_Inbox/          (setiap ada ide)
🔄 PROSES (2-3 hr)  → 2_Permanent/      (rapikan + link)
🔗 HUBUNGKAN        → tambah [[link]]   (setiap menulis)
🗺️ BANGUN MOC       → 1_Atlas/          (setelah 5+ catatan)
📅 LOG HARIAN       → 4_Daily/          (setiap hari)
📊 EKSPLORASI       → Graph View        (seminggu sekali)
```

---

> [!note] Mulai Praktik
> Sekarang buka **[[Latihan Zettelkasten 1 - Tangkap Ide]]** dan ikuti instruksinya langkah demi langkah. Ada 3 latihan total:
> 1. 📥 **[[Latihan Zettelkasten 1 - Tangkap Ide]]** — Menangkap ide ke Inbox
> 2. 🔄 **[[Latihan Zettelkasten 2 - Proses Inbox ke Permanen]]** — Memproses catatan
> 3. 🔗 **[[Latihan Zettelkasten 3 - Linking & Membangun MOC]]** — Menghubungkan semuanya
