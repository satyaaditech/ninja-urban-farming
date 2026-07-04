# 10 — AUDIT SENIOR DEVELOPER: NINJA URBAN FARMING (ROBLOX)

*Evaluasi arsitektur, gameplay, dan strategi pengembangan oleh Senior Roblox Developer.*

---

## 1. Kesimpulan Eksekutif

**Status Evaluasi:** GREENLIGHT (Sangat Layak Dilanjutkan)

Ini adalah salah satu dokumen desain game (GDD) Roblox paling rapi, komprehensif, dan matang. Proyek ini sangat memahami tidak hanya sains di balik *urban farming*, tetapi juga cara kerja engine Roblox dan praktik terbaik pengembangannya. Transisi dari buku fisik ke *immersive closed-loop simulator* dilakukan dengan cemerlang. Jika ketelitian sains dapat diseimbangkan dengan *instant gratification* yang dibutuhkan audiens muda, game ini berpotensi besar mendominasi *niche* EdTech dan Simulator di Roblox.

---

## 2. Kekuatan Utama (Apa yang Sudah Sangat Tepat)

### 2.1 Arsitektur Server-Authoritative yang Solid
Pendekatan pada Spesifikasi Teknis (03) sangat tepat. Menggunakan `ModuleScript` terpusat, memisahkan logika simulasi di Server (menggunakan *Server Tick* kustom setiap 30 detik untuk menghemat performa), dan hanya mengirim `StateDelta` ke Klien via `RemoteEvent` adalah standar industri (AAA) di Roblox. Ini akan mencegah eksploitasi dan *lag* yang parah.

### 2.2 "Ninja Vision" & Indikator Visual
Dalam Roblox, aturan utamanya adalah *Show, Don't Tell*. Ide untuk mengubah warna air, tekstur daun layu, dan partikel stres pada ikan jauh lebih baik daripada sekadar menampilkan angka di UI. Fitur "Ninja Vision" akan sangat membantu pemain visual.

### 2.3 Anggaran Performa (Performance Budget)
Membatasi poligon (Galon 300 tris, Biopond 400 tris) dan menggunakan `MaterialService` PBR yang baru adalah langkah jenius. Anda mendapatkan visual realistis tanpa mengorbankan memori klien, memastikan game ini lancar di HP (*mobile*).

---

## 3. Risiko & Titik Kritis (Tantangan Khas Pemain Roblox)

Meskipun secara teknis sempurna, audiens Roblox memiliki karakteristik unik (terutama demografi usia 10-16 tahun) yang bisa menjadi tantangan bagi visi game ini:

### 3.1 Risiko Churn Rate di 5 Menit Pertama (Attention Span)
- **Masalah:** Pemain Roblox sangat tidak sabar. Jika hari 1-5 di game (sekitar 1 jam bermain nyata) hanya berisi menunggu flok air lele terbentuk atau menyemai bibit tanpa hasil instan, 80% pemain akan *quit* sebelum merasakan momen *Aha!*.
- **Solusi:** Di fase tutorial (Tahap 1), berikan **Time-Skip gratis** yang dikendalikan oleh NPC Mentor Ninja. Biarkan pemain mengalami 1 siklus panen kecil yang dipercepat (misalnya, membesarkan bibit kangkung dalam 3 menit pertama) agar mereka merasakan kepuasan sistem *closed-loop*, sebelum mereka dilepas ke skala waktu normal.

### 3.2 Offline Progression (Pertumbuhan Saat Offline)
- **Masalah:** 15 menit nyata = 1 hari in-game. Lele butuh 75 hari game (sekitar 18 jam bermain aktif). Sangat sedikit pemain Roblox yang bermain non-stop selama itu.
- **Solusi:** Pertimbangkan simulasi *offline*. Saat pemain *logout*, hitung waktu yang berlalu dan terapkan saat mereka *login* kembali (menggunakan `os.time()` di `DataStore`). **Catatan Kritis:** Batasi simulasi offline pada "batas aman" agar tidak terjadi krisis saat pemain tidur (misal: jika pakan habis saat offline, sistem masuk mode *stasis/pause* otomatis, bukan ikan mati massal).

### 3.3 Optimalisasi UI untuk Mobile
- **Masalah:** Lebih dari 70% pemain Roblox bermain menggunakan *smartphone*. Sistem diagnosis penyakit dan resep *booster* yang terlalu banyak teks akan membuat layar HP penuh dan membingungkan.
- **Solusi:** Pastikan desain `ScreenGui` Anda berpusat pada ikon. Gunakan sistem *Drag-and-Drop* yang besar atau roda menu (*Radial Menu*) daripada daftar list yang panjang.

---

## 4. Saran Fitur Tambahan (Untuk Meningkatkan Monetisasi & Retensi)

Strategi monetisasi sudah sangat etis (*non-pay-to-win*). Untuk memaksimalkan pendapatan tanpa merusak integritas *gameplay*, pertimbangkan ini:

- **Sistem Peliharaan (Pets) Fungsional Ringan:** Pemain Roblox tergila-gila dengan *pets*. Anda bisa menambahkan Kucing Pertanian (Farm Cat) atau Anjing Penjaga yang bisa dibeli dengan Robux. Secara gameplay mereka organik: Kucing otomatis menangkap hama tikus, Anjing mencegah burung pemakan ikan.
- **Elemen Sosial Sejak Day-1:** Meskipun Multiplayer Co-op ada di tahap pasca-peluncuran, buat agar pemain bisa saling mengunjungi lahan pemain lain di satu server sejak awal rilis (seperti game *Islands* atau *My Restaurant*). Pemain bisa jalan-jalan, memberi jempol (*likes*), dan mungkin membantu menyiram tanaman. Ini memicu efek FOMO dan pamer progres.
- **Sound Design yang Memuaskan (ASMR Farming):** Game farming yang sukses memiliki efek suara yang sangat memuaskan saat panen (*pop, kaching, swoosh*). Karena interaksi di game ini lambat dan penuh pertimbangan, pastikan umpan balik audionya sangat *juicy*.
