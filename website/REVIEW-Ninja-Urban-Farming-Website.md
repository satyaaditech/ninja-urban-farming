# REVIEW: Website Ninja Urban Farming

> **Tanggal:** 5 Juli 2026  
> **Reviewer:** AI Expert Urban Farming  
> **Sumber konten acuan:** `Katalog-Resep-Formulasi-Urban-Farming.md`, `Ninja-Urban-Farming.md`, `BluePrint.md`

---

## DAFTAR ISI

1. [Ringkasan Skor](#ringkasan-skor)
2. [A. Arsitektur & Setup Teknis](#a-arsitektur--setup-teknis)
3. [B. Kualitas Konten](#b-kualitas-konten)
4. [C. UX & Navigasi](#c-ux--navigasi)
5. [D. Kelengkapan Konten](#d-kelengkapan-konten)
6. [E. Rekomendasi Pengembangan](#e-rekomendasi-pengembangan)
7. [F. Action Items (Checklist)](#f-action-items-checklist)

---

## Ringkasan Skor

| Aspek | Skor | Status |
|-------|------|--------|
| Arsitektur | **7/10** | Setup Astro v7 benar, tapi filter kategori rusak |
| Akurasi Konten | **9/10** | Semua 53 formula cocok sumber, SOP detail |
| Kelengkapan Konten | **4/10** | Banyak SOP/klinis/referensi belum masuk |
| UX & Navigasi | **7/10** | IA bersih, mobile nav bagus, filter rusak |
| Desain Visual | **8/10** | Palet profesional, semua gambar placeholder |
| SEO & Metadata | **3/10** | Hanya meta dasar |
| Print-Friendly | **1/10** | Belum ada style cetak |
| Build Quality | **8/10** | 81 file HTML dibuild bersih |

---

## A. Arsitektur & Setup Teknis

### A1. Framework & Konfigurasi — Benar

- **Astro v7** dengan `output: 'static'` — pilihan tepat untuk situs dokumentasi ke GitHub Pages
- `astro.config.mjs` baris 9: `base: '/ninja-urban-farming'` sudah benar
- 4 content collections: `klinis-tanaman`, `sop`, `formulas`, `klinis-lele` — terstruktur baik
- Setiap collection pakai Zod schema validation

### A2. 🐛 BUG KRITIS: Filter Kategori Tidak Berfungsi

**Lokasi:** Semua 53 file `.md` di `src/content/formulas/`

**Masalah:** Setiap file punya `category: "Formula"` di frontmatter (baris 5). Akibatnya:
- `src/pages/katalog/index.astro` baris 8 menghasilkan deduplikasi `["Formula"]`
- Filter kategori di katalog (baris 41-45) cuma render 1 tombol — sama persis dengan "Semua"
- Fitur filter tidak berfungsi sama sekali

**Akar masalah:** File `src/data/formulas.json` (801 baris) punya 12 kategori asli (`ECO-ENZYME NINJA`, `4 FORMULA BOOSTER TANAMAN`, dll.), tapi file ini **tidak pernah dipakai** oleh halaman. Halaman pakai `getCollection('formulas')` yang baca `.md` files — semua dengan `category: "Formula"`.

**Cara perbaiki:** Update `category:` di semua 53 file frontmatter `.md` ke kategori yang benar sesuai `formulas.json`.

### A3. Pipeline Data Tidak Konsisten

- `src/data/formulas.json` — 53 entri lengkap dengan kategori benar, tag, ingredients, dosage preview, full markdown content. **Tidak digunakan oleh halaman manapun.**
- Satu-satunya pemakaian: link download CSV di `katalog/index.astro` baris 116 (`/data/formulas.csv`)
- Dua sumber kebenaran (`formulas.json` vs `.md` content collection) yang tidak sinkron

**Rekomendasi:** Pilih satu:
- (a) Fix frontmatter `.md` files ke kategori benar
- (b) Refactor halaman katalog untuk baca `formulas.json` langsung
- (c) Regenerasi semua `.md` dari `formulas.json` dengan metadata benar

### A4. SEO & Metadata — Kurang

**Yang sudah ada** (`Layout.astro` baris 16-26):
- `lang="id"`
- `viewport`, `description`, `title`
- Favicon

**Yang belum ada:**
- Open Graph tags (`og:title`, `og:description`, `og:image`)
- Twitter Card tags
- `robots` meta
- Canonical URL tag
- JSON-LD structured data (e.g., `Article` schema untuk SOP)
- Self-hosted fonts (saat ini Google Fonts CDN — pertimbangan GDPR)

### A5. Styling — Baik

- CSS custom properties system lengkap (`Layout.astro` baris 37-440)
- Palet hijau primer + amber/oren aksen
- Tipografi Inter + Merriweather
- Responsive breakpoints
- Card system, button variants, tag system
- Prose styles untuk rendering markdown
- Mobile hamburger menu dengan animasi CSS (`Navigation.astro` baris 166-200)

---

## B. Kualitas Konten

### B1. Formula — Akurat, Metadata Kurang

**Akurasi konten: 9/10.** Semua 53 formula diverifikasi cocok dengan `Katalog-Resep-Formulasi-Urban-Farming.md`:
- `eco-enzyme-ninja-eco-enzyme-dasar-mother-formula.md` — Cocok baris 32-71 sumber. Rasio, indikator, tabel penggunaan benar semua.
- `pestisida-organik-pesnab-pesnab-super-bawang-putih-cabai.md` — Cocok Bab 8.1. Bahan, prosedur, jadwal aplikasi, penjelasan ilmiah (allicin + capsaicin) benar.
- `4-formula-booster-tanaman-k-booster-ninja-kalium-buah-lebat.md` — Cocok Bab 2.1.

**Struktur konten di `.md` files bagus:**
- Frontmatter dengan title, description, pubDate, category, tags, ingredients arrays, dosage
- Body dalam Bahasa Indonesia dengan emoji (✅ sukses, ❌ gagal, ⚠️ peringatan)
- Catatan ilmiah (🔬) di akhir formula booster/pestisida

### B2. SOPs — 7 dari 7 Ada, Kualitas Tinggi

Semua SOP komplit:
- `sop-kangkung.md` (114 baris) — Dua metode propagasi (biji vs. stek batang), persiapan, penanaman, jadwal perawatan dengan dosis spesifik per hari, teknik panen + tumbuh ulang, tabel masalah & solusi. "Metode Ninja" (baris 44-46) untuk stek batang kangkung pasar sangat praktikal.
- `sop-tomat.md`, `sop-bayam.md`, `sop-sawi-sawian.md`, `sop-selada.md`, `sop-seledri.md`, `sop-daun-bawang.md`

### B3. 🐛 BUG: Malformed YAML di `layu-fusarium.md`

**File:** `src/content/klinis/tanaman/layu-fusarium.md` baris 18

```
''Pada tomat & cabai'': ''layu mendadak dalam 2-3 hari''
```

Format ini tidak valid untuk Zod schema parsing. Bisa menyebabkan build error atau data hilang secara diam-diam. **Harus diperbaiki.**

### B4. Gambar — Semua Placeholder

- Semua halaman pakai `ImagePlaceholder.astro`
- Caption deskriptif cukup untuk ilustrator, tapi tidak ada gambar asli
- `dist/images/placeholders/` ada tapi kosong

---

## C. UX & Navigasi

### C1. Information Architecture — Logis

| Level | Route | Konten |
|-------|-------|--------|
| Home | `/ninja-urban-farming/` | Hero, diagram closed-loop, SOP terbaru, jalur mulai |
| Tentang | `/ninja-urban-farming/tentang` | Visi, audiens, filosofi |
| SOP List | `/ninja-urban-farming/sop` | 7 kartu SOP dengan filter |
| SOP Detail | `/ninja-urban-farming/sop/[slug]` | SOP lengkap + breadcrumb |
| Katalog List | `/ninja-urban-farming/katalog` | 53 kartu formula, search + filter |
| Katalog Detail | `/ninja-urban-farming/katalog/[slug]` | Formula lengkap + breadcrumb |
| Klinis Hub | `/ninja-urban-farming/klinis` | Dua kartu hub → lele / tanaman |
| Klinis Lele List | `/ninja-urban-farming/klinis/lele` | 8 kartu penyakit, filter |
| Klinis Tanaman List | `/ninja-urban-farming/klinis/tanaman` | 6 kartu penyakit, filter |

### C2. Navigasi — Solid

- 5 item nav: Beranda, Tentang, SOP, Katalog, Klinis
- Active state detection pakai `startsWith`
- Breadcrumb di setiap halaman
- Mobile hamburger menu berfungsi baik

### C3. Search & Filter

- **Search box** (`katalog/index.astro` baris 32-58): Client-side, filter by title, description, tags, ingredients. Performa baik untuk 53 item.
- **Tag filter** (baris 49-56): 8 tag pertama. Berfungsi.
- **Category filter**: ❌ RUSAK (lihat bug A2 di atas)
- **Empty state** (baris 103-107): Ditampilkan saat tidak ada hasil.

### C4. Homepage — Desain Bagus

- Hero section dengan badge animasi gradient
- Statistik: "8+ SOP" — **seharusnya 7** (hanya 7 SOP yang ada)
- Dua CTA
- Grid Sistem Closed-Loop (BSF → Lele → Raised Bed → Ayam)
- Jalur "Mulai dari sini" untuk Pemula / Formula / Diagnosa

### C5. Print — Tidak Ada

- Tidak ada `@media print` di Layout.astro
- Tabel dengan `overflow-x: auto` akan terpotong saat diprint
- Nav sticky akan ikut keprint
- Header gelap boros tinta
- Padahal sumber katalog menyatakan "Cetak dan tempel di dekat area kerja"

---

## D. Kelengkapan Konten

### D1. SOP yang Hilang dari BluePrint

| BAB BluePrint | Konten | Status |
|---------------|--------|--------|
| BAB 2 | Setup Kolam Galon Lele Bioflok (Sistem 3 Galon) | ❌ TIDAK ADA |
| BAB 3 | Maggot BSF — Biopond, Siklus Kehidupan, Kelambu Lalat | ❌ TIDAK ADA |
| BAB 4 | Ayam Petelur — Deep Litter, Pakan Ninja | ❌ TIDAK ADA |
| BAB 5 | Panduan Budidaya Lele (formula pakan, sampling, panen) | ❌ TIDAK ADA |
| BAB 8 | Panduan Rotasi Sayuran & Pengendalian Hama | ❌ TIDAK ADA |
| BAB 9 | Jadwal Harian "Ninja" (Rutinitas 15 Menit/Hari) | ❌ TIDAK ADA |
| BAB 10 | Katalog Komoditas Integratif | ❌ TIDAK ADA |

**Sayuran yang belum ada SOP:**
- Cabai / Lombok (target K-Booster, Cal-Phos, PesNab)
- Terong (target K-Booster dan Cal-Phos)
- Stroberi (target K-Booster)

### D2. Klinis Lele — 5 dari 8 Hilang

| Ref BluePrint | Kondisi | Status |
|---------------|---------|--------|
| KLINIS A | Stres Amonia / Nitrit Akut (Menggantung Tegak, Kumis Keriting) | ❌ TIDAK ADA |
| KLINIS B | Jamur Putih / Cotton Wool (Saprolegnia) | ✅ ADA |
| KLINIS C | Luka Merah, Sirip Gripis, Dropsy (Aeromonas) | ✅ ADA |
| KLINIS D | Kembung Pakan / Obstruksi Usus | ❌ TIDAK ADA |
| KLINIS E | Mati Lampu / Blackout (>3 Jam) | ❌ TIDAK ADA |
| KLINIS F | Broken Head Syndrome (Defisiensi Vitamin C) | ❌ TIDAK ADA |
| KLINIS G | Jaundice / Penyakit Kuning (Aflatoksin) | ❌ TIDAK ADA |
| KLINIS H | White Spot / Bintik Putih (Ich) | ✅ ADA |

### D3. Klinis Tanaman — 4 dari 6 Hilang/Sebagian

| Ref BluePrint | Kondisi | Status |
|---------------|---------|--------|
| KLINIS TANAMAN A | Layu Fusarium + Layu Bakteri | ✅ ADA |
| KLINIS TANAMAN B | Antraknosa / Patek (Colletotrichum) | ❌ TIDAK ADA |
| KLINIS TANAMAN C | Busuk Daun / Late Blight (Phytophthora) | ⚠️ SEBAGIAN |
| KLINIS TANAMAN D | Virus Gemini / Kuning Bule | ❌ TIDAK ADA |
| KLINIS TANAMAN E | Damping-Off (Pythium) | ✅ ADA |
| KLINIS TANAMAN F | Karat Putih (Albugo) pada Kangkung | ❌ TIDAK ADA |

### D4. Bab Referensi Katalog — 4 Bab Hilang

Dari `Katalog-Resep-Formulasi-Urban-Farming.md` Daftar Isi:

| Bab | Konten | Nilai |
|-----|--------|-------|
| 13 | Cheat Sheet Dosis & Rasio | Referensi cepat semua aplikasi formula |
| 14 | Tabel Konversi Satuan Dapur | Kritis: sdm → gram, dll. |
| 15 | Ringkasan Semua Formula Booster | Tabel ringkasan 16 booster |
| 16 | **Tabel Indeks Cepat — Kegunaan & Aplikasi** | Tabel paling bernilai: cari berdasarkan gejala/kebutuhan → ketemu formula |

> **Bab 16** sangat penting — tabel raksasa terindeks per kategori (A–K) dengan nama formula, komposisi, kegunaan, dan cara aplikasi. Ini akan jadi halaman `/katalog/indeks-cepat` atau wizard "Cari berdasarkan kebutuhan."

---

## E. Rekomendasi Pengembangan

### E1. 🚨 Perbaikan Kritis (Harus Sebelum Publish)

| # | Tugas | Estimasi |
|---|-------|----------|
| 1 | **Fix category frontmatter** di 53 file `.md` formula | 30 menit |
| 2 | **Fix malformed YAML** di `layu-fusarium.md` baris 18 | 5 menit |
| 3 | **Fix stat hero** `index.astro` baris 38: "8+" → "7" | 1 menit |

### E2. 📝 Konten Prioritas Tinggi (Materi Sumber Sudah Ada)

| # | Tugas | Sumber |
|---|-------|--------|
| 4 | **SOP Lele Bioflok** — sistem 3 galon, aerasi, sampling | BluePrint BAB 2+5, Ninja-Urban-Farming BAB 5+7 |
| 5 | **SOP Maggot BSF** — biopond, siklus, kelambu | BluePrint BAB 3 |
| 6 | **SOP Ayam Petelur Deep Litter** — alas, pakan, manajemen | BluePrint BAB 4 |
| 7 | **Halaman Indeks Cepat** (`/katalog/indeks-cepat`) | Katalog Bab 16 (baris 1102-1256) |
| 8 | **Lengkapi Klinis Lele** — 5 entri (A, D, E, F, G) | BluePrint + Ninja-Urban-Farming Lampiran Klinis |
| 9 | **Lengkapi Klinis Tanaman** — 3 entri (B, D, F) + perbaiki C | BluePrint BAB 7 |
| 10 | **Cheat Sheet Dosis** (`/katalog/cheat-sheet`) | Katalog Bab 13 |
| 11 | **Jadwal Harian Ninja** (`/jadwal-harian`) | BluePrint BAB 9, Ninja-Urban-Farming BAB 19 |

### E3. 🔧 Fitur (Prioritas Menengah)

| # | Fitur | Keterangan |
|---|-------|------------|
| 12 | **Site-wide search** — tidak hanya di katalog, tapi semua konten (SOP, klinis, formula). Bisa pakai Pagefind (static search untuk Astro). | |
| 13 | **Print-friendly styles** — `@media print` di `Layout.astro`: sembunyikan nav, hilangkan background gelap, teks hitam, tabel full-width. | |
| 14 | **Google Sheets integration** — koneksi live ke Google Sheets untuk data formula, fetch saat build time. | |
| 15 | **Fix CSV download** — pastikan `formulas.csv` digenerate saat build dari `formulas.json`. | |
| 16 | **Gambar asli** — ganti semua `ImagePlaceholder` dengan foto/gambar sebenarnya. | |

### E4. 🚀 Visi Jangka Panjang

| # | Ide | 
|---|-----|
| 17 | **Pipeline Obsidian → Website** — otomatisasi sinkron konten dari vault Obsidian ke content collections Astro. |
| 18 | **PWA (Progressive Web App)** — akses offline untuk petani di lahan tanpa internet. |
| 19 | **Roblox Integration** — companion guide untuk game edukasi Roblox (folder `roblox/` sudah ada). |
| 20 | **Multilingual** — versi Bahasa Inggris untuk jangkauan internasional. |
| 21 | **Kontribusi Komunitas** — GitHub-based flow untuk user submit variasi formula atau modifikasi lapangan. |

---

## F. Action Items (Checklist)

### Fase 1: Perbaikan Bug (sebelum publish)
- [ ] Fix `category:` frontmatter di 53 file `.md` formula
- [ ] Fix malformed YAML di `layu-fusarium.md` baris 18
- [ ] Fix stat hero "8+ SOP" → "7 SOP"

### Fase 2: Konten Inti (minimum viable)
- [ ] SOP Lele Bioflok (sistem 3 galon)
- [ ] SOP Maggot BSF
- [ ] SOP Ayam Petelur Deep Litter
- [ ] 5 Klinis Lele yang hilang (A, D, E, F, G)
- [ ] 4 Klinis Tanaman yang hilang (B, C, D, F)
- [ ] Halaman Indeks Cepat (`/katalog/indeks-cepat`)

### Fase 3: Referensi & Tools
- [ ] Cheat Sheet Dosis (`/katalog/cheat-sheet`)
- [ ] Tabel Konversi Satuan Dapur
- [ ] Jadwal Harian Ninja
- [ ] Halaman Rotasi Sayuran & Companion Planting

### Fase 4: UX & Fitur
- [ ] Site-wide search (Pagefind)
- [ ] Print-friendly CSS
- [ ] Google Sheets live integration
- [ ] Gambar asli untuk semua placeholder

### Fase 5: Visi Jangka Panjang
- [ ] PWA offline support
- [ ] Obsidian → Website automation
- [ ] Roblox companion guide
- [ ] English translation
- [ ] Community contribution flow

---

> **Kesimpulan:** Website sudah punya fondasi teknis yang solid (Astro v7, content collections, styling profesional) dan konten yang akurat. Gap terbesar adalah **kelengkapan konten** — baru ~40% dari total materi sumber yang masuk. Perbaiki bug filter kategori dulu, lalu fokus tambah SOP Lele/BSF/Ayam dan lengkapi klinis. Indeks Cepat adalah quick-win paling berdampak untuk kegunaan harian.
