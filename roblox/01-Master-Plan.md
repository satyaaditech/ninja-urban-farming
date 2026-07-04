# 01 — RENCANA INDUK: NINJA URBAN FARMING (ROBLOX)

## Judul Game
**Ninja Urban Farming: Simulator Siklus Tertutup**

## Slogan
*"High Yield, Low Effort — Belajar Bertani Urban Seperti Ninja."*

---

## 1. Visi

Menjadi **simulasi pertanian urban paling akurat dan paling mudah diakses di dunia** yang dibangun di dalam Roblox, berfungsi sebagai sumber belajar utama bagi sekolah, universitas, dan pembelajar mandiri di seluruh dunia. Game ini menerjemahkan buku panduan *Ninja Urban Farming* 16 bab ke dalam simulator ekosistem siklus tertutup ( *closed-loop* ) yang imersif, ketat secara ilmiah, di mana setiap limbah menjadi sumber daya dan setiap keputusan memiliki konsekuensi yang terukur.

---

## 2. Pilar Utama

| Pilar | Deskripsi |
|--------|-------------|
| **Akurasi Ilmiah** | Setiap parameter (pH, amonia, DO, ABW, feeding rate, rasio NPK, aktivitas mikroba) berperilaku sesuai dengan sains agronomi dan akuakultur nyata. |
| **Siklus Tertutup Otentik** | Limbah dari satu subsistem memberi makan subsistem lainnya. Air kotor lele → pupuk tanaman. Sisa dapur → maggot BSF → pakan ayam. Kotoran ayam → kompos → tanah. **100% organik, nol bahan kimia sintetis.** Tanpa konversi "ajaib". |
| **Diagnosis Klinis** | Pemain harus mengamati gejala visual (daun menguning, ikan menggantung vertikal, jamur kapas) dan menerapkan pengobatan organik yang tepat dari panduan SOP — persis seperti petani urban sungguhan. |
| **Skalabilitas Modular** | Mulai dengan 1 galon lele. Kembangkan ke 3 galon + biopond BSF + ayam petelur + raised bed + sistem kompos & Eco-Enzyme. Sistem berkembang bersama pemain. |
| **Utilitas Edukasi** | Modul pembelajaran bawaan, rubrik penilaian, dasbor guru, dan jalur sertifikasi untuk lingkungan pendidikan formal. |
| **Monetisasi Berkelanjutan** | Monetisasi etis melalui kustomisasi kosmetik, paket ekspansi lanjutan, lisensi pengajar/kelas, dan item akselerasi opsional — tidak pernah *pay-to-win* pada mekanik inti. |

---

## 3. Target Audiens

### Primer
- **Pelajar (usia 12–22 tahun)** di program pertanian, biologi, atau ilmu lingkungan
- **Guru & dosen** yang menggunakan game sebagai alat bantu ajar interaktif
- **Penggemar urban farming** yang ingin berlatih sebelum berinvestasi uang sungguhan

### Sekunder
- **Pemain Roblox umum (usia 10+)** yang tertarik genre simulasi/tycoon
- **LSM & program pemerintah** yang mempromosikan edukasi ketahanan pangan
- **Petani hobi** yang memvalidasi setup rumahan mereka

---

## 4. Tujuan Pembelajaran (Penyelarasan Taksonomi Bloom)

Melalui game ini, pembelajar akan mampu:

| Tingkat | Tujuan |
|-------|-----------|
| **Mengingat** | Mengidentifikasi parameter kunci setiap subsistem (rentang pH optimal, % feeding rate, target ABW, gejala penyakit). |
| **Memahami** | Menjelaskan logika siklus tertutup: mengapa biopond BSF mengurangi bau, mengapa fermentasi deep litter bekerja, mengapa rotasi air mencegah lonjakan amonia. |
| **Menerapkan** | Menghitung kebutuhan pakan harian menggunakan rumus ABW × N × FR. Mencampur resep pestisida organik (PesNab). Mendiagnosis kesehatan ikan dari gejala visual. |
| **Menganalisis** | Memecahkan masalah kegagalan sistem: pH rendah → tambah dolomit; lonjakan amonia → kurangi pakan + flushing air; daun menguning → identifikasi defisiensi nitrogen vs. magnesium. |
| **Mengevaluasi** | Membandingkan efektivitas pengobatan (salt bath vs. daun pepaya untuk Saprolegnia). Menilai tradeoff alokasi sumber daya antar subsistem. |
| **Mencipta** | Merancang tata letak zona kustom. Memformulasikan booster organik eksperimental. Mengoptimalkan sistem siklus tertutup lengkap untuk hasil maksimal dengan input minimal. |

---

## 5. Gambaran Sistem Game

```
┌──────────────────────────────────────────────────────────────────┐
│                   NINJA URBAN FARMING GAME                         │
│                                                                   │
│  ┌─────────┐   ┌─────────┐   ┌──────────┐   ┌──────────────┐    │
│  │  LELE   │──▶│ RAISED  │──▶│ DAPUR &  │──▶│   KOMPOSTER  │    │
│  │ BIOFLOK │   │  BEDS   │   │ KONSUMEN │   │   + EE TONG  │    │
│  │(Protein)│   │(Sayuran)│   │          │   │              │    │
│  └────┬────┘   └────┬────┘   └────┬─────┘   └──────┬───────┘    │
│       │             │             │                 │             │
│       │  air buangan│             │ sisa dapur      │ kompos      │
│       └─────────────┘             └─────────────────┘             │
│                                                                   │
│  ┌─────────┐   ┌──────────┐   ┌──────────┐   ┌──────────────┐    │
│  │  AYAM   │◀──│  MAGGOT  │◀──│  PUYUH   │──▶│   KELINCI    │    │
│  │ PETELUR │   │   BSF    │   │ PETELUR  │   │  (POC Urine) │    │
│  │(Telur)  │   │(Protein) │   │(Telur)   │   │              │    │
│  └────┬────┘   └────┬─────┘   └────┬─────┘   └──────┬───────┘    │
│       │             │             │                  │             │
│       │ manure      │ maggot      │ ekskreta         │ urine       │
│       └─────────────┴─────────────┴──────────────────┘             │
│                         ▼                                         │
│                    PUPUK & TANAH                                  │
└──────────────────────────────────────────────────────────────────┘
```

### Ringkasan Subsistem

| # | Subsistem | Mekanik Inti | Parameter Kunci |
|---|-----------|--------------|----------------|
| 1 | Lele Bioflok (3 Galon) | Pertumbuhan ikan, kimia air, manajemen penyakit | pH, DO, NH₃, NO₂⁻, ABW, Feeding Rate, kepadatan |
| 2 | Maggot BSF (Biopond) | Simulasi siklus hidup, auto-harvest | Suhu, kelembapan, C/N substrat, kepadatan larva |
| 3 | Ayam Petelur (Deep Litter) | Produksi telur, auto-composting | Ketebalan litter, C/N ratio, komposisi pakan, kesehatan |
| 4 | Raised Beds (Sayuran) | Pertumbuhan tanaman, manajemen penyakit/hama, rotasi | NPK, pH tanah, kelembapan, sinar matahari, tekanan hama |
| 5 | Komposter & Eco-Enzyme | Dekomposisi, produksi enzim | Suhu, kelembapan, C/N ratio, aktivitas mikroba |
| 6 | Bio-Multiplikasi EM4 | Ekspansi kultur mikroba | pH, konsentrasi gula, waktu fermentasi |
| 7 | Booster Organik (K-Booster, Aminor-Grow, Cal-Phos, Mag-Elixir) | Sistem crafting perangsang tanaman | Rasio resep, waktu fermentasi |
| 8 | Ilmu Tanah (Asam Humat, JMS-IMO, Biochar) | Regenerasi kesehatan tanah | KTK, aktivitas mikroba (indikator relatif), % bahan organik |

---

## 6. Mode Permainan

### 6.1 Mode Cerita / Terbimbing
Narasi terstruktur mengikuti bab-bab buku. Pemain mewarisi halaman belakang 75 m² dan dibimbing langkah demi langkah oleh NPC "Mentor Ninja" untuk membangun setiap subsistem. Setiap bab terbuka setelah menyelesaikan bab sebelumnya. Skenario klinis diperkenalkan pada momen yang ditentukan (misalnya, "Lele Anda menggantung vertikal — diagnosis dan obati sebelum kematian massal dalam 12 jam").

### 6.2 Mode Sandbox / Bebas
Akses tak terbatas ke semua subsistem sejak awal. Tanpa batasan tutorial. Pemain bereksperimen dengan tata letak, menguji parameter ekstrem, dan merancang konfigurasi siklus tertutup mereka sendiri. Ideal untuk pembelajar tingkat lanjut dan optimasi kompetitif.

### 6.3 Mode Kelas / Pengajar
Guru membuat "tugas" dengan tujuan spesifik:
- Atur kondisi awal (misalnya, pH 6.2, ikan menunjukkan stres amonia)
- Tentukan kriteria keberhasilan (pulihkan pH ke 7.5, nol kematian dalam 48 jam)
- Atur batas waktu dan sumber daya yang diizinkan
- Lihat dasbor performa siswa dengan analitik diagnostik

### 6.4 Mode Tantangan / Skenario
Skenario dengan tekanan waktu:
- "Krisis Mati Lampu" — listrik padam, aerator mati 3 jam. Selamatkan lele Anda.
- "Invasi Kutu Kebul" — vektor virus Gemini terdeteksi. Kendalikan dan obati dalam 5 hari game.
- "Minggu Kekeringan" — pasokan air dipotong setengah. Optimalkan distribusi ke seluruh subsistem.
- "Maggot Kabur" — prepupa BSF merayap keluar; panen dan proses sebelum kerugian.

### 6.5 Multiplayer Co-op (Pasca-Peluncuran)
Beberapa pemain mengelola lahan bersebelahan. Perdagangan sumber daya. Satu fokus lele, yang lain fokus tanaman. Produksi EE dan kompos bersama. Papan peringkat kompetitif untuk efisiensi sistem total.

---

## 7. Sistem Waktu

| Parameter | Nilai | Catatan |
|-----------|-------|-------|
| Kecepatan default | 1 hari game = 15 menit waktu nyata | Dapat dikonfigurasi 10–30 menit |
| Kecepatan dipercepat | 1 hari game = 2 menit | Untuk melewati masa tunggu (biaya kredit in-game) |
| Kecepatan krisis | 1 jam game = 30 detik | Skenario darurat membutuhkan keputusan real-time |
| Timer fermentasi | Diskalakan ke sistem waktu | Fermentasi 14 hari nyata = ~3.5 jam pada kecepatan default |
| Siklus pertumbuhan tanaman | Tergantung spesies | Kangkung: 25 hari (~6.25 jam), Tomat: 90 hari (~22.5 jam) |
| Siklus pertumbuhan lele | 2.5–3 bulan | ~18.75–22.5 jam pada kecepatan default |

---

## 8. Strategi Monetisasi

### 8.1 Prinsip Etis
- **Tanpa pay-to-win pada mekanik inti.** Laju pertumbuhan, ketahanan penyakit, dan hasil panen tidak dapat ditingkatkan dengan Robux.
- **Pengetahuan gratis.** Semua panduan klinis SOP dan formula dari buku dapat diakses dalam game tanpa pembelian.
- **Kosmetik dahulu.** Monetisasi primer adalah kustomisasi visual.

### 8.2 Aliran Pendapatan

| Aliran | Deskripsi | Harga |
|--------|-------------|-------------|
| **Skin Kosmetik** | Warna galon, desain kandang, material raised bed (bambu, kayu reclaimed, metal modern), outfit NPC | 50–300 Robux |
| **Preset Tata Letak** | Tata letak zona yang sudah dioptimalkan (kompak, pemula, expert) | 100–250 Robux |
| **Paket Ekspansi** | Buka subsistem lanjutan: Stroberi Vertikultur, Pepaya California tabulampot, Budikdamber, Hidroponik Sederhana. *Catatan: Ini adalah DLC berbayar, berbeda dari pembaruan konten gratis pasca-peluncuran (lihat 06-Roadmap, Fase 7).* | 300–500 Robux per paket |
| **Token Percepat Waktu** | Percepat fermentasi/pertumbuhan (non-kompetitif, kenyamanan saja) | 25 Robux per penggunaan |
| **Lisensi Kelas** | Dasbor guru, manajemen siswa, pembuatan tugas, analitik | 1.000–5.000 Robux/tahun |
| **Ujian Sertifikasi** | Asesmen akhir modul yang menghasilkan "Sertifikat Ninja Urban Farming" virtual | 200 Robux per ujian |
| **Dekorasi Premium** | Item dekoratif: orang-orangan sawah, lonceng angin, lentera, gnome taman, fitur air | 25–150 Robux |
| **Event Pass Musiman** | Tantangan terbatas dengan kosmetik eksklusif dan varietas tanaman langka | 200–400 Robux |

### 8.3 Pengalaman Gratis
Game dasar (Lele 1 Galon + 1 Raised Bed + Komposter + Biopond BSF) sepenuhnya gratis. Pemain dapat menyelesaikan inti pembelajaran, memanen lele dan sayuran, serta memahami konsep siklus tertutup tanpa menghabiskan Robux sepeser pun.

---

## 9. Platform & Basis Teknis

| Item | Spesifikasi |
|------|---------------|
| Engine | Roblox Studio (skrip Luau terbaru) |
| Klien | Windows, macOS, iOS, Android, Xbox |
| Fisika | Fisika bawaan Roblox untuk daya apung air, gravitasi |
| Jaringan | Model klien-server Roblox; server-otoritatif untuk semua logika simulasi |
| Persistensi Data | Roblox DataStoreService untuk progres pemain; MemoryStoreService untuk state multiplayer langsung |
| Rendering | Manfaatkan MaterialService baru Roblox (2023+), SurfaceAppearance, tekstur PBR untuk visual tanah/air/tanaman yang realistis |
| Audio | Ambient berlapis (hujan, burung, dengung aerator), umpan balik UI, sulih suara NPC (opsional) |
| Aksesibilitas | Mode buta warna, text-to-speech untuk deskripsi klinis, toggle UI sederhana |

---

## 10. Metrik Keberhasilan (Pasca-Peluncuran)

| Metrik | Target |
|--------|--------|
| Pengguna Aktif Bulanan (MAU) | 50.000+ |
| Durasi Sesi Rata-rata | 25+ menit |
| Retensi D7 | 35%+ |
| Lisensi Kelas Terjual | 200+ di tahun pertama |
| Sertifikasi Pemain Diselesaikan | 5.000+ di tahun pertama |
| Konten Buatan Pengguna (desain farm dibagikan) | 10.000+ |
| Kemitraan Institusi Pendidikan | 50+ |
| Pemain melaporkan "bertani sungguhan setelah main game" | Pelacakan kualitatif via survei |

---

## 11. Lanskap Kompetitif

| Game | Kekuatan | Diferensiator Kami |
|------|----------|-------------------|
| Farming Simulator (PC) | Pertanian komersial skala besar | Kami fokus pada sistem siklus tertutup urban skala kecil dengan ketelitian ilmiah |
| Stardew Valley | Pixel art menawan, elemen RPG | Kami memprioritaskan akurasi biologis dan transferabilitas dunia nyata |
| Tycoon pertanian Roblox | Mudah dipelajari, kasual | Kami menambahkan diagnosis klinis, SOP pengobatan organik, dan asesmen formal |
| Simulator akuaponik nyata | Sangat akurat | Kami membuatnya mudah diakses, tergamifikasi, dan tersedia di semua platform via Roblox |

---

## 12. Prinsip Pengembangan Inti

1. **Sains Dahulu, Seru Kemudian.** Mekanik dirancang dari formula dan data nyata, lalu dibungkus dalam gameplay yang menarik.
2. **Tunjukkan, Jangan Hanya Beri Tahu.** Setiap parameter memiliki indikator visual (warna ikan, tekstur daun, kekeruhan air, kegelapan tanah).
3. **Gagal untuk Maju.** Pemain belajar lebih banyak dari mendiagnosis masalah daripada dari menjalankan sempurna. Skenario klinis adalah momen pembelajaran.
4. **Akar Indonesia, Jangkauan Global.** Menjunjung asal bahasa Indonesia tetapi menyediakan lokalisasi penuh bahasa Inggris dan multi-bahasa.
5. **Komunitas sebagai Konten.** Memungkinkan pemain membagikan tata letak farm, resep kustom, dan skenario tantangan.

---

*Dokumen Berikutnya: 02-Sistem-Mekanik.md — Mekanik Game Detail untuk Semua Subsistem*
