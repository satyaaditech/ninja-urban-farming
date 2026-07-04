---
judul: "Project Briefing — Ninja Urban Farming"
tanggal: "2026-06-26"
tag:
  - briefing
  - meta
  - project
status: 🌿
---

# PROJECT BRIEFING: Ninja Urban Farming

> [!important] Untuk AI Baru — Baca Ini Dulu
> File ini adalah dokumen onboarding untuk AI yang baru bergabung. Baca seluruh isi file ini **sebelum memulai pekerjaan apapun**. File ini mencakup seluruh konteks proyek, struktur direktori, konvensi penulisan, dan status terkini.

---

## 1. GAMBARAN BESAR PROYEK

**Proyek:** Menulis buku panduan berjudul **"Ninja Urban Farming"** — Panduan Lengkap Sistem Ketahanan Pangan Keluarga 100% Organik.

**Konsep Inti:** Buku ini mengajarkan sistem **closed-loop** di halaman rumah 75 m² (dapat diskalakan ke 6-100 m²) di mana:

```
Sampah Dapur → Maggot BSF → Pakan Lele & Ayam
                         ↓
Kotoran Lele (Air Bioflok) + Kotoran Ayam (Kompos) → Pupuk Raised Bed
                         ↓
Sayur Segar, Telur, Ikan → Dapur (siklus berulang)
```

**Filosofi "Ninja":** Efisien waktu (15 menit/hari), minim tenaga, presisi, tanpa limbah, tanpa bau, 100% organik.

**Target Pembaca:** Keluarga Indonesia yang ingin kemandirian pangan dari halaman sendiri.

---

## 2. STRUKTUR DIREKTORI PROYEK

Root proyek berada di: `/Users/satyaadidharma/Urban Farming/`

```
Urban Farming/
│
├── BluePrint.md                  # Raw blueprint — seluruh konten teknis mentah (703 baris)
├── Ninja-Urban-Farming.md        # Naskah final — buku lengkap (2900+ baris)
├── inject_visuals.py             # Skrip Python untuk inject diagram & gambar
│
├── drafts/                       # Pipeline editorial
│   ├── content/                  # Draft konten per bab (A1 - A5)
│   │   ├── A1-akuakultur.md
│   │   ├── A2-entomologi-peternakan.md
│   │   ├── A3-hortikultura.md
│   │   ├── A4-biokimia-tanah.md
│   │   └── A5-sistem-terintegrasi.md
│   │
│   ├── editorial/                # File proses editorial
│   │   ├── A0-gap-analysis.md    # Analisis gap BluePrint → naskah
│   │   ├── A6-structured-naskah.md  # Naskah hasil developmental editing
│   │   ├── A7-copy-edited.md     # Naskah hasil copy editing
│   │   └── A8-review-report.md   # Technical review report
│   │
│   ├── prompts/                  # Prompt AI untuk setiap tahap
│   │   ├── A0-cartographer.md
│   │   ├── A1-A5 (content prompts)
│   │   ├── A6-developmental-editor.md
│   │   ├── A7-copy-editor.md
│   │   ├── A8-technical-reviewer.md
│   │   ├── A9-layout-designer.md
│   │   └── A10-qa-proofreader.md
│   │
│   └── publishing/               # Output final untuk publishing
│       ├── A9-layout-naskah.md
│       ├── A10-final-naskah.md
│       └── Ninja-Urban-Farming.md
│
└── obsidian/                     # Obsidian vault (knowledge base)
    └── urban_farming/            # Root vault — **kamu di sini sekarang**
        ├── PROJECT-BRIEFING.md   # ← FILE INI
        ├── Welcome.md
        ├── _Templates/
        ├── _Assets/
        ├── .obsidian/
        ├── 0_Inbox/
        ├── 1_Atlas/
        ├── 2_Permanent/
        ├── 3_Literature/
        └── 4_Daily/
```

---

## 3. ALUR KERJA EDITORIAL (PIPELINE A0-A10)

Setiap tahap menghasilkan file baru, tahap berikutnya memakan output tahap sebelumnya:

| Tahap | Nama | Input | Output | Deskripsi |
|-------|------|-------|--------|-----------|
| **A0** | Cartographer | `BluePrint.md` | `A0-gap-analysis.md` | Analisis gap, pemetaan struktur, identifikasi duplikasi |
| **A1-A5** | Content Drafts | `BluePrint.md` per bab | `A1-A5 per bab` | Draft konten mentah per kelompok bab |
| **A6** | Developmental Editor | `A1-A5` | `A6-structured-naskah.md` | Restrukturisasi, ekspansi naratif, penambahan diagram |
| **A7** | Copy Editor | `A6` | `A7-copy-edited.md` | Perbaikan bahasa, konsistensi istilah, tone |
| **A8** | Technical Reviewer | `A7` | `A8-review-report.md` | Validasi teknis, fakta ilmiah, akurasi resep/formula |
| **A9** | Layout Designer | `A8` (approved) | `A9-layout-naskah.md` | Layout, visual, infografis, callout styling |
| **A10** | QA Proofreader | `A9` | `A10-final-naskah.md` | Proofreading final, indeks, glosarium |

**Output final yang dipublikasikan:** `Ninja-Urban-Farming.md` di root (hasil dari A10).

---

## 4. ISI BUKU (26 BAB, 6 BAGIAN)

### Bagian 1: FONDASI — Memulai Sistem
- Bab 2: Perencanaan & Zonasi Lahan (2 zona, variasi 6-100 m²)
- Bab 3: Membangun Infrastruktur Dasar (Raised bed, Kolam Lele Bioflok 3 Galon)
- Bab 4: Setup Maggot BSF (Biopond Auto-Harvest, Kelambu Kawin)
- Bab 5: Setup Ayam Petelur Deep Litter

### Bagian 2: OPERASIONAL — Menjalankan Harian
- Bab 6: Budidaya Lele — Setup, Penebaran, Panen
- Bab 7: Manajemen Pakan Lele — Rumus & Fermentasi
- Bab 8: Pabrik Nutrisi Tanaman — Kompos, Fertigasi, Foliar
- Bab 9: Rotasi Sayuran & Hama Organik
- Bab 10: Jadwal Harian "Ninja" (15 menit/hari)

### Bagian 3: KLINIS — Menangani Masalah
- Bab 11: SOP Klinis Penyakit Lele (Klinis A-H: Amonia, Jamur Saprolegnia, Aeromonas, Kembung Pakan, Blackout/Hipoksia, Broken Head, Jaundice, White Spot)
- Bab 12: SOP Klinis Penyakit Tanaman (Klinis A-F: Fusarium/Layu Bakteri, Antraknosa, Late Blight, Virus Gemini, Damping-off, Karat Putih)

### Bagian 4: LABORATORIUM — Formula Booster
- Bab 13: 4 Formula Booster Tanaman (K-Booster, Aminor-Grow, Cal-Phos Liquid, Mag-Elixir)
- Bab 14: 2 Formula Booster Tanah (Humo-Ninja, JMS-IMO Serum)
- Bab 15: Ekstraksi & Aktivasi Asam Humat Mandiri
- Bab 16: Bio-Multiplikasi EM4 Mandiri
- Bab 17: Nutrisi Generatif (Trik Tomat & Cabai Lebat)
- Bab 18: Ekspansi Bahan Rumah Tangga (10+ formula dapur baru)

### Bagian 5: EKSPANSI — Diversifikasi
- Bab 19-22: Katalog Sayuran, Buah, Ternak Alternatif (Puyuh & Kelinci), Protokol Keamanan

### Bagian 6: STUDI KASUS & REFERENSI
- Bab 23-26: Studi Kasus Multi-Ukuran Lahan, Kalender 12 Bulan, FAQ, Peralatan & Biaya

---

## 5. STRUKTUR VAULT OBSIDIAN (Zettelkasten Method)

Vault ini menggunakan **Zettelkasten Method** — manajemen pengetahuan berbasis catatan atomik yang saling terhubung.

### 5.1 Folder & Fungsinya

| Folder | Fungsi | Kapan Digunakan |
|--------|--------|-----------------|
| **`0_Inbox/`** | Penampungan ide cepat, catatan mentah | Setiap kali ada ide / temuan baru |
| **`1_Atlas/`** | Map of Content (MOC) — pusat navigasi | Saat satu topik sudah punya 5+ catatan |
| **`2_Permanent/`** | Catatan permanen, 1 catatan = 1 konsep | Setelah catatan Inbox diproses & matang |
| **`3_Literature/`** | Catatan dari sumber eksternal (video, buku, jurnal) | Setiap selesai membaca/menonton sumber |
| **`4_Daily/`** | Catatan harian riset (format: `YYYY-MM-DD`) | Setiap hari (opsional) |
| **`_Templates/`** | Template untuk berbagai jenis catatan | Tidak diedit manual |
| **`_Assets/`** | Gambar, PDF, lampiran | Drag & drop file ke Obsidian |

### 5.2 Siklus Kerja Harian

```
📥 TANGKAP        → tulis di 0_Inbox/         (setiap ada ide)
🔄 PROSES (2-3 hr) → pindahkan ke 2_Permanent/ (rapikan + tambahkan link)
🔗 HUBUNGKAN      → tambahkan [[wikilink]]     (setiap menulis)
🗺️ BANGUN MOC     → buat di 1_Atlas/           (setelah 5+ catatan tentang satu topik)
📅 LOG HARIAN     → gunakan 4_Daily/           (setiap hari, opsional)
📊 EKSPLORASI     → buka Graph View            (seminggu sekali, cek catatan yatim)
```

---

## 6. TEMPLATE & KONVENSI PENULISAN

### 6.1 Daftar Template (di `_Templates/`)

#### `tpl-catatan-permanen.md`
```
---
judul: "{{title}}"
tanggal: "{{date}}"
tag:
  - 
status: 🌱
referensi:
  - 
---
# {{title}}
> [!abstract] Ringkasan
> 
## Isi
## Keterkaitan
- 
```

#### `tpl-catatan-literatur.md`
```
---
judul: "{{title}}"
tanggal: "{{date}}"
tag:
  - literatur
sumber: ""
penulis: ""
tahun: 
link: 
status: 🌱
---
# {{title}}
> [!quote] Sumber
> - **Penulis:** 
> - **Sumber:** 
> - **Link:** 
## Poin-Poin Penting
## Ide & Wawasan Pribadi
## Keterkaitan
- 
```

#### `tpl-moc.md`
```
---
judul: "{{title}}"
tanggal: "{{date}}"
tag:
  - moc
---
# {{title}}
> [!tldr] Peta Konten
> Halaman ini menghubungkan berbagai catatan tentang **{{title}}**.
## Subtopik
### 
## Catatan Terkait
### 
```

#### `tpl-catatan-harian.md`
```
---
tanggal: "{{date}}"
tag:
  - harian
---
# {{date}}
## 📝 Catatan Riset
## 🔗 Temuan / Ide Baru
## 📚 Bacaan Hari Ini
## 📅 Rencana Besok
```

### 6.2 Konvensi Markdown Obsidian

| Elemen | Sintaks | Contoh |
|--------|---------|--------|
| **Wikilink** | `[[Nama Catatan]]` | `[[Hidroponik]]` |
| Wikilink + alias | `[[Nama\|teks tampilan]]` | `[[Nutrisi AB Mix\|pupuk hidroponik]]` |
| Wikilink ke heading | `[[Nama#subjudul]]` | `[[Urban Farming#Metode & Sistem]]` |
| Wikilink ke blok | `[[Nama^blok-id]]` | `[[Resep#^k-booster]]` |
| **Embed file** | `![[file.ext]]` | `![[basil_tomato_infographic.png]]` |
| **Callout** | `> [!type]` | `> [!note]`, `> [!abstract]`, `> [!tldr]`, `> [!quote]`, `> [!tip]`, `> [!important]`, `> [!warning]`, `> [!info]` |
| **Tag** | `#tag` | `#hidroponik`, `#kompos`, `#nutrisi` |
| **YAML Frontmatter** | `---` ... `---` | Lihat template di atas |
| **Tabel** | Markdown table | Lihat aturan di bawah |

### 6.3 Aturan Tabel (WAJIB — Paling Sering Salah)

Tabel adalah elemen yang paling rentan rusak di Obsidian. Ikuti checklist ini setiap membuat tabel:

**Checklist Sebelum Commit:**

```
[ ] Ada heading/teks pengantar SEBELUM tabel (tabel tidak boleh muncul tiba-tiba tanpa konteks)
[ ] Ada 1 baris KOSONG antara teks pengantar dan baris header tabel
[ ] Baris alignment (---|---) TIDAK boleh ada spasi di dalamnya
[ ] Jumlah kolom di header = jumlah kolom di alignment = jumlah kolom di semua baris data
[ ] Setiap baris tabel diawali dan diakhiri pipe |
```

**Contoh BENAR:**
```
**Judul Tabel:**

| Kolom A | Kolom B | Kolom C |
|---------|---------|---------|
| Data 1  | Data 2  | Data 3  |
| Data 4  | Data 5  | Data 6  |
```

**Contoh SALAH — alignment pakai spasi:**
```
| Kolom A | Kolom B |
| ------- | ------- |    ← SALAH! Spasi di antara dash bikin Obsidian gagal parse
```

**Contoh SALAH — tidak ada blank line sebelum tabel:**
```
**Judul Tabel:**
| Kolom A | Kolom B |    ← SALAH! Butuh 1 baris kosong di atasnya
|---------|---------|
```

**Pola yang selalu benar:**
```
[heading atau teks pengantar]

| Header1 | Header2 | Header3 |
|---------|---------|---------|
| Isi     | Isi     | Isi     |
```

> [!tip] Cara Cek Cepat
> Di Obsidian, buka **Reading View** (`Cmd+E`). Jika tabel muncul sebagai teks biasa (bukan grid tabel), berarti formatnya salah. Edit dan perbaiki.

### 6.4 Aturan Penting

1. **Satu catatan = satu konsep** — Jangan gabung banyak ide dalam satu catatan permanen
2. **Selalu tambahkan wikilink** — Setiap catatan wajib punya minimal 1 wikilink di bagian Keterkaitan
3. **Gunakan status emoji** — `🌱` (seedling/belum matang) → `🌿` (growing/matang) → `🌳` (evergreen/sangat matang)
4. **File baru selalu di `0_Inbox/`** — Jangan langsung buat di `2_Permanent/`
5. **Judul file = judul catatan** — Gunakan huruf kapital di awal kata, hindari karakter khusus
6. **Gambar/aset di `_Assets/`** — Jangan simpan gambar di folder konten
7. **Frontmatter YAML wajib di SEMUA catatan** — Minimal `judul`, `tanggal`, `tag`
8. **Sebelum commit, buka Reading View (`Cmd+E`)** — Pastikan semua tabel, callout, dan wikilink ter-render dengan benar

---

## 7. KONFIGURASI OBSIDIAN (`.obsidian/`)

### 7.1 `app.json`
- **Template folder:** `_Templates/`
- **New file location:** `0_Inbox/` — semua file baru otomatis masuk Inbox
- **Attachment folder:** `_Assets/` — semua gambar/lampiran otomatis ke sini
- **Auto-update links:** ON — saat rename file, semua wikilink diperbarui otomatis
- **Inline title:** ON — judul dari frontmatter ditampilkan inline

### 7.2 `daily-notes.json`
- **Folder:** `4_Daily/`
- **Template:** `_Templates/tpl-catatan-harian.md`
- **Format:** `YYYY-MM-DD`

### 7.3 `templates.json`
- **Folder:** `_Templates/` — lokasi template untuk `Ctrl+T`

---

## 8. STATUS PROYEK SAAT INI

### 8.1 Buku (Naskah)
- ✅ **BluePrint.md** — Selesai (703 baris, seluruh konten teknis mentah lengkap)
- ✅ **Pipeline Editorial A0-A10** — Selesai
- ✅ **Ninja-Urban-Farming.md** — Naskah final (2900+ baris, 26 bab + glosarium + cheat sheet)
- ✅ **inject_visuals.py** — Sudah dijalankan, diagram Mermaid & gambar sudah di-inject

### 8.2 Obsidian Vault
- ✅ **Struktur & Template** — Selesai, siap pakai
- ✅ **MOC Utama** — `1_Atlas/Urban Farming.md` (147 baris, memetakan 60+ topik)
- ⚠️ **0_Inbox/** — 11 catatan, sebagian besar masih kosong (placeholder)
- ⚠️ **2_Permanent/** — Baru 3 catatan (hidroponik basics)
- ⚠️ **3_Literature/** — 11 catatan tentang tomat & kompos (dari sumber YouTube)
- ❌ **4_Daily/** — Kosong

### 8.3 Yang Perlu Dikerjakan
1. **Mengisi vault** — Memindahkan pengetahuan dari `BluePrint.md` dan `Ninja-Urban-Farming.md` ke dalam catatan Zettelkasten yang saling terhubung
2. **Membangun MOC per topik** — Setelah 5+ catatan per topik, buat MOC di `1_Atlas/`
3. **Mengisi Inbox yang kosong** — Proses 11 catatan Inbox yang masih placeholder
4. **Mencatat literatur baru** — Setiap temuan baru dari YouTube/jurnal ke `3_Literature/`
5. **Daily notes** — Mulai logging riset harian di `4_Daily/`

---

## 9. INSTRUKSI UNTUK AI BARU

### 9.1 Cara Membaca Proyek Ini

1. **Baca file ini dulu** (kamu sedang melakukannya) — pahami seluruh konteks
2. **Buka `Ninja-Urban-Farming.md`** — ini adalah naskah final, sumber kebenaran konten
3. **Buka `1_Atlas/Urban Farming.md`** — pahami peta topik MOC utama
4. **Jelajahi `2_Permanent/`** — lihat contoh catatan permanen yang sudah ada
5. **Jelajahi `3_Literature/`** — lihat contoh catatan literatur

### 9.2 Cara Bekerja di Vault Ini

**Saat menulis catatan baru:**
1. Buat file di `0_Inbox/` dulu (atau gunakan `Ctrl+N`)
2. Gunakan template yang sesuai (`Ctrl+T` → pilih template)
3. Isi metadata frontmatter lengkap
4. Tulis konten dengan format Obsidian yang benar (wikilink, callout, tag)
5. Selalu tambahkan `[[wikilink]]` ke catatan terkait di bagian **Keterkaitan**
6. Setelah matang, pindahkan ke `2_Permanent/` atau `3_Literature/`

**Saat menghubungkan catatan:**
1. Cek catatan yang sudah ada di `2_Permanent/` — jangan buat duplikat
2. Gunakan `[[wikilink]]` untuk menghubungkan
3. Cek panel **Backlink** Obsidian untuk melihat koneksi yang terbentuk
4. Gunakan **Graph View** (`Ctrl+G`) untuk melihat catatan yatim (belum terhubung)

**Saat membuat MOC:**
1. Gunakan template `tpl-moc`
2. Simpan di `1_Atlas/`
3. Pastikan ada minimal 5+ catatan anak untuk satu MOC
4. Update MOC utama (`Urban Farming.md`) jika menambah topik besar baru

### 9.3 Struktur Callout yang Dianjurkan

| Callout | Gunakan Untuk |
|---------|--------------|
| `> [!abstract]` | Ringkasan di awal catatan permanen |
| `> [!tldr]` | Deskripsi singkat MOC |
| `> [!quote]` | Kutipan sumber literatur |
| `> [!note]` | Informasi tambahan, catatan kaki |
| `> [!tip]` | Trik Ninja, tips praktis |
| `> [!important]` | Hal kritis yang wajib diperhatikan |
| `> [!warning]` | Peringatan risiko |
| `> [!info]` | Konteks atau definisi |

### 9.4 Tag yang Sudah Dipakai

| Tag | Kategori |
|-----|----------|
| `#moc` | Map of Content |
| `#hidroponik` | Hidroponik |
| `#nutrisi` | Nutrisi tanaman |
| `#kompos` | Kompos & pengomposan |
| `#urban-farming` | Pertanian perkotaan umum |
| `#panduan` | Panduan / tutorial |
| `#parameter` | Parameter / metrik |
| `#harian` | Daily notes |
| `#literatur` | Catatan literatur |
| `#briefing` | Meta project briefing |
| `#project` | Meta proyek |

### 9.5 Path Penting (Absolute)

| Deskripsi | Path |
|-----------|------|
| Root proyek | `/Users/satyaadidharma/Urban Farming/` |
| Naskah final | `/Users/satyaadidharma/Urban Farming/Ninja-Urban-Farming.md` |
| Blueprint raw | `/Users/satyaadidharma/Urban Farming/BluePrint.md` |
| Root vault | `/Users/satyaadidharma/Urban Farming/obsidian/urban_farming/` |
| MOC utama | `/Users/satyaadidharma/Urban Farming/obsidian/urban_farming/1_Atlas/Urban Farming.md` |
| Template | `/Users/satyaadidharma/Urban Farming/obsidian/urban_farming/_Templates/` |
| Aset | `/Users/satyaadidharma/Urban Farming/obsidian/urban_farming/_Assets/` |

---

## 10. PANDUAN CEPAT — APA YANG HARUS AI LAKUKAN

> [!info] Saat user memberi perintah, AI harus:
> 1. **Cek vault dulu** — Apakah catatan terkait sudah ada? Gunakan wikilink `[[nama]]` jika sudah ada.
> 2. **Gunakan template** — Jika membuat catatan baru, ikuti struktur template yang sesuai.
> 3. **Gunakan format Obsidian** — Semua catatan HARUS menggunakan format yang kompatibel dengan Obsidian (wikilink, callout, tag, frontmatter YAML).
> 4. **Hubungkan** — Setiap catatan baru HARUS punya minimal 1 wikilink ke catatan yang sudah ada.
> 5. **Jangan buat duplikat** — Periksa apakah topik sudah ada di vault sebelum membuat catatan baru.
> 6. **Simpan di folder yang benar** — Inbox untuk draft, Permanent untuk catatan matang, Literature untuk sumber eksternal, Atlas untuk MOC.
> 7. **Update MOC** — Jika menambah catatan baru dalam suatu topik, pertimbangkan untuk mengupdate MOC yang relevan.
> 8. ⚠️ **TABEL: Ikuti checklist Section 6.3** — heading pengantar → blank line → header → alignment row TANPA spasi → data. Reading View (`Cmd+E`) harus dicek sebelum selesai.

---

> [!note] Last Updated
> 2026-06-26 — Satya Adidharma
> 
> File ini adalah dokumen hidup. Update bagian **Status Proyek Saat Ini** (Section 8) secara berkala saat progres signifikan tercapai.
