# 06 — PETA JALAN PENGEMBANGAN: Fase, Milestone & Prioritas

---

## 1. Filosofi Pengembangan

**"Vertical Slice Dahulu, Perluas Kemudian."**

Daripada membangun 10+ subsistem secara paralel dan tidak ada yang bisa dimainkan selama berbulan-bulan, setiap fase menghasilkan **irisan vertikal yang lengkap, dapat dimainkan, dan dapat diajarkan**. Fase 1 saja sudah menjadi simulator budidaya lele fungsional yang dapat digunakan di ruang kelas. Setiap fase berikutnya menambah kedalaman dan keluasan.

---

## 2. Struktur Tim (Direkomendasikan)

| Peran | Jumlah | Tanggung Jawab |
|-------|------|----------------|
| **Desainer Game / Produser** | 1 | Desain fitur, balancing, manajemen peta jalan |
| **Programmer Luau Senior** | 1 | Engine simulasi server, persistensi data, arsitektur |
| **Programmer Luau (UI)** | 1 | UI klien, HUD, panel, modal |
| **Artis Lingkungan 3D** | 1 | Lingkungan farm, bangunan, properti, pencahayaan |
| **Artis Karakter/Prop 3D** | 1 | NPC, ikan, ayam, BSF, tanaman, alat |
| **Artis Teknis** | 0.5 | Shader, partikel, indikator parameter visual |
| **Desainer Audio** | 0.5 | Ambient, SFX, suara UI |
| **Koordinator QA / Playtest** | 1 | Rencana pengujian, pelacakan bug, umpan balik edukator |
| **Manajer Komunitas** | 0.5 | Discord, media sosial, penjangkauan guru |
| **Ahli Materi (Urban Farming)** | Konsultan | Validasi akurasi simulasi |

**Total: ~7–8 setara penuh waktu. Estimasi timeline: 12–18 bulan ke peluncuran penuh.**

---

## 3. Rincian Fase

---

### FASE 0: Fondasi (Bulan 1–2)

**Tujuan:** Semua infrastruktur siap. Belum ada yang menghadap pemain, tetapi semua sistem inti kokoh secara arsitektur.

| Tugas | Perk. Hari | Prioritas |
|------|-----------|----------|
| Setup proyek Roblox Studio, struktur folder, hierarki ModuleScript | 3 | P0 |
| Definisi tipe Luau (Types.lua) | 2 | P0 |
| Basis data konstanta & parameter tuning (Constants.lua) | 3 | P0 |
| TimeManager — jam game, siklus siang/malam, skala waktu | 5 | P0 |
| Integrasi DataStoreService — simpan/muat data pemain | 5 | P0 |
| Tata letak zona dasar (terrain Zona 1 & Zona 2) | 5 | P0 |
| Kontroler kamera (orbit, zoom, fokus) | 4 | P0 |
| Manajer input (keyboard, mouse, sentuh, gamepad) | 4 | P0 |
| Sistem interaksi (kerangka ProximityPrompt) | 4 | P0 |
| Bus event (kerangka RemoteEvent/RemoteFunction) | 3 | P0 |
| Kerangka UI dasar (ScreenGui, navigasi panel) | 5 | P0 |
| Manajer audio (sistem ambient, sistem SFX) | 4 | P0 |
| Kerangka lokalisasi (tabel string ID + EN) | 3 | P0 |
| Toggle aksesibilitas (buta warna, stub TTS) | 3 | P1 |
| Setup pipeline CI/CD (Rojo, GitHub Actions untuk Roblox) | 3 | P1 |
| **Sistem Simulasi Offline** (catch-up calculation + no-crisis mode) | 5 | P0 |
| **Sistem Kunjungan Sosial Dasar** (read-only: pemain bisa lihat farm pemain lain dalam 1 server) | 5 | P1 |

**Milestone: P0 — "Farm Kosong"**
- Pemain dapat bergabung, berjalan, membuka/menutup panel UI
- Siklus siang/malam berfungsi
- Data tersimpan dan termuat dengan benar
- Semua modul arsitektur terinstansiasi (belum ada logika simulasi)

---

### FASE 1: Lele Bioflok MVP (Bulan 3–4)

**Tujuan:** Simulasi budidaya lele yang lengkap dan akurat secara ilmiah dalam 3 galon. Ini adalah **irisan vertikal inti** yang membuktikan konsep.

| Tugas | Perk. Hari | Prioritas |
|------|-----------|----------|
| **Engine Kimia Air** (pH, NH₃, NO₂⁻, DO, suhu, alkalinitas) | 10 | P0 |
| Model 3D Galon (tembus pandang, potongan atas, katup, pipa) | 5 | P0 |
| Interaksi setup galon (tempatkan, sambung pipa, colok aerator) | 5 | P0 |
| Sistem aerasi (gelembung partikel, mekanik katup bleeding) | 3 | P0 |
| Mekanik flushing (interaksi katup, kalkulasi ulang parameter air) | 4 | P0 |
| **Model Pertumbuhan Ikan** (ABW, fase, formula pertumbuhan) | 8 | P0 |
| Model 3D ikan + animasi berenang | 5 | P0 |
| **Sistem Pemberian Pakan** (kalkulator ABW × N × FR, takar → bibis → beri) | 8 | P0 |
| Mekanik fermentasi (bibis) (campur EM4 + molase + pelet → inkubasi) | 4 | P0 |
| UI timbangan digital (menimbang ikan, mengukur pakan) | 3 | P0 |
| Mekanik Ninja Sampling (tangkap 5 ikan, timbang, perbarui ABW) | 5 | P0 |
| **Sistem Penyakit Klinis A** (Stres Amonia — pemicu lengkap, visual, pengobatan, hasil) | 8 | P0 |
| Sistem Penyakit Klinis B (Saprolegniasis) | 5 | P1 |
| Sistem Penyakit Klinis D (Kembung Pakan) | 5 | P1 |
| Sistem Penyakit Klinis E (Anoksia/Mati Lampu) | 5 | P1 |
| **UI Panel Detail Lele** (parameter, populasi, pakan, aksi) | 8 | P0 |
| UI Diagnosis Klinis (penampil gejala, pemilihan diagnosis, aplikasi pengobatan) | 8 | P0 |
| Laporan Kasus Klinis (umpan balik pasca-resolusi) | 4 | P0 |
| Sistem peringatan (peringatan pergeseran parameter, popup pemicu klinis) | 4 | P0 |
| Bilah mini HUD untuk galon lele | 2 | P0 |
| Mekanik panen (serok, timbang, grading) | 3 | P1 |
| Mekanik sortir (pemisahan kanibal pada hari 45) | 3 | P1 |
| Ekonomi dasar (Kredit diperoleh dari panen, dibelanjakan untuk pakan/benih) | 5 | P1 |
| Audio spesifik lele (dengung aerator, percikan air, ikan memercik) | 3 | P1 |
| Pengujian bug & tuning kimia air | 10 | P0 |

**Milestone: P1 — "Simulator Lele"**
- Pemain dapat menjalankan siklus budidaya ikan lengkap: setup → tebar → beri pakan → kelola kimia → diagnosis 2+ penyakit → panen
- Sepenuhnya dapat dimainkan sebagai alat edukasi mandiri untuk akuakultur
- **Pengujian edukator pertama** dapat dimulai di sini

---

### FASE 2: Tanaman MVP (Bulan 5–6)

**Tujuan:** Tambah raised bed dengan kimia tanah dan pertumbuhan tanaman. Lengkapi siklus nutrisi air-ke-tanaman.

| Tugas | Perk. Hari | Prioritas |
|------|-----------|----------|
| **Engine Kimia Tanah** (NPK, pH, kelembapan, bahan organik, KTK) | 10 | P0 |
| Model 3D Raised Bed (papan kayu, lapisan plastik, mulsa atas) | 3 | P0 |
| Mekanik konstruksi bedengan (craft papan, paku, staples lapisan) | 5 | P0 |
| **Model Pertumbuhan Tanaman** (kurva spesifik spesies, tahap tumbuh) | 8 | P0 |
| Model 3D tanaman — kangkung (semai → matang) | 5 | P0 |
| Model 3D tanaman — sawi, caisim, pakcoy | 4 | P0 |
| Model 3D tanaman — tomat, cabai (semai → buah) | 6 | P0 |
| Mekanik pemupukan air lele → tanaman (flush → siram raised bed) | 4 | P0 |
| **Sistem Penyakit Tanaman A** (Layu Fusarium — pemicu, visual, pengobatan) | 6 | P0 |
| Sistem Penyakit Tanaman B (Layu Bakteri) | 4 | P1 |
| Sistem Penyakit Tanaman E (Virus Gemini + vektor kutu kebul) | 6 | P1 |
| Sistem Penyakit Tanaman F (Damping-Off pada semaian) | 4 | P1 |
| Sistem hama (kutu daun, kutu kebul, ulat) | 5 | P1 |
| Crafting PesNab (semprot bawang putih + cabai + sabun) | 4 | P1 |
| **UI Panel Detail Raised Bed** (parameter tanah, status tanaman, aksi) | 8 | P0 |
| UI Diagnosis Penyakit Tanaman | 6 | P0 |
| Mekanik rotasi tanaman (bonus fiksasi nitrogen legum) | 3 | P2 |
| Mekanik panen (klik tanaman matang → kalkulasi hasil) | 3 | P0 |
| Indikator visual tanaman (menguning → shader klorosis, bercak → overlay tekstur) | 5 | P0 |
| Efek cuaca pada tanaman (hujan = auto-siram, mendung = -15% pertumbuhan) | 4 | P2 |
| Audio spesifik bedengan (siram, gemerisik daun) | 2 | P2 |

**Milestone: P2 — "Prototipe Siklus Tertutup"**
- Siklus Lele → air → tanaman berfungsi
- Pemain dapat mengelola akuakultur dan hortikultura
- 2+ penyakit tanaman dapat diobati
- **Skor Loop Health v1** sekarang dapat diukur

---

### FASE 3: Integrasi BSF & Ayam (Bulan 7–8)

**Tujuan:** Lengkapi siklus protein. Sisa dapur → maggot → pakan ayam → telur. Kotoran ayam → kompos → tanah.

| Tugas | Perk. Hari | Prioritas |
|------|-----------|----------|
| **Engine Siklus Hidup BSF** (telur → larva → prepupa → pupa → dewasa) | 8 | P0 |
| Model 3D Biopond (box, ramp 45°, kontainer penampungan) | 4 | P0 |
| Model larva BSF + animasi (menggeliat di substrat) | 4 | P0 |
| Model lalat dewasa BSF + sistem partikel kawanan | 3 | P0 |
| Manajemen substrat (tambah sisa dapur, kelembapan, anti-bau dengan EE) | 5 | P0 |
| Mekanik auto-harvest (prepupa memanjat ramp → kumpulkan) | 4 | P0 |
| Kandang kawin BSF (penutup kasa, bilah kayu untuk bertelur) | 4 | P0 |
| **Sistem Ayam** (kesehatan, lapar, produksi telur, stres) | 6 | P0 |
| Model 3D ayam + animasi (diam, mengais, makan, bertelur) | 6 | P0 |
| Model 3D kandang (di bawah atap, kotak sarang, tempat pakan) | 4 | P0 |
| **Engine Deep Litter** (keseimbangan C:N, panas fermentasi, kematangan, bau) | 8 | P0 |
| Animasi ayam mengais → auto-aerasi | 3 | P0 |
| Mekanik pencampuran pakan (50% komersial + 25% sayuran + 25% maggot) | 4 | P0 |
| Mekanik koleksi telur (rutinitas pagi harian) | 2 | P0 |
| Integrasi kotoran ayam → kompos | 3 | P0 |
| UI Panel Detail BSF | 4 | P0 |
| UI Panel Detail Ayam | 4 | P0 |
| Sistem Penyakit Klinis C (Aeromonas — penuh) | 5 | P1 |
| Sistem Penyakit Klinis F (Kepala Pecah) | 4 | P2 |
| Sistem Penyakit Klinis G (Penyakit Kuning) | 4 | P2 |
| Sistem Penyakit Klinis H (Bintik Putih) | 4 | P2 |
| Audio spesifik BSF (dengung, gerakan larva) | 2 | P2 |
| Audio spesifik ayam (berkokok, mengais) | 2 | P2 |

**Milestone: P3 — "Siklus Protein Lengkap"**
- Semua 4 subsistem inti saling terhubung: Lele + Tanaman + BSF + Ayam
- Aliran sumber daya: dapur → maggot → ayam → kotoran → kompos → tanah
- **Skor Loop Health berfungsi penuh** melacak semua aliran sumber daya
- 5+ kondisi klinis ikan terimplementasi

---

### FASE 4: Kompos, EE & Booster (Bulan 9–10)

**Tujuan:** Tambah kedalaman crafting. Semua resep booster organik, penguasaan kompos, produksi EE, multiplikasi EM4.

| Tugas | Perk. Hari | Prioritas |
|------|-----------|----------|
| **Engine Komposter** (rasio CN, fase suhu, kematangan, pembalikan) | 6 | P0 |
| Model 3D Komposter (drum berputar, partikel uap) | 3 | P0 |
| Mesin pencacah daun (input pakan → output daun tercacah) | 3 | P0 |
| **Sistem Eco-Enzyme** (rasio 3:1:10, fermentasi, tahap maturasi, pelacakan pH) | 6 | P0 |
| Model kontainer EE (berbagai ukuran) | 2 | P0 |
| Mekanik pelepasan gas EE ("sendawakan" harian selama bulan pertama) | 2 | P0 |
| **Bio-Multiplikasi EM4** (produksi EM-Aktif, pemeriksaan kualitas) | 4 | P1 |
| **Crafting K-Booster Ninja** (batang pisang + sabut kelapa + molase + leri + EE) | 4 | P1 |
| **Crafting Aminor-Grow** (kepala/jeroan lele + air kelapa + molase + EE) | 4 | P1 |
| **Crafting Cal-Phos Liquid** (cangkang telur sangrai + tulang + cuka kayu) | 4 | P1 |
| **Crafting Mag-Elixir** (garam Epsom + air kelapa + EE) | 2 | P2 |
| **Sistem Humo-Ninja** (pembuatan biochar + charging + aplikasi) | 5 | P2 |
| **Serum JMS-IMO** (humus bambu + kentang + garam + aerasi) | 5 | P2 |
| **Humat-Fulvat Teraktivasi** (peningkatan humat komersial dengan EE) | 3 | P2 |
| **Ekstraksi Humat Alkalin DIY** (lindi abu kayu + ekstraksi kompos) | 4 | P2 |
| UI Buku Crafting (browser resep, pelacakan bahan, manajemen antrian) | 8 | P0 |
| Mekanik aplikasi booster (siram tanah, semprot daun, kalkulasi dosis) | 4 | P0 |
| Efek booster pada pertumbuhan tanaman (pengubah parameter) | 4 | P0 |
| Sistem inventaris (menyimpan booster, EE, EM-Aktif yang di-craft) | 4 | P0 |
| Sistem Penyakit Tanaman C (Antraknosa pada cabai) | 4 | P2 |
| Sistem Penyakit Tanaman D (Late Blight pada tomat) | 4 | P2 |
| Sistem Penyakit Tanaman G (Karat Putih pada kangkung) | 3 | P2 |

**Milestone: P4 — "Master Crafter"**
- Semua 4 resep booster organik dapat di-craft dan diaplikasikan
- Sistem Kompos + EE + EM4 berfungsi penuh
- Pertumbuhan tanaman dapat dioptimalkan jauh melampaui baseline dengan booster
- Semua 7 kondisi klinis tanaman terimplementasi

---

### FASE 5: Edukasi, Ekonomi & Mode Permainan (Bulan 11–12)

**Tujuan:** Kerangka edukasi penuh, sistem ekonomi, mode permainan, poles.

| Tugas | Perk. Hari | Prioritas |
|------|-----------|----------|
| **Mode Cerita** (progresi terbimbing 16 bab, dialog NPC Mentor Ninja) | 15 | P0 |
| Model NPC Mentor Ninja + animasi | 5 | P0 |
| Sistem overlay tutorial (panduan langkah demi langkah) | 8 | P0 |
| **Mode Kelas** (dasbor guru, pembuatan kelas, sistem tugas) | 15 | P0 |
| Alat pembuat skenario (menghadap guru) | 10 | P0 |
| Pelacakan progres siswa + dasbor analitik | 10 | P0 |
| **Sistem Sertifikasi** (ujian Dasar, Lanjutan, Master, Pengajar) | 12 | P1 |
| Pembuatan kartu laporan otomatis | 5 | P1 |
| **Sistem Ekonomi Penuh** (pasar, balancing kredit, pelacakan pengeluaran) | 10 | P0 |
| **Basis Pengetahuan** (referensi buku dalam game, SOP yang dapat dicari, formula) | 8 | P0 |
| **Pembuat Kasus Klinis** (pembuatan tantangan prosedural) | 10 | P1 |
| Mode Tantangan (skenario harian/mingguan/kustom) | 8 | P1 |
| Implementasi monetisasi (toko kosmetik, ekspansi, token waktu) | 10 | P0 |
| Sistem achievement (50+ achievement) | 5 | P2 |
| Panel pengaturan (audio, video, bahasa, aksesibilitas, kontrol) | 5 | P0 |
| Pass lokalisasi penuh (ID + EN) | 10 | P0 |
| Pass optimasi performa (semua platform) | 10 | P0 |
| Stress testing (10+ pemain bersamaan, subsistem maks) | 5 | P0 |

**Milestone: P5 — "Kandidat Peluncuran"**
- Semua sistem, mode, dan fitur terimplementasi
- Kerangka edukasi lengkap
- Monetisasi terintegrasi
- Siap untuk beta tertutup

---

### FASE 6: Poles, Beta & Peluncuran (Bulan 13–14)

**Tujuan:** Kualitas, pembangunan komunitas, peluncuran resmi.

| Tugas | Perk. Hari | Prioritas |
|------|-----------|----------|
| Beta Tertutup — undang 100–500 pemain | 14 | P0 |
| Beta Edukator — 5–10 sekolah uji mode kelas | 14 | P0 |
| Sprint perbaikan bug (patch mingguan) | 20 | P0 |
| Tuning keseimbangan (ekonomi, laju pertumbuhan, kesulitan penyakit) | 10 | P0 |
| Poles UI/UX (waktu animasi, interaksi mikro, transisi) | 10 | P1 |
| Poles visual (pencahayaan, post-processing, penyempurnaan material) | 10 | P1 |
| Poles audio (mixing, rentang dinamis, optimasi mobile) | 5 | P2 |
| Poles performa (optimasi mobile, Xbox) | 10 | P0 |
| QA lokalisasi (tinjauan penutur asli) | 5 | P1 |
| Produksi trailer peluncuran | 5 | P1 |
| Aset halaman toko (tangkapan layar, deskripsi, tag) | 3 | P1 |
| Kit pers + materi penjangkauan edukator | 5 | P1 |
| Setup server Discord + alat moderasi | 3 | P1 |
| Rencana dukungan hari peluncuran | 3 | P0 |

**Milestone: P6 — "Peluncuran 1.0"**
- Rilis publik di platform Roblox
- Lisensi kelas tersedia untuk dibeli
- Saluran komunitas aktif

---

### FASE 7: Pasca-Peluncuran (Bulan 15+)

**Tujuan:** Pertahankan, perluas, sempurnakan berdasarkan data pemain dan umpan balik.

> **Catatan:** Konten pasca-peluncuran di bawah adalah **pembaruan gratis** untuk semua pemain. Ini berbeda dengan **Paket Ekspansi DLC** (Stroberi Vertikultur, Pepaya California, Budikdamber, Hidroponik Sederhana — lihat `01-Master-Plan.md` Section 8.2) yang merupakan konten premium berbayar yang dirilis bertahap selama Fase 3–5.

| Kuartal | Fokus | Jenis |
|---------|-------|-------|
| **K1 Pasca-Peluncuran** | Perbaikan bug, patch keseimbangan, event musiman pertama, fitur QoL yang diminta komunitas | Gratis |
| **K2** | Mode Multiplayer Co-op (farm bersebelahan, perdagangan, fasilitas bersama, papan peringkat) | Gratis |
| **K3** | Ekspansi "Farm-to-Table" — sistem memasak menggunakan hasil panen, simulasi pasar petani | Gratis |
| **K4** | Ekspansi "Tantangan Iklim" — pertanian spesifik wilayah (tropis, kering, sedang), skenario perubahan iklim, adaptasi kekeringan/banjir | Gratis |
| **Tahun 2+** | Platform konten komunitas (tata letak farm bersama, skenario kustom), dukungan VR, kompetitor NPC AI | Gratis |

---

## 4. Daftar Risiko

| Risiko | Kemungkinan | Dampak | Mitigasi |
|------|-----------|--------|------------|
| Kompleksitas simulasi membuat pemain kewalahan | Sedang | Tinggi | Pengungkapan fitur progresif (FTUE); mode sederhana; tutorial unggul |
| Perubahan platform Roblox merusak sistem | Sedang | Sedang | Arsitektur modular; pemantauan API Roblox rutin; pertahankan suite pengujian |
| Adopsi edukator lebih rendah dari yang diharapkan | Sedang | Tinggi | Bermitra dengan 2–3 sekolah percontohan selama Fase 2; kumpulkan testimoni lebih awal |
| Masalah performa di mobile low-end | Tinggi | Sedang | Mode performa dari Fase 0; LOD agresif; batasi total parts |
| Akurasi simulasi dikritik ahli | Rendah | Tinggi | Tinjauan ahli materi di setiap fase; kutip sumber; disclaimer tentang penyederhanaan |
| Overrun anggaran DataStore | Rendah | Sedang | Serialisasi efisien; simpan delta (bukan simpan penuh setiap siklus); pantau penggunaan |
| Burnout dari scope creep | Sedang | Tinggi | Batas fase ketat; disiplin "vertical slice"; tinjauan scope rutin |
| Monetisasi dianggap pay-to-win | Sedang | Tinggi | Semua mekanik inti gratis; monetisasi hanya kosmetik, kenyamanan, dan fitur edukasi |
| Kompetitor merilis game serupa | Rendah | Sedang | Keunggulan first-mover di niche urban farming Roblox; eksekusi lebih cepat; pembangunan komunitas |
| Masalah kualitas lokalisasi | Rendah | Rendah | Tinjauan penutur asli; kontribusi terjemahan komunitas; pass LQA profesional |
| **Churn rate 5 menit pertama** (pemain drop sebelum momen "Aha!") | **SANGAT TINGGI** | **KRITIS** | Time-Skip tutorial gratis (Section 3.1 07-Gameplay); hadiah instan di menit 1–3; jangan biarkan pemain menunggu tanpa hasil |
| **UI tidak optimal di mobile** (70%+ pemain HP) | **TINGGI** | **TINGGI** | Mobile-first design dari Fase 0; radial menu + drag-and-drop; touch target min 48×48px; uji di perangkat low-end setiap sprint |
| **Offline progression bugs** (simulasi catch-up tidak akurat) | Sedang | Tinggi | Unit test ekstensif untuk kalkulasi offline; batas aman 24 jam; no-crisis mode; logging setiap catch-up untuk debugging |

---

## 5. Indikator Kinerja Utama (Per Fase)

| Fase | Metrik Keberhasilan | Target |
|-------|---------------|--------|
| P0 | UI mobile-centric teruji di perangkat low-end | >60 FPS di Android 4GB RAM |
| P1 | Pemain dapat menyelesaikan siklus lele penuh tanpa panduan | 80% penguji |
| P1 | Retensi 5-menit pertama (tutorial time-skip) | >70% pemain mencapai Hari 5 game |
| P2 | Skor Loop Health > 60% dapat dicapai | Diverifikasi QA |
| P3 | Siklus BSF → Ayam → Kompos berfungsi | Nol input pakan eksternal dimungkinkan |
| P4 | Semua 4 booster di-craft dan efektif | +20% peningkatan hasil diverifikasi |
| P5 | Mode kelas dapat digunakan oleh guru non-teknis | Onboarding guru 30 menit |
| P6 | Retensi D7 | > 35% |
| P7 | MAU berkelanjutan | > 50.000 |

---

## 6. Ringkasan Estimasi Sumber Daya

| Fase | Durasi | Jam Pengembang (perk.) | Hasil Kunci |
|-------|----------|-----------------|-----------------|
| P0: Fondasi | 2 bulan | 800 | Arsitektur, farm kosong |
| P1: Lele MVP | 2 bulan | 1.200 | Simulator budidaya ikan |
| P2: Tanaman MVP | 2 bulan | 900 | Prototipe siklus tertutup |
| P3: BSF + Ayam | 2 bulan | 1.000 | Siklus protein lengkap |
| P4: Booster | 2 bulan | 900 | Kedalaman crafting |
| P5: Edukasi + Ekonomi | 2 bulan | 1.400 | Kandidat peluncuran |
| P6: Poles + Peluncuran | 2 bulan | 800 | Rilis 1.0 |
| **TOTAL** | **14 bulan** | **~7.000** | — |

**Estimasi Anggaran (model kontraktor/studio):**
- 7 FTE × 14 bulan × tarif rata-rata → kisaran $500.000–$800.000 USD
- Alternatif: bootstrap dengan 2–3 pengembang pada timeline lebih panjang (18–24 bulan, $150.000–$300.000)

---

## 7. Langkah Selanjutnya Segera

1. **✅ Selesai:** Finalisasi dokumen rencana induk 6 dokumen ini
2. **Rekrut/tugaskan:** Pengembang Luau untuk arsitektur Fase 0
3. **Daftar aset:** Buat dokumen spesifikasi aset 3D detail dari rencana ini
4. **Prototipe:** Bangun TimeManager + interaksi Galon dasar sebagai proof-of-concept
5. **Mitra:** Identifikasi 2–3 sekolah untuk pengujian edukator Fase 1
6. **Komunitas:** Buat server Discord, mulai bangun daftar tunggu
7. **Pendanaan:** Jika pendanaan eksternal dibutuhkan, rencana induk ini berfungsi sebagai fondasi pitch deck

---

*Akhir Dokumentasi Rencana Induk.*

*Semua 6 dokumen selesai:*
- `01-Master-Plan.md` — Visi, gambaran, monetisasi
- `02-Sistem-Mekanik.md` — Mekanik game detail
- `03-Spesifikasi-Teknis-Roblox.md` — Arsitektur teknis
- `04-Kerangka-Edukasi.md` — Kerangka pendidikan
- `05-UI-UX-Design.md` — Spesifikasi UI/UX
- `06-Roadmap-Development.md` — Peta jalan pengembangan
