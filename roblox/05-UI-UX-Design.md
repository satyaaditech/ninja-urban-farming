# 05 — DESAIN UI/UX: Spesifikasi Antarmuka & Pengalaman Pengguna

> ⚠️ **MOBILE-FIRST MANDATE:** 70%+ pemain Roblox bermain di smartphone. SEMUA desain UI harus dirancang untuk layar sentuh 5–6 inci terlebih dahulu, baru diadaptasi ke desktop. Sistem diagnosis penyakit dan resep booster yang terlalu banyak teks akan membuat layar HP penuh dan membingungkan. Gunakan ikon, radial menu, dan drag-and-drop — bukan daftar teks panjang.

---

## 1. Prinsip Desain

| Prinsip | Deskripsi | Implementasi |
|-----------|-------------|---------------|
| **Mobile-First** | 70%+ pemain di HP — desain untuk ibu jari | Radial menu, drag-and-drop, ikon besar (min 48×48px touch target) |
| **Visibilitas Status Sistem** | Pemain selalu tahu apa yang terjadi | HUD persisten dengan parameter kunci; peringatan berkode warna |
| **Kecocokan Antara Sistem dan Dunia Nyata** | Istilah game cocok dengan terminologi pertanian nyata | Gunakan istilah pertanian Indonesia dengan tooltip bahasa Inggris; ikon realistis |
| **Kontrol dan Kebebasan Pengguna** | Urung mudah, navigasi jelas | "Urung darurat" untuk aksi terakhir; tombol kembali selalu terlihat |
| **Konsistensi dan Standar** | Aksi sama = interaksi sama di mana-mana | Model interaksi terstandarisasi di seluruh 10+ subsistem |
| **Pencegahan Kesalahan** | Cegah kesalahan sebelum terjadi | Konfirmasi aksi destruktif; peringatan sebelum overfeeding; kunci aksi tidak kompatibel |
| **Pengenalan Daripada Mengingat** | Jangan paksa pemain menghafal | Buku resep selalu dapat diakses; referensi SOP klinis selalu satu klik jauhnya |
| **Fleksibilitas dan Efisiensi** | Power user dapat bergerak lebih cepat | Pintasan keyboard; menu radial aksi cepat; operasi batch |
| **Bantuan dan Dokumentasi** | Bantuan saat dibutuhkan | Tombol bantuan "?" peka konteks; petunjuk Mentor Ninja; tertaut ke konten buku |

---

## 2. Arsitektur Informasi

### 2.1 Hierarki Layar

```
[Menu Utama]
├── Main
│   ├── Mode Cerita (Lanjutkan / Game Baru / Pilih Bab)
│   ├── Mode Sandbox (Farm Baru / Muat Farm)
│   ├── Mode Kelas (Gabung Kelas / Tugas)
│   └── Mode Tantangan (Harian / Mingguan / Kustom)
├── Basis Pengetahuan (Referensi buku, panduan SOP, formula, resep)
├── Sertifikasi (Lobi ujian / Hasil / Sertifikat)
├── Pasar (Kosmetik / Ekspansi / Token Waktu)
├── Pengaturan (Audio / Video / Bahasa / Aksesibilitas / Kontrol)
└── Kredit & Tentang

[HUD Dalam Game]  ← Selalu terlihat selama gameplay
├── Bilah Atas: Waktu Game · Hari # · Kredit · Skor Loop Health
├── Baki Peringatan: Peringatan klinis, pengingat tugas, popup achievement
├── Aksi Cepat: Menu radial (atau bilah bawah di mobile)
├── Minimap: Zona 1 / Zona 2 / Teleportasi cepat
└── Status Subsistem: Bilah parameter mini (dapat dikonfigurasi)

[Panel Detail]  ← Terbuka saat pemain klik/berinteraksi dengan subsistem
├── Dasbor Parameter: Pengukur, grafik tren, riwayat
├── Tombol Aksi: Kontekstual (Beri Pakan, Flush, Panen, Obati, dll.)
├── Referensi SOP: Panduan klinis tertanam untuk subsistem ini
└── Tombol tutup (atau klik jauh)

[Modal Layar Penuh]  ← Untuk tugas fokus
├── Diagnosis Kasus Klinis
├── Antarmuka Crafting
├── Ujian Sertifikasi
├── Pasar
├── Pengaturan
└── Editor Tata Letak Farm
```

### 2.2 Aliran Navigasi

```
Menu Utama ──▶ Dunia Game
                  │
                  ├── Jalan ke subsistem ──▶ Muncul ProximityPrompt
                  │                              │
                  │                              ├── Aksi cepat (klik) ──▶ Segera
                  │                              └── Buka panel (tahan/klik ikon) ──▶ Panel Detail
                  │
                  ├── Peringatan muncul ──▶ Klik peringatan ──▶ Panel Detail (subsistem terkait)
                  │
                  ├── Buka Buku Crafting (tombol pintas "C") ──▶ Antarmuka Crafting
                  │
                  ├── Buka Basis Pengetahuan (tombol pintas "K") ──▶ Panel Referensi
                  │
                  ├── Buka Menu Utama (Esc / tombol Menu) ──▶ Overlay jeda
                  │
                  └── Kasus klinis dipicu ──▶ Modal paksa (waktu-kritis)
```

---

## 3. Head-Up Display (HUD)

### 3.1 Tata Letak

```
┌──────────────────────────────────────────────────────────────┐
│ ☰   Hari 47  ☀ Pagi (07:30)    💰 1.250    🔄 Loop: 78%    │  ← Bilah Atas
│                                                               │
│                                                               │
│                                                               │
│                    [TAMPILAN DUNIA GAME]                      │
│                                                               │
│                                                               │
│                                                               │
│                                                               │
│      [Bilah Mini Subsistem]         [⚡ Aksi Cepat]          │  ← Kiri/Kanan Bawah
│      Galon 1: ● pH 7.2            🔧 Buka Keran            │
│      Galon 2: ● pH 6.8 ⚠         🐟 Beri Pakan           │
│      Galon 3: ● pH 7.5            🌱 Siram Tanaman         │
│      Bed 1:   ● N 85%             🥚 Kumpulkan Telur      │
│      Kompos:  ● 67% Matang        📋 Buka Resep           │
└──────────────────────────────────────────────────────────────┘
```

### 3.2 Detail Bilah Atas

| Elemen | Deskripsi | Interaksi |
|---------|-------------|-------------|
| ☰ Menu | Membuka menu utama / jeda | Klik |
| Hari [N] | Hari game saat ini | Hover: hari sejak mulai |
| ☀/🌙 ikon | Fase hari + jam game | Hover: waktu tepat; Klik: kontrol kecepatan waktu |
| 💰 Kredit | Saldo saat ini | Hover: pemasukan/pengeluaran hari ini; Klik: buka panel ekonomi |
| 🔄 Loop % | Skor Loop Health | Hover: rincian; Klik: buka dasbor Loop Health |
| ⚠ Ikon peringatan (jika aktif) | Jumlah peringatan aktif | Klik: lompat ke peringatan paling mendesak |

### 3.3 Bilah Mini Subsistem (Kiri Bawah)

Indikator status minimal yang selalu terlihat untuk setiap subsistem aktif. Diberi kode warna:

| Warna | Arti |
|-------|---------|
| 🟢 Hijau | Rentang optimal |
| 🟡 Kuning | Peringatan — mendekati kritis |
| 🔴 Merah | Kritis — butuh tindakan segera |
| ⬜ Abu-abu | Subsistem tidak aktif / belum dibangun |

Setiap baris dapat diklik → membuka Panel Detail untuk subsistem tersebut.

### 3.4 Aksi Cepat (Kanan Bawah)

Menu radial peka konteks (tahan Q / klik kanan / tekan lama mobile):

```
         [Beri Pakan]
              │
[Panen] ───── ● ───── [Siram]
              │
         [Periksa]
```

Aksi yang ditampilkan bergantung pada apa yang dilihat atau terdekat dengan pemain. Di mobile, ini menjadi bilah tombol horizontal di bagian bawah layar.

---

## 4. Panel Detail (Per Subsistem)

### 4.1 Panel Lele Bioflok

```
┌──────────────────────────────────────────────────┐
│  🐟 LELE BIOFLOK — GALON #1          [✕ Tutup]  │
├──────────────────────────────────────────────────┤
│                                                    │
│  ┌─ Parameter ─────────────────────────────────┐  │
│  │ pH:     [████████░░] 7.2  🟢               │  │
│  │ Amonia: [██░░░░░░░░] 0.1  🟢               │  │
│  │ DO:     [████████░░] 4.8  🟢               │  │
│  │ Nitrit: [█░░░░░░░░░] 0.2  🟢               │  │
│  │ Suhu:   28°C  🟢                           │  │
│  │ Flok:   82% matang                          │  │
│  └──────────────────────────────────────────────┘  │
│                                                    │
│  ┌─ Populasi ───────────────────────────────────┐  │
│  │ 18 ekor · Fase: Grower (Hari 35)             │  │
│  │ ABW: 18.4 g · Target panen: 100 g           │  │
│  │ Kesehatan rata-rata: ████████░░ 85%          │  │
│  │ Sampling terakhir: 5 hari lalu               │  │
│  └──────────────────────────────────────────────┘  │
│                                                    │
│  ┌─ Pakan Hari Ini ────────────────────────────┐  │
│  │ Kebutuhan: 18 × 18.4 × 0.05 = 16.6 g/hari   │  │
│  │ Pagi (40%): 6.6 g   [✓ Diberi]               │  │
│  │ Sore (60%): 10.0 g  [  Belum  ]              │  │
│  │ Status Bibis: ✓ Terfermentasi 2 jam           │  │
│  └──────────────────────────────────────────────┘  │
│                                                    │
│  [🔧 Flush 50%] [🐟 Sampling] [💊 Obati]         │
│  [📋 Lihat SOP Klinis]                            │
│                                                    │
└──────────────────────────────────────────────────┘
```

### 4.2 Panel Raised Bed

```
┌──────────────────────────────────────────────────┐
│  🌱 RAISED BED #2                    [✕ Tutup]   │
├──────────────────────────────────────────────────┤
│                                                    │
│  ┌─ Parameter Tanah ───────────────────────────┐  │
│  │ pH:      [████████░░] 6.8  🟢               │  │
│  │ Nitrogen:[████████░░] 82%  🟢               │  │
│  │ Fosfor:  [██████░░░░] 65%  🟡              │  │
│  │ Kalium:  [████████░░] 78%  🟢               │  │
│  │ Kalsium: [████░░░░░░] 45%  🔴              │  │
│  │ KTK:     18.5 meq/100g                       │  │
│  │ Mikroba: 8.2 × 10⁷ CFU/g  🟢                 │  │
│  └──────────────────────────────────────────────┘  │
│                                                    │
│  ┌─ Tanaman ────────────────────────────────────┐  │
│  │ Spesies:  Cabai (Capsicum annuum)            │  │
│  │ Fase:     Pembungaan (Hari 45/80)            │  │
│  │ Kesehatan:████████░░ 88%                     │  │
│  │ Hama:    Kutu Kebul ⚠ (ringan)               │  │
│  │ Penyakit:Tidak ada                           │  │
│  └──────────────────────────────────────────────┘  │
│                                                    │
│  ┌─ Rekomendasi ───────────────────────────────┐  │
│  │ ⚠ Kalsium rendah — risiko busuk ujung buah   │  │
│  │ → Aplikasikan Cal-Phos Liquid (2 ml/L)       │  │
│  │ ⚠ Kutu Kebul terdeteksi                      │  │
│  │ → Semprot Minyak Mimba atau pasang Yellow Trap│  │
│  └──────────────────────────────────────────────┘  │
│                                                    │
│  [💧 Siram] [🌿 Semprot] [🔬 Diagnosis]         │
│  [📋 Lihat SOP Klinis Tanaman]                    │
│                                                    │
└──────────────────────────────────────────────────┘
```

### 4.3 Dasbor Loop Health

```
┌──────────────────────────────────────────────────┐
│  🔄 DASBOR LOOP HEALTH              [✕ Tutup]    │
├──────────────────────────────────────────────────┤
│                                                    │
│  Skor Keseluruhan: 78%  🟡                       │
│                                                    │
│  ┌─ Daur Ulang Air ──────── 82% ████████░░ ────┐ │
│  │ Lele → Raised Bed: 14.2 L/hari              │  │
│  │ Air segar masuk:   3.8 L/hari                │  │
│  └──────────────────────────────────────────────┘  │
│                                                    │
│  ┌─ Pemulihan Nutrisi ───── 71% ███████░░░ ────┐ │
│  │ Kompos → Tanah:   2.1 kg/hari                │  │
│  │ Limbah terbuang:  0.8 kg/hari ⚠             │  │
│  └──────────────────────────────────────────────┘  │
│                                                    │
│  ┌─ Alih Fungsi Limbah ──── 88% █████████░ ────┐ │
│  │ Dapur → BSF:       1.5 kg/hari               │  │
│  │ Dapur → Kompos:    2.3 kg/hari               │  │
│  │ Terbuang ke luar:  0.5 kg/hari               │  │
│  └──────────────────────────────────────────────┘  │
│                                                    │
│  ┌─ Kemandirian ─────────── 65% ██████░░░░ ────┐ │
│  │ Input diproduksi:    65%                      │  │
│  │ Input dibeli:        35% (pakan, EM4, garam) │  │
│  └──────────────────────────────────────────────┘  │
│                                                    │
│  ┌─ Zero Waste ──────────── 92% █████████░ ────┐ │
│  │ Semua aliran termanfaatkan dengan baik!       │  │
│  └──────────────────────────────────────────────┘  │
│                                                    │
│  📈 Tren 7 Hari Terakhir: [grafik garis kecil ↗]  │
│                                                    │
└──────────────────────────────────────────────────┘
```

---

## 5. Aliran Interaksi Kunci

### 5.1 Aliran Diagnosis Klinis

```
Pemicu: Ambang parameter terlampaui ATAU kejadian terjadwal
    │
    ▼
┌─────────────────────────────────────────┐
│ ⚠ PERINGATAN KLINIS!                   │
│                                         │
│ Gejala Terdeteksi di Galon #2:          │
│ • Ikan menggantung vertikal            │
│ • Kumis tampak keriting                 │
│ • Air sedikit keruh kekuningan          │
│                                         │
│ [🔍 Inspeksi Langsung] [📊 Lihat Data] │
│ [📋 Buka SOP Klinis]    [⏰ Nanti]      │
└─────────────────────────────────────────┘
    │
    ▼ (Pemain klik "Inspeksi" atau "Lihat Data")
    │
┌─────────────────────────────────────────┐
│ DIAGNOSIS — GALON #2                    │
│                                         │
│ Parameter:                              │
│ pH: 6.4 🔴   Amonia: 0.8 🔴           │
│ DO: 2.1 🔴   Nitrit: 0.6 🟡           │
│                                         │
│ Pilih Diagnosis Anda:                   │
│ ○ A: Stres Amonia                     │
│ ○ B: Jamur Saprolegnia                 │
│ ○ C: Infeksi Aeromonas                 │
│ ○ D: Kembung Pakan                     │
│ ○ Saya perlu info lebih lanjut         │
│                                         │
│ [Konfirmasi Diagnosis]                  │
└─────────────────────────────────────────┘
    │
    ▼ (Pemain memilih, mengkonfirmasi)
    │
┌─────────────────────────────────────────┐
│ PENANGANAN — STRES AMONIA              │
│                                         │
│ Tindakan yang direkomendasikan:         │
│ ☐ Puasakan ikan (24–48 jam)           │
│ ☐ Flush air 50%                       │
│ ☐ Tingkatkan aerasi                    │
│ ☐ Tambahkan Garam Krosok 1g/L         │
│                                         │
│ [Terapkan Semua] [Pilih Manual]        │
└─────────────────────────────────────────┘
    │
    ▼
[Bilah progres: pengobatan sedang diterapkan...]
    │
    ▼
┌─────────────────────────────────────────┐
│ HASIL PENANGANAN                       │
│                                         │
│ Diagnosis: Stres Amonia ✅ Benar       │
│ Penanganan: ✓ Puasakan ✓ Flush         │
│             ✓ Aerasi   ✓ Garam         │
│ Waktu respons: 4 jam (dari 12 jam)     │
│ Mortalitas: 0 ekor 🎉                  │
│                                         │
│ Skor: ⭐⭐⭐ (Sempurna!)               │
│                                         │
│ [Lihat Analisis Detail] [Tutup]        │
└─────────────────────────────────────────┘
```

### 5.2 Aliran Crafting (Booster Organik)

```
Pemain membuka Buku Crafting (tombol pintas "C")
    │
    ▼
┌──────────────────────────────────────────────────┐
│  📖 BUKU RESEP — RAMUAN ORGANIK                  │
├──────────────────────────────────────────────────┤
│  [Booster] [Pestisida] [POC] [Tanah] [EM4]      │  ← Tab
│                                                   │
│  ┌─ K-BOOSTER NINJA ──────────────────────────┐  │
│  │ Target: Pembuahan & Pemanis Buah           │  │
│  │ Bahan:                                     │  │
│  │   ✓ Gedebog Pisang: 2 kg  (tersedia)      │  │
│  │   ✓ Sabut Kelapa:  1 kg  (tersedia)       │  │
│  │   ✓ Molase:        250ml (tersedia)        │  │
│  │   ✓ Air Leri:      5 L   (tersedia)        │  │
│  │   ✓ Eco-Enzyme:    50ml  (usia 1+ thn)     │  │
│  │                                             │  │
│  │ Fermentasi: 14 hari  │ [Mulai Membuat →]   │  │
│  └─────────────────────────────────────────────┘  │
│                                                   │
│  ┌─ AMINOR-GROW ──────────────────────────────┐  │
│  │ Target: Pertumbuhan Daun Super Cepat       │  │
│  │ Bahan:                                     │  │
│  │   ✓ Kepala Lele:   1 kg   (3 tersedia)     │  │
│  │   ✓ Air Kelapa:    500ml  (tersedia)       │  │
│  │   ✓ Molase:        150ml  (tersedia)       │  │
│  │   ✗ Eco-Enzyme:    100ml  (HABIS!)        │  │
│  │   ✓ Air Bersih:    3 L    (tersedia)       │  │
│  │                                             │  │
│  │ Fermentasi: 21 hari  │ [Beli EE →]         │  │
│  └─────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────┘
    │
    ▼ (Klik "Mulai Membuat")
    │
┌──────────────────────────────────────────────────┐
│  MEMBUAT: K-BOOSTER NINJA                         │
│                                                    │
│  Langkah 1: Cacah gedebog pisang + sabut kelapa  │
│  [Gunakan Mesin Pencacah →]                       │
│                                                    │
│  ... (proses terpandu langkah demi langkah) ...    │
│                                                    │
│  Campuran siap! Masukkan ke tong fermentasi.       │
│  ⏳ Estimasi selesai: 14 hari game (3.5 jam)      │
│  [Gunakan Token Percepat? 25 Robux]              │
│  [Biarkan Fermentasi]                             │
└──────────────────────────────────────────────────┘
```

---

## 6. Adaptasi Spesifik Mobile

| Desktop | Ekuivalen Mobile |
|---------|------------------|
| Hover mouse untuk tooltip | Tekan lama untuk tooltip |
| Menu konteks klik kanan | Menu radial tekan lama |
| Tombol pintas keyboard (C, K, Esc) | Tombol di layar |
| Zoom scroll wheel | Cubit untuk zoom |
| Pergerakan WASD | Joystick virtual (kiri) |
| Pandangan mouse | Seret sentuh (sisi kanan) |
| Panel detail (samping) | Overlay panel layar penuh |
| Bilah aksi cepat | Bilah aksi bawah (dapat dijangkau ibu jari) |

---

## 7. Panduan Gaya Visual

### 7.1 Palet Warna

| Peran | Warna | Hex |
|------|-------|-----|
| Primer (Farm/Merek) | Hijau Tanah | `#4A7C3F` |
| Sekunder (Air) | Biru Aqua | `#3B9AE1` |
| Aksen (Peringatan) | Kuning Peringatan | `#F5A623` |
| Bahaya | Merah Peringatan | `#E74C3C` |
| Sukses | Hijau Segar | `#2ECC71` |
| Latar Gelap | Cokelat Tanah | `#3E2723` |
| Latar Terang | Perkamen | `#F5F0E1` |
| Teks Primer | Arang | `#2C2C2C` |
| Teks Sekunder | Abu-abu Hangat | `#6B5E53` |
| Latar Panel UI | Gelap Semi-transparan | `rgba(30, 25, 20, 0.92)` |

### 7.2 Tipografi

| Penggunaan | Font | Ukuran | Ketebalan |
|-------|------|------|--------|
| Judul | Gotham / Fredoka One (cadangan) | 24–32px | Tebal |
| Teks isi | Source Sans Pro / Arial (cadangan) | 14–16px | Reguler |
| Nilai parameter | Roboto Mono / monospace | 16–18px | Sedang |
| Label tombol | Gotham (sama dengan judul) | 14–18px | SemiTebal |
| Teks peringatan | Source Sans Pro | 16px | Tebal |

### 7.3 Ikonografi

- Gunakan ikon sederhana bergaya siluet (lebar goresan konsisten, ujung bulat)
- Tema pertanian: daun, tetes air, ikan, telur, tanah, matahari
- Parameter menggunakan simbol yang dikenal universal: `pH`, `°C`, `mg/L`, `%`
- Ikon subsistem: 🐟 Lele, 🪰 BSF, 🐔 Ayam, 🌱 Tanaman, ♻ Kompos, 🧪 EE

---

## 8. Onboarding & Pengalaman Pengguna Pertama Kali (FTUE)

### 8.1 Peluncuran Pertama

1. Layar selamat datang → pilihan bahasa (ID / EN)
2. Sinematik singkat: drone terbang melintasi urban farm yang subur → zoom ke halaman belakang terbengkalai
3. NPC Mentor Ninja memperkenalkan diri: "Selamat datang, calon Ninja Urban Farmer!"
4. Pemain memilih mode: Terbimbing (disarankan) atau Sandbox
5. Preferensi aksesibilitas: mode buta warna, toggle TTS, mode sederhana

### 8.2 Bab Pertama: Bangun Galon Pertama Anda

1. NPC membawa pemain ke Zona 1
2. Garis hantu galon + dudukan muncul → "Tempatkan galon di sini"
3. Pemain menyeret model galon ke posisi
4. Sambungkan pipa manifold (posisi snap-to)
5. Colokkan aerator → gelembung muncul → "Bagus! Sekarang isi air."
6. Pemain mengisi dengan air (selang interaktif)
7. Tambah EM4 + molase (NPC menyediakan jumlah awal)
8. "Sekarang kita tunggu 3–5 hari agar bakteri bioflok tumbuh."
9. Opsi lompat waktu: "Lompat ke Hari 5?" dengan penjelasan mekanik waktu
10. Siap menebar ikan → aklimatisasi ikan terpandu (apungkan kantong 15 menit)

### 8.3 Pengungkapan Fitur Progresif

Fitur terbuka secara bertahap untuk menghindari pemain baru kewalahan:

| Hari Game | Buka |
|----------|--------|
| Hari 1 | Galon Lele #1, HUD dasar |
| Hari 3 | Pemantauan parameter air |
| Hari 5 | Penebaran ikan, sistem pakan |
| Hari 15 | Raised Bed #1 (sederhana: kangkung) |
| Hari 20 | Komposter |
| Hari 25 | Biopond BSF |
| Hari 35 | Galon Lele #2 + #3 |
| Hari 40 | Ayam Petelur + Deep Litter |
| Hari 50 | Crafting Booster Organik |
| Hari 60 | Alat Ilmu Tanah |
| Hari 75 | Sistem Ilmu Tanah Lanjutan (Humo-Ninja, JMS-IMO) |

---

## 9. Umpan Balik & Interaksi Mikro

| Interaksi | Umpan Balik |
|-------------|----------|
| Hover tombol | Skala naik halus (105%) + warna cerah |
| Klik tombol | Skala turun (95%) + suara "pop" singkat |
| Aksi berhasil | Kilatan hijau pada objek + suara "ding" memuaskan |
| Aksi gagal | Kilatan merah + animasi goyang "error" + teks penjelasan |
| Sumber daya ditambah | Partikel dari tangan pemain → kontainer target |
| Perubahan parameter | Pengisian/pengurasan pengukur teranimasi selama 0.5 detik |
| Peringatan klinis | Denyut merah tepi layar + bip meningkat |
| Achievement terbuka | Banner tengah layar dengan ledakan partikel konfeti |
| Transisi hari | Pudar-ke-hitam singkat (0.3 detik) + teks "Hari [N]" |
| Waktu malam | Pergeseran pencahayaan ambient bertahap selama 15 detik nyata |
| Hujan mulai | Build-up 3 detik: langit menggelap → tetes pertama → hujan penuh |

---

*Dokumen Berikutnya: 06-Roadmap-Development.md — Fase Pengembangan & Peta Jalan*
