---
judul: "Latihan Zettelkasten 3 - Linking & Membangun MOC"
tanggal: "2026-06-24"
tag:
  - latihan
---

# 🔗 Latihan 3: Menghubungkan & Membangun MOC

> [!goal] Tujuan
> Kamu akan membuat koneksi antar catatan dan membangun MOC pertamamu.

---

## Bagian A: Membuat Catatan Baru & Menghubungkannya

### Instruksi

Kita akan membuat 2 catatan baru yang terhubung dengan catatan yang sudah kamu buat di Latihan 2.

#### Catatan 1: "Defisiensi Nutrisi pada Tanaman Hidroponik"

1. `Ctrl+N` → judul: **Defisiensi Nutrisi pada Tanaman Hidroponik**
2. Gunakan template `tpl-catatan-permanen`
3. Tulis tentang gejala kekurangan nutrisi yang umum:

```markdown
---
judul: "Defisiensi Nutrisi pada Tanaman Hidroponik"
tanggal: "2026-06-24"
tag:
  - hidroponik
  - nutrisi
  - masalah
status: 🌱
referensi:
  - 
---

# Defisiensi Nutrisi pada Tanaman Hidroponik

> [!abstract] Ringkasan
> Panduan mengenali gejala defisiensi nutrisi pada 
> tanaman hidroponik dan cara penanganannya.

## Isi

### Defisiensi Nitrogen (N)
- **Gejala:** Daun tua menguning, pertumbuhan lambat
- **Penyebab:** ppm terlalu rendah, larutan terlalu encer
- **Solusi:** Tambah larutan A dari [[Nutrisi AB Mix]]

### Defisiensi Kalsium (Ca)
- **Gejala:** Daun baru keriting, tip burn pada selada
- **Penyebab:** pH terlalu tinggi, kalsium mengendap
- **Solusi:** Turunkan pH ke 5.8-6.2

### Defisiensi Besi (Fe)
- **Gejala:** Daun muda pucat/kuning (klorosis interveinal)
- **Penyebab:** pH tinggi, atau larutan B kurang
- **Solusi:** Cek pH, tambah kelat besi

## Keterkaitan

- [[Tanaman yang Cocok untuk Hidroponik Pemula]] — tanaman ini sensitif terhadap defisiensi
- [[Nutrisi AB Mix]] — sumber nutrisi
- [[pH Larutan Nutrisi]] — parameter kunci
```

> [!tip] Perhatikan bagian **Keterkaitan**!
> Di sinilah kamu menghubungkan `[[Tanaman yang Cocok untuk Hidroponik Pemula]]` (dari Latihan 2) dengan catatan baru ini.

4. Simpan di `2_Permanent/`

#### Catatan 2: "pH Larutan Nutrisi"

1. `Ctrl+N` → judul: **pH Larutan Nutrisi**
2. Gunakan template `tpl-catatan-permanen`
3. Isi dengan pengetahuan tentang pH:

```markdown
---
judul: "pH Larutan Nutrisi"
tanggal: "2026-06-24"
tag:
  - hidroponik
  - nutrisi
  - parameter
status: 🌱
referensi:
  - 
---

# pH Larutan Nutrisi

> [!abstract] Ringkasan
> pH adalah parameter kritis dalam hidroponik yang 
> mempengaruhi ketersediaan nutrisi bagi tanaman.

## Isi

### Mengapa pH Penting?
- pH menentukan apakah nutrisi bisa diserap akar
- Setiap nutrisi punya rentang pH optimal untuk penyerapan
- Di luar rentang, nutrisi mengendap dan tidak tersedia

### Rentang Ideal
- **Umum:** 5.5 - 6.5
- **Selada:** 5.8 - 6.2
- **Tomat:** 5.5 - 6.0

### Cara Mengukur
- pH meter digital — paling akurat
- Kertas lakmus — murah tapi kurang presisi
- Tetes indikator — alternatif murah

### Cara Menyesuaikan
- **Turunkan pH:** larutan pH Down (asam fosfat)
- **Naikkan pH:** larutan pH Up (kalium hidroksida)

## Keterkaitan

- [[Nutrisi AB Mix]] — nutrisi yang pH-nya diatur
- [[Defisiensi Nutrisi pada Tanaman Hidroponik]] — pH salah menyebabkan defisiensi
- [[Tanaman yang Cocok untuk Hidroponik Pemula]] — tiap tanaman punya rentang pH berbeda
```

---

## Bagian B: Melihat Hasil Linking

### Verifikasi Backlink

1. Buka `[[Tanaman yang Cocok untuk Hidroponik Pemula]]` (dari Latihan 2)
2. Lihat panel kanan → tab **Backlinks**
3. Kamu akan melihat **2 backlink**: dari `Defisiensi Nutrisi` dan `pH Larutan Nutrisi`

> [!success] Inilah keajaiban Zettelkasten!
> Tanpa kamu sadari, catatanmu sudah saling terhubung. Nanti saat riset makin dalam, cukup buka satu catatan dan kamu bisa lompat ke catatan terkait.

---

## Bagian C: Open Graph View

1. Tekan `Ctrl+G` untuk membuka **Graph View**
2. Klik titik-titik yang muncul — kamu akan melihat 3-4 catatan sudah terhubung
3. Perhatikan:
   - Titik tanpa garis = catatan "yatim" (belum terhubung) → tugas nanti buat dihubungkan

---

## Bagian D: Membangun MOC Mini (Bonus)

Kalau sudah nyaman, coba buat MOC untuk **"Nutrisi & Parameter Hidroponik"**:

1. `Ctrl+N` → **"Nutrisi & Parameter Hidroponik"**
2. Gunakan template `tpl-moc`
3. Simpan di `1_Atlas/`
4. Isi dengan semua catatan nutrisi & parameter yang sudah kamu buat

---

## 🏆 Ceklis Akhir

- [ ] Membuat 2 catatan baru yang saling terhubung
- [ ] Backlink muncul di panel kanan saat buka catatan lama
- [ ] Graph View menampilkan semua titik dan garis koneksi
- [ ] Kamu paham cara `[[linking]]` dan mengapa penting

---

> [!success] Selamat!
> Kamu sudah menyelesaikan 3 latihan Zettelkasten. Sekarang kamu bisa:
> - Menangkap ide ke Inbox
> - Memproses ke catatan permanen  
> - Menghubungkan dengan `[[wikilink]]`
> - Melihat koneksi lewat Backlink dan Graph View
> - Membangun MOC sebagai navigasi
>
> **Lanjutkan eksplorasi sendiri**, atau kembali ke `[[Panduan Zettelkasten untuk Pemula]]` kapan saja.
