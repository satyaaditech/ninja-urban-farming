# LAPORAN REVIEW TEKNIS (A8) — NINJA URBAN FARMING

**Sumber:** `_A7-copy-edited.md` (2927 baris) vs `BluePrint.md`
**Tanggal:** 10 Juni 2026

---

## 1. DOSIS & RASIO — Temuan

### 1.1 Inkonsistensi Waktu Fermentasi Air Cucian Beras
- **Baris 706** (Bab 6): "diamkan 24 jam sampai berbau asam"
- **Baris 1904** (Bab 16): "Diamkan 3-5 hari sampai asam"
- **Status:** Kontradiksi. 24 jam vs 3-5 hari untuk bahan yang sama.
- **Rekomendasi:** Pilih satu durasi standar (3-5 hari untuk fermentasi asam laktat stabil, atau 24 jam untuk penggunaan darurat saja). Sinkronkan kedua baris.

### 1.2 Ambigu: Jumlah Telur Ayam pada Indikator Sehat
- **Baris 581** (Bab 5): "Telur rutin setiap hari — 5-7 butir/minggu pada masa puncak produksi"
- **Konteks:** Bab ini mengasumsikan 5 ekor ayam (baris 536). Indikator tidak menyebutkan apakah 5-7 butir per ekor atau total flock. Jika total flock: terlalu rendah (seharusnya 25-35 butir/minggu).
- **Rekomendasi:** Tegaskan: "5-7 butir/minggu **per ekor**" atau sesuaikan angka untuk total flock.

### 1.3 PesNab Bawang-Cabai: Label "Tanpa Pengenceran" Kurang Jelas
- **Baris 2757** (Cheat Sheet): "Tanpa pengenceran"
- **Baris 956-969** (Bab 9): Resep sudah menghasilkan 1 liter larutan (halus + 1 L air + saring + sabun). "Tanpa pengenceran" berarti larutan 1 liter itu langsung dipakai, bukan konsentrat.
- **Status:** Tidak salah, tapi bisa membingungkan pembaca yang mengira ini undiluted concentrate.
- **Rekomendasi:** Ubah menjadi "Langsung pakai (tidak diencerkan lagi)" di Cheat Sheet.

### 1.4 Rasio Lain: Tidak Ada Masalah
Semua rasio K-Booster (1:100), Aminor-Grow (1:200), Cal-Phos (1:500), Mag-Elixir (1:200), JMS-IMO (1:10), POC Urine Kelinci (1:100), EE foliar (1:1000), garam krosok (1-2 g/L), FR lele (3%-6%) konsisten antara draft dan BluePrint.

---

## 2. KONTRADIKSI ANTAR BAB — Temuan

### 2.1 Maggot BSF untuk Pakan Lele: Disebut di Pengantar, Tidak Ada di Operasional
- **Baris 71** (Bab Pengantar): "Maggot... Kamu berikan... ke lele sebagai pakan tambahan."
- **Baris 101** (Bab Pengantar): "100% untuk lele fase starter" (hanya pelet).
- **Bab 6–7** (Operasional Lele): Tidak satu pun menyebut maggot sebagai pakan lele. Semua bahasan pakan hanya pelet.
- **BluePrint Bab 3:** Menyebut maggot untuk "pakan lele."
- **Status:** Benang merah putus. Filsafat closed-loop menyatakan maggot → lele, tapi SOP pakan lele tidak mengakomodasi.
- **Rekomendasi:** Tambahkan sub-bab singkat di Bab 6 atau Bab 7: "Pakan Maggot untuk Lele — Fase, Takaran, dan Cara Pemberian."

### 2.2 POC Kulit Pisang dari BluePrint Tidak Muncul di Draft
- **BluePrint Bab 16 baris 677:** Menyebut "POC dari kulit pisang yang direndam atau difermentasi."
- **Draft Bab 17** (Nutrisi Generatif): Hanya mereferensi K-Booster (yang pakai batang pisang + sabut kelapa, fermentasi 14 hari).
- **Status:** Opsi sederhana dari BluePrint (POC kulit pisang instan) tidak tersedia di draft. K-Booster jauh lebih kompleks.
- **Rekomendasi:** Tambahkan "Alternatif Sederhana: POC Kulit Pisang (rendam 3-5 hari)" di Bab 17.

### 2.3 Pakan Lele: "100% Pelet Fase Starter" vs Filosofi Closed-Loop
- **Baris 101:** "Pakan pabrikan (pelet) masih digunakan... 100% untuk lele fase starter."
- Ini tidak bertentangan secara internal, tapi bertentangan dengan klaim "100% Organik" di judul buku (baris 2). Pelet komersial mengandung bahan sintetis (premix vitamin/mineral, binder).
- **Rekomendasi:** Tambahkan klarifikasi di Bab Pengantar: "100% Organik" merujuk pada input tanaman (pupuk, pestisida) dan metode budidaya, bukan pada pakan starter lele yang masih bergantung pelet.

---

## 3. KEAMANAN — Temuan

### 3.1 Sabun Cuci Piring sebagai Surfaktan: Tidak Ada Spesifikasi Jenis
- **Muncul di:** PesNab (baris 960, 982), Baking Soda (1348), Belerang (1381), Minyak Mimba (1416), Cuka Dapur (1003), Minyak Jelantah (1008), Cheat Sheet (2761-2762).
- **Masalah:** Tidak disebutkan bahwa harus sabun cuci piring **non-antibakteri**. Sabun antibakteri mengandung triclosan/chloroxylenol yang membunuh mikroba menguntungkan di daun dan tanah.
- **Rekomendasi:** Di Bab 9 (PesNab), tambahkan: "Gunakan sabun cuci piring **bening tanpa antibakteri/pewangi** — sabun antibakteri merusak mikroba baik di permukaan daun."

### 3.2 Air Rendaman Tembakau — Peringatan Kurang Kuat
- **Baris 1421:** "Air rendaman tembakau (⚠️ hentikan 7 hari sebelum panen)"
- **Masalah:** Nikotin adalah neurotoksin. Pengguna perlu tahu bahwa ini adalah opsi paling toksik di antara semua PesNab yang disebutkan. Tidak disebutkan risiko kontak kulit saat menyemprot, atau bahaya residu pada tanaman buah.
- **Rekomendasi:** Perkuat peringatan: "⚠️ **Hanya sebagai opsi terakhir.** Nikotin bersifat toksik. Pakai sarung tangan. JANGAN untuk tanaman yang buahnya sudah mendekati panen meskipun >7 hari."

### 3.3 Belerang/Sulfur — Tidak Ada Peringatan Aplikasi
- **Baris 1381:** "Semprot kabut ke seluruh tanaman, terutama bawah daun, pagi hari."
- **Masalah:** Belerang bersifat fitotoksik pada suhu >30°C (membakar daun). Tidak ada peringatan tentang ini, juga tidak ada peringatan tentang inhalasi debu belerang saat mencampur.
- **Rekomendasi:** Tambahkan: "⚠️ Jangan semprot saat suhu >30°C atau terik matahari penuh. Pakai masker saat mencampur bubuk belerang."

### 3.4 Minyak Jelantah (Minyak Goreng Bekas)
- **Baris 1008:** Digunakan sebagai insektisida (2 sdm + 1 L air + sabun). Ada peringatan hentikan 5 hari sebelum panen (baris 1012).
- **Status:** Cukup aman sebagai insektisida kontak mekanis, tapi tidak disebutkan bahwa minyak jelantah yang sudah tengik/berkali-kali dipakai mengandung senyawa polimer dan radikal bebas. Tidak berbahaya bagi tanaman, tapi bisa mempengaruhi mikroba tanah jika menetes.
- **Rekomendasi:** Tambahkan: "Gunakan minyak jelantah maksimal 2 kali pakai. Minyak yang sudah hitam pekat dan berbau tengik — jangan dipakai."

### 3.5 Sayur Afkir dari Pasar — Tanpa Peringatan Residu Pestisida
- **Baris 596:** "Kunjungi pasar tradisional sore hari, ambil daun sawi/kangkung layu gratis."
- **Masalah:** Sayuran pasar konvensional mengandung residu pestisida. Masuk ke biopond BSF atau kandang ayam → residu masuk ke sistem closed-loop.
- **Rekomendasi:** Tambahkan: "⚠️ Cuci bersih sayur pasar dengan air mengalir sebelum diberikan ke ayam atau biopond. Idealnya hanya gunakan sayur afkir dari kebun sendiri atau yang jelas-jelas organik."

### 3.6 Checklist Keamanan yang Sudah Memadai
- Lindi alkali korosif (baris 1819) — ⚠️ sarung tangan ✓
- Biochar mentah (baris 1695) — ⚠️ wajib charging ✓
- Kubis untuk kelinci fatal (baris 2328) — ⚠️ ✓
- Kulit jeruk d-Limonene (baris 483) — ⚠️ ✓
- Cuka sebagai herbisida non-selektif (baris 999) — ⚠️ peringatan keras ✓
- MSG kontroversial (baris 1996) — baca sampai habis + 5 butir risiko ✓
- Ampas tahu >12 jam basi (baris 693) — ⚠️ ✓
- Aerator mati >3 jam fatal (baris 625) — ⚠️ ✓

---

## 4. KELENGKAPAN — Temuan

### 4.1 SOP Pemberian Maggot BSF ke Lele (Tidak Ada)
- **Rujukan:** Baris 39 (diagram closed-loop), baris 71 (pengantar). Tidak ada di Bab 6 atau Bab 7.
- **Yang hilang:** Takaran maggot per fase lele, frekuensi, cara penyajian (segar vs blansir), fase lele yang boleh diberi maggot, risiko overfeeding maggot (kandungan lemak 30-35%).
- **Rekomendasi:** Tambahkan sub-bab "Pakan Maggot BSF untuk Lele" di Bab 7.

### 4.2 Tidak Ada Panduan Memperoleh Benih Lele dan DOC Ayam
- Draft mengasumsikan pembaca sudah memiliki/paham cara mendapatkan benih lele 7-9 cm dan DOC ayam petelur.
- Tidak ada panduan: ciri benih berkualitas, estimasi harga, tempat membeli, transportasi, atau karantina awal.
- **Rekomendasi:** Tambahkan lampiran atau sub-bab singkat di Bab 6 dan Bab 5.

### 4.3 Tidak Ada SOP Perbanyakan BSF Mandiri Penuh
- Bab 4 membahas siklus hidup dan kelambu, tapi tidak ada instruksi konkret: berapa banyak pupa untuk memulai siklus, berapa rasio jantan-betina ideal, berapa lama kelambu produktif, kapan harus meremajakan stok pupa.
- **Rekomendasi:** Tambahkan sub-bab "Starter Pack BSF: Berapa Banyak Pupa untuk Memulai?" di Bab 4.

### 4.4 Alternatif Daun Mangga Sudah Ada di FAQ, Tapi Tidak di Bab Utama
- FAQ #5 (baris 2489): Alternatif daun jati, bambu, ketapang, sekam, serbuk gergaji, kardus.
- Bab 3, 5, 8, 14, 15 semuanya menyebut "daun mangga kering" sebagai sumber karbon utama tanpa merujuk ke alternatif.
- **Rekomendasi:** Di Bab 3 (Raised Bed) dan Bab 5 (Deep Litter), tambahkan catatan kaki: "lihat FAQ #5 untuk alternatif jika tidak ada daun mangga."

### 4.5 Keamanan Pangan Pasca Panen (Tidak Ada)
- Tidak ada panduan: mencuci sayur, menyimpan telur, membersihkan lele untuk konsumsi, atau masa simpan hasil panen.
- Ini relevan karena sistem closed-loop menggunakan kotoran hewan sebagai pupuk — risiko kontaminasi silang E. coli/Salmonella pada sayuran yang dimakan mentah (selada, kemangi).
- **Rekomendasi:** Tambahkan sub-bab "Keamanan Pangan Pasca Panen" di Bab 22 (Protokol Keamanan): cuci sayur dengan air mengalir + EE 1:1000, jangan pupuk dengan air lele 1 minggu sebelum panen sayur daun yang dimakan mentah.

### 4.6 Struktur Bab vs BluePrint — Semua Tercover
Draft mencakup seluruh 16 bab BluePrint + 10 bab tambahan (Pengantar, Cara Baca, Bab 18-26, Glosarium, Cheat Sheet). Tidak ada bab BluePrint yang hilang.

---

## RINGKASAN TEMUAN

| Area | Jumlah Temuan | Tingkat Kritis |
|------|--------------|----------------|
| Dosis & Rasio | 3 (inkonsistensi, ambigu, label) | Rendah |
| Kontradiksi | 3 (maggot-lele gap, POC pisang hilang, klaim 100% organik) | Sedang |
| Keamanan | 5 (sabun, tembakau, belerang, jelantah, sayur pasar) | Sedang |
| Kelengkapan | 5 (SOP maggot-lele, sumber benih, BSF mandiri, alternatif, keamanan pangan) | Sedang |

**Total: 16 temuan.** Tidak ada temuan yang bersifat fatal (membahayakan jiwa atau merusak sistem secara permanen). Semua dapat dikoreksi dengan tambahan 1-3 paragraf atau klarifikasi singkat.
