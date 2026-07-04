# 18 — DAFTAR KEBUTUHAN ASET VISUAL LENGKAP

> **Tujuan:** Peta lengkap seluruh kebutuhan diagram, infografis, wireframe, dan ilustrasi yang harus dibuat untuk mendukung dokumen GDD. Disusun per file, per bagian, dengan target audiens dan jenis visual yang direkomendasikan.
>
> **Cara Pakai:** Tim Artist/Designer menggunakan dokumen ini sebagai *work order*. Centang `⬜ → ✅` setelah visual selesai dibuat.

---

## RINGKASAN

| File Sumber | Jumlah Visual | Target Utama |
|-------------|--------------|--------------|
| `01-Master-Plan.md` | 4 | Investor, Stakeholder |
| `02-Sistem-Mekanik.md` | 8 | Developer, Designer |
| `03-Spesifikasi-Teknis-Roblox.md` | 5 | Programmer |
| `04-Kerangka-Edukasi.md` | 4 | Edukator, Investor |
| `05-UI-UX-Design.md` | 6 | UI/UX Designer, Programmer |
| `06-Roadmap-Development.md` | 3 | Produser, Investor |
| `07-Gameplay.md` | 6 | Game Designer, Investor |
| `08-Katalog-Komoditas.md` | 6 | 3D Artist, Tech Artist |
| `09-Validasi-Ilmiah.md` | 1 | Investor, Edukator |
| `11-Art-Bible.md` | 2 | 3D Artist |
| `12-Data-Schema-API.md` | 2 | Programmer |
| **TOTAL** | **47** | — |

---

## FILE 1: `01-Master-Plan.md`

| # | Bagian | Jenis Visual | Deskripsi | Target | Status |
|---|--------|-------------|-----------|--------|--------|
| 1 | §2 — Pilar Utama | Infografis | 6 pilar utama game dalam format visual (ikon + deskripsi singkat), cocok untuk slide presentasi investor | Investor | ⬜ |
| 2 | §5 — Gambaran Sistem Game | Diagram Alir (Flowchart) | Menggantikan ASCII art saat ini dengan diagram alir visual yang menunjukkan hubungan antar 8 subsistem (Lele → Raised Bed → Dapur → Komposter → BSF → Ayam, dll.) | Investor, Developer | ⬜ |
| 3 | §8.2 — Aliran Pendapatan Monetisasi | Infografis / Tabel Visual | Piramida atau diagram lingkaran yang menunjukkan proporsi pendapatan: Kosmetik, Ekspansi, Lisensi Kelas, Token Waktu, dll. | Investor | ⬜ |
| 4 | §11 — Lanskap Kompetitif | Diagram Perbandingan | Matriks posisi kompetitif: sumbu X = Akurasi Ilmiah, sumbu Y = Aksesibilitas. Posisi Ninja UF vs kompetitor | Investor | ⬜ |

---

## FILE 2: `02-Sistem-Mekanik.md`

| #   | Bagian                                  | Jenis Visual                  | Deskripsi                                                                                                                                              | Target              | Status |
| --- | --------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- | ------ |
| 5   | §1.2 — Simulasi Kimia Air               | State Diagram (Mermaid)       | Diagram hubungan sebab-akibat: aksi pemain (flush, beri pakan, tambah dolomit) → perubahan parameter (pH, NH₃, DO). Visualisasi rumus delta            | Developer           | ⬜      |
| 6   | §1.3 — Model Pertumbuhan Ikan           | Diagram Fase (Timeline)       | Timeline visual 3 fase (Starter → Grower → Finisher) dengan ABW, hari, kode pelet, dan feeding rate                                                    | Developer, Designer | ⬜      |
| 7   | §1.5 — Sistem Penyakit Ikan (8 Kondisi) | Matriks Ilustrasi             | Kartu visual 8 kondisi klinis: gambar gejala + parameter pemicu + pengobatan. Format seperti "kartu Pokemon" diagnostik                                | Designer, Edukator  | ⬜      |
| 8   | §2.2 — Siklus Hidup BSF                 | Flowchart Siklus (Mermaid)    | Diagram lingkaran siklus: Telur (3-4h) → Larva (14-18h) → Prepupa (1-2h) → Pupa (7-10h) → Dewasa (5-8h) → kembali ke Telur. Sertakan durasi waktu game | Developer, Designer | ⬜      |
| 9   | §3.2 — Model Fermentasi Deep Litter     | Diagram Proses                | Visualisasi proses fermentasi: input (daun kering + kotoran) → proses (C:N balance, suhu, aerasi ayam) → output (kompos matang 6 bulan)                | Developer           | ⬜      |
| 10  | §4.2 — Tabel Sumber Input Nutrisi       | Infografis Tabel              | Heatmap visual: baris = sumber nutrisi (Air lele, Kompos, EE, K-Booster, dll.), kolom = unsur (N, P, K, Ca, Mg). Warna menunjukkan tingkat kontribusi  | Designer, Developer | ⬜      |
| 11  | §7 — Crafting Booster Organik (4 Resep) | Diagram Resep / Crafting Tree | Pohon resep visual: bahan mentah → proses (fermentasi/campuran) → produk jadi → aplikasi + efek. Untuk K-Booster, Aminor-Grow, Cal-Phos, Mag-Elixir    | Designer            | ⬜      |
| 12  | §9 — Integrasi Siklus Tertutup          | Diagram Alir Sumber Daya      | Diagram Sankey atau flowchart berwarna yang menunjukkan semua aliran sumber daya antar 8+ subsistem, termasuk volume dan arah aliran                   | Investor, Developer | ⬜      |

---

## FILE 3: `03-Spesifikasi-Teknis-Roblox.md`

| # | Bagian | Jenis Visual | Deskripsi | Target | Status |
|---|--------|-------------|-----------|--------|--------|
| 13 | §3.1 — Hierarki ModuleScript | Diagram Pohon Folder | Visualisasi pohon folder (tree view) yang lebih mudah dibaca daripada ASCII art saat ini. Warna berbeda untuk Server / Replicated / Client | Programmer | ⬜ |
| 14 | §3.2 — Aliran Data Client-Server | Diagram Arsitektur (Mermaid Sequence) | Sequence diagram: Client Input → RemoteEvent → Server Validation → Simulation Engine → StateDelta → Client Renderer. Sertakan daftar RemoteEvent | Programmer | ⬜ |
| 15 | §4 — Arsitektur Tick Simulasi | Diagram Timing | Timeline visual yang menunjukkan: Server Tick (30 detik) vs Client Heartbeat (per frame). Kapan data disimpan, kapan delta dikirim | Programmer | ⬜ |
| 16 | §5.1 — Skema Data Pemain | Entity Relationship Diagram | ERD visual yang menunjukkan relasi: PlayerData → GalonLele[] → WaterState + Fish[]. PlayerData → RaisedBed[] → SoilState + PlantData. Dst. | Programmer | ⬜ |
| 17 | §6.3 — Indikator Parameter Visual | Matriks Referensi Visual | Tabel bergambar: kolom kiri = parameter (Amonia tinggi, DO rendah, dll.), kolom kanan = screenshot/mockup tampilan visual di game world | 3D Artist, Tech Artist | ⬜ |

---

## FILE 4: `04-Kerangka-Edukasi.md`

| # | Bagian | Jenis Visual | Deskripsi | Target | Status |
|---|--------|-------------|-----------|--------|--------|
| 18 | §1 — Filosofi Pendidikan | Diagram Siklus Kolb | Diagram lingkaran 4 tahap Kolb: Pengalaman Konkret → Observasi Reflektif → Konseptualisasi Abstrak → Eksperimentasi Aktif, dengan contoh game di setiap tahap | Edukator, Investor | ⬜ |
| 19 | §2.1 — Jalur Pembelajaran Terbimbing (16 Bab) | Peta Perjalanan (Learning Path Map) | Infografis jalur belajar bergambar: 16 bab sebagai "stasiun" di sepanjang jalan, dengan ikon topik dan estimasi durasi | Edukator, Investor | ⬜ |
| 20 | §3.1 — Kerangka Kompetensi (10 Kompetensi) | Diagram Radar/Spider | Diagram radar 10 sumbu (K1-K10) yang menunjukkan profil kompetensi pemain di berbagai tingkat kemahiran | Edukator | ⬜ |
| 21 | §6.1 — Pemetaan Kurikulum Indonesia | Infografis Pemetaan | Tabel visual berwarna: baris = tingkat kelas (SMP 7 → Universitas), kolom = mata pelajaran, isi = modul game yang relevan | Edukator, Investor | ⬜ |

---

## FILE 5: `05-UI-UX-Design.md`

| # | Bagian | Jenis Visual | Deskripsi | Target | Status |
|---|--------|-------------|-----------|--------|--------|
| 22 | §2.1 — Hierarki Layar | Diagram Sitemap | Sitemap visual bergambar: Menu Utama → sub-menu → layar game → panel → modal. Menggantikan ASCII tree saat ini | UI Designer | ⬜ |
| 23 | §3.1 — Tata Letak HUD | Wireframe Mobile | Wireframe layar HP 5-6 inci: posisi bilah atas, bilah mini subsistem (kiri bawah), aksi cepat (kanan bawah), area dunia game (tengah) | UI Designer, Programmer | ⬜ |
| 24 | §3.4 — Aksi Cepat (Radial Menu) | Mockup Interaksi | Mockup radial menu dalam konteks: pemain dekat galon lele → muncul 4 opsi melingkar (Beri Pakan, Flush, Sampling, Obati) | UI Designer | ⬜ |
| 25 | §4.1 — Panel Lele Bioflok | Mockup UI Panel | Hi-fi mockup panel detail lele: gauge parameter, info populasi, info pakan, tombol aksi. Versi mobile (full-screen overlay) | UI Designer, Programmer | ⬜ |
| 26 | §4.3 — Dasbor Loop Health | Mockup UI Dasbor | Mockup dasbor Loop Health: 5 kategori dengan progress bar, skor keseluruhan, grafik tren 7 hari | UI Designer | ⬜ |
| 27 | §5.1 — Aliran Diagnosis Klinis | Flowchart UX | Flowchart UX lengkap: Peringatan muncul → Inspeksi → Baca Data → Pilih Diagnosis → Pilih Pengobatan → Hasil + Laporan. Dengan mockup setiap layar | UI Designer | ⬜ |

---

## FILE 6: `06-Roadmap-Development.md`

| # | Bagian | Jenis Visual | Deskripsi | Target | Status |
|---|--------|-------------|-----------|--------|--------|
| 28 | §2 — Struktur Tim | Diagram Organisasi | Org chart visual: 10 peran dengan ikon, jumlah FTE, dan garis tanggung jawab | Produser, Investor | ⬜ |
| 29 | §3 — Rincian Fase (Fase 0-7) | Gantt Chart (Mermaid Gantt) | Timeline horizontal 14 bulan: Fase 0 (Bulan 1-2) → Fase 1 (Bulan 3-4) → ... → Fase 6 (Bulan 13-14). Warna berbeda per fase, milestone ditandai | Produser, Investor | ⬜ |
| 30 | §4 — Daftar Risiko | Matriks Risiko | Matriks 2D: sumbu X = Kemungkinan (Rendah-Tinggi), sumbu Y = Dampak (Rendah-Kritis). Plot setiap risiko sebagai titik berwarna | Produser, Investor | ⬜ |

---

## FILE 7: `07-Gameplay.md`

| # | Bagian | Jenis Visual | Deskripsi | Target | Status |
|---|--------|-------------|-----------|--------|--------|
| 31 | §2 — Core Loop | Diagram Siklus (Mermaid) | Diagram siklus 4 tahap: Observasi → Analisis → Aksi → Refleksi, menggantikan ASCII art saat ini. Dengan ikon dan warna | Investor, Designer | ⬜ |
| 32 | §3 — Player Journey (4 Tahap) | Infografis Timeline Pemain | Timeline horizontal: Pemula (Hari 1-15) → Praktisi (16-45) → Ahli (46-75) → Ninja Master (76+). Setiap tahap memiliki ikon, sistem yang terbuka, dan momen "Aha!" | Designer, Investor | ⬜ |
| 33 | §3.1 — FTUE (5 Menit Pertama) | Flowchart Tutorial | Flowchart langkah demi langkah: bergabung → pilih bahasa → sinematik → pilih mode → NPC memandu → setup galon → Time-Skip → tebar ikan. Kritis untuk retensi | Designer | ⬜ |
| 34 | §8 — Kurva Kesulitan | Grafik Kurva | Grafik garis: sumbu X = Waktu, sumbu Y = Kesulitan. Tangga naik bertahap dari "1 Galon" hingga "Krisis Multi-Sistem", menggantikan ASCII graph saat ini | Designer | ⬜ |
| 35 | §9.2 — Loop Organik Lengkap | Diagram Alir Ekosistem | Diagram alir besar berwarna: Sisa Dapur → BSF → Maggot → Ayam → Telur + Kotoran → Kompos → Tanah → Sayuran → Dapur (loop). Menggantikan ASCII art saat ini | Investor, Edukator | ⬜ |
| 36 | §11 — Sehari dalam Game | Infografis Timeline Harian | Infografis bergambar "Sehari Sebagai Ninja Farmer": strip horizontal dari 06:00 → 19:00 dengan ikon aktivitas di setiap jam. Menggantikan ASCII box saat ini | Designer, Investor | ⬜ |

---

## FILE 8: `08-Katalog-Komoditas.md`

| # | Bagian | Jenis Visual | Deskripsi | Target | Status |
|---|--------|-------------|-----------|--------|--------|
| 37 | §1 — Daftar Komoditas | Infografis Katalog | Infografis "menu" bergambar: 11 tanaman + 3 hewan dengan ikon, nama, dan julukan Ninja. Menggantikan ASCII box saat ini | Designer, Investor | ⬜ |
| 38 | §2-3 (semua spesies) — Fase Pertumbuhan | Kumpulan Ilustrasi / Sketsa | Untuk setiap tanaman: strip horizontal 4-5 gambar dari Semai → Vegetatif Awal → Vegetatif Akhir → Panen → (Berbuah). Panduan absolut bagi 3D Modeler | 3D Artist | ⬜ |
| 39 | §7 — Matriks Rotasi Tanaman | Diagram Rotasi (Mermaid/Infografis) | Diagram visual 4 bedengan × 3 siklus rotasi: warna berbeda per jenis tanaman, panah menunjukkan perpindahan. Menggantikan ASCII diagram saat ini | Designer, Edukator | ⬜ |
| 40 | §10.2-10.6 — Matriks Defisiensi | Matriks Ilustrasi Shader | Matriks visual besar: baris = jenis defisiensi (N, P, K, Ca, Mg), kolom = spesies. Setiap sel berisi gambar close-up daun/buah yang menunjukkan gejala spesifik. Panduan utama bagi Tech Artist | Tech Artist | ⬜ |
| 41 | §10 — Perbedaan Defisiensi N vs Mg vs Fe | Diagram Perbandingan 3-Panel | 3 gambar daun berdampingan: (1) N = kuning merata, (2) Mg = kuning antar tulang daun, (3) Fe = daun muda kuning. Kritis untuk diagnostik gameplay | Tech Artist, Edukator | ⬜ |
| 42 | §4.1 — Mekanik Fiksasi Nitrogen Kacang Panjang | Diagram Sebelum-Sesudah | Visualisasi tanah sebelum legum (N=40%) vs sesudah (N=65-80%), dengan ilustrasi bintil akar Rhizobium | Designer, Edukator | ⬜ |

---

## FILE 9: `09-Validasi-Ilmiah.md`

| # | Bagian | Jenis Visual | Deskripsi | Target | Status |
|---|--------|-------------|-----------|--------|--------|
| 43 | §9 — Kesimpulan Akhir (Tabel Akurasi) | Infografis Ringkasan | Pie chart atau bar chart: 78 Akurat (92.9%) vs 6 Approximasi (7.1%) vs 0 Tidak Akurat. Badge "TIDAK DITEMUKAN HALUSINASI AI" | Investor, Edukator | ⬜ |

---

## FILE 10: `11-Art-Bible.md`

| # | Bagian | Jenis Visual | Deskripsi | Target | Status |
|---|--------|-------------|-----------|--------|--------|
| 44 | §1 — Style Guide Visual | Mood Board / Style Reference | Kumpulan gambar referensi gaya visual: contoh "low-poly stylized realism", palet warna, contoh pencahayaan, referensi game serupa (Loomian Legacy, Adopt Me) | 3D Artist | ⬜ |
| 45 | §6.2 — Tanaman (55 Model) | Sprite Sheet Referensi | Untuk setiap spesies: strip referensi 4-5 fase pertumbuhan dengan skala poly yang direkomendasikan. Berguna sebagai checklist visual produksi | 3D Artist | ⬜ |

---

## FILE 11: `12-Data-Schema-API.md`

| #   | Bagian                    | Jenis Visual                | Deskripsi                                                                                                                                                          | Target     | Status |
| --- | ------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | ------ |
| 46  | §1 — DataStore Schema     | Entity Relationship Diagram | ERD visual penuh: PlayerData sebagai root → relasi ke WaterState, Fish[], SoilState, PlantData, BSFColonyState, dll. Dengan tipe data dan kardinalitas             | Programmer | ⬜      |
| 47  | §2 — RemoteEvent Contract | Sequence Diagram            | Diagram sekuens: panah Client → Server (PerformAction, CraftRecipe, SubmitDiagnosis) dan Server → Client (SyncState, StateDelta, ClinicalAlert). Dengan rate limit | Programmer | ⬜      |

---

## PRIORITAS PRODUKSI

### Prioritas P0 — Wajib untuk Pitching & Fase 1 (16 item)
> Visual ini dibutuhkan untuk presentasi investor dan pengembangan Fase 0-1.

| # | Item | File |
|---|------|------|
| 2 | Diagram Sistem Game (8 subsistem) | 01-Master-Plan |
| 5 | State Diagram Kimia Air | 02-Sistem-Mekanik |
| 7 | Kartu 8 Kondisi Klinis Ikan | 02-Sistem-Mekanik |
| 12 | Diagram Alir Siklus Tertutup | 02-Sistem-Mekanik |
| 14 | Arsitektur Client-Server | 03-Spesifikasi-Teknis |
| 16 | ERD Skema Data | 03-Spesifikasi-Teknis |
| 23 | Wireframe HUD Mobile | 05-UI-UX-Design |
| 25 | Mockup Panel Lele | 05-UI-UX-Design |
| 27 | Flowchart UX Diagnosis | 05-UI-UX-Design |
| 29 | Gantt Chart Roadmap | 06-Roadmap |
| 31 | Diagram Core Loop | 07-Gameplay |
| 33 | Flowchart FTUE | 07-Gameplay |
| 35 | Diagram Loop Organik | 07-Gameplay |
| 40 | Matriks Defisiensi Shader | 08-Katalog |
| 43 | Infografis Validasi Ilmiah | 09-Validasi |
| 44 | Mood Board Art Style | 11-Art-Bible |

### Prioritas P1 — Dibutuhkan untuk Fase 2-3 (18 item)
> Item: 1, 3, 6, 8, 9, 10, 11, 13, 15, 17, 18, 19, 22, 24, 26, 32, 37, 38

### Prioritas P2 — Nice-to-Have (13 item)
> Item: 4, 20, 21, 28, 30, 34, 36, 39, 41, 42, 45, 46, 47

---

## CATATAN TEKNIS

### Format File Visual
- **Diagram Mermaid:** Dapat langsung disisipkan ke dalam file .md menggunakan blok kode ` ```mermaid `. Kompatibel dengan `inject_visuals.py`.
- **Wireframe & Mockup UI:** Format PNG/SVG, resolusi 1920×1080 minimum.
- **Ilustrasi 3D/Shader:** Format PNG dengan latar transparan, resolusi 512×512 minimum per panel.
- **Infografis:** Format PNG/SVG, lebar 1200px minimum untuk keterbacaan di layar.

### Penamaan File Visual
```
roblox/visuals/
├── diagrams/         ← Mermaid dan flowchart
├── wireframes/       ← UI mockup dan wireframe
├── infographics/     ← Infografis untuk investor/edukator
├── references/       ← Referensi visual untuk 3D artist
└── shader-guides/    ← Panduan defisiensi untuk tech artist
```

---

*Terakhir diperbarui: 2026-07-04*
*Total item visual: 47*
*Sumber: Audit menyeluruh terhadap 18 file dalam folder `roblox/`*
