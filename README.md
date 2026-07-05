# 🥷 Ninja Urban Farming

Repositori utama proyek **Ninja Urban Farming** — panduan komprehensif berbahasa Indonesia tentang pertanian perkotaan organik dalam sistem closed-loop.

Repo ini berisi:
- Manuscript buku utama
- Draft konten dan pipeline editorial
- Obsidian vault untuk knowledge management
- Website statis yang dideploy ke GitHub Pages

---

## 🌐 Website

Website proyek ini dibangun dengan [Astro](https://astro.build) v7 dan di-deploy otomatis ke **GitHub Pages**.

**URL:** [https://satyaadiditech.github.io/ninja-urban-farming](https://satyaadiditech.github.io/ninja-urban-farming)

### Menjalankan Website Secara Lokal

```bash
cd website
npm install
npm run dev
```

Buka browser di: `http://localhost:4321/ninja-urban-farming/`

### Build Production

```bash
cd website
npm run build
```

Hasil build ada di `website/dist/`.

---

## 📁 Struktur Repository

```
/
├── Ninja-Urban-Farming.md      # Manuscript utama buku (source of truth)
├── BluePrint.md                # Ringkasan/outline buku
├── inject_visuals.py           # Script untuk inject diagram dan gambar ke manuscript
├── AGENTS.md                   # Panduan untuk AI coding agents
├── README.md                   # File ini
│
├── drafts/                     # Pipeline editorial dan draft konten
│   ├── content/                # Draft konten per domain
│   ├── editorial/              # Pipeline editorial (gap analysis, review, dll)
│   ├── prompts/                # Template prompt untuk setiap tahap editorial
│   └── publishing/             # Output final sebelum publish
│
├── obsidian/urban_farming/     # Obsidian vault untuk catatan dan knowledge management
│
├── roblox/                     # Direktori cadangan untuk konten game terkait
│
└── website/                    # Source code website Astro
    ├── .github/workflows/      # GitHub Actions untuk auto-deploy
    ├── public/                 # Aset statis
    ├── src/
    │   ├── components/         # Komponen reusable
    │   ├── layouts/            # Layout halaman
    │   ├── content/            # Konten Markdown (content collections)
    │   │   ├── sop/            # SOP budidaya
    │   │   ├── formulas/       # Katalog resep formula
    │   │   ├── klinis-tanaman/ # Penyakit tanaman
    │   │   └── klinis-lele/    # Penyakit ikan lele
    │   ├── pages/              # Halaman website
    │   └── content.config.ts   # Skema content collections Astro v7
    ├── astro.config.mjs        # Konfigurasi Astro + GitHub Pages
    └── package.json
```

---

## 🌱 Konten Website

Website saat ini mencakup:

- **Beranda** — pengenalan sistem Ninja Urban Farming
- **SOP Budidaya** — panduan operasional tanaman (kangkung, tomat, selada, sawi, bayam, daun bawang, seledri)
- **Katalog Resep** — 53+ formula organik untuk pupuk, pestisida, fungisida, media tanam, pakan, dll.
- **Klinis Tanaman** — diagnosa dan penanganan penyakit/hama tanaman
- **Klinis Lele** — 8 penyakit umum pada budidaya lele bioflok
- **Tentang** — penjelasan sistem closed-loop

---

## 📝 Manuscript & Editorial Pipeline

Alur kerja konten:

```
drafts/content/ → drafts/editorial/ → drafts/publishing/ → Ninja-Urban-Farming.md
```

Untuk menambah atau mengganti diagram/gambar di manuscript, edit placeholder sesuai sintaks di `AGENTS.md`, lalu jalankan:

```bash
python inject_visuals.py
```

---

## 🚀 Auto-Deploy ke GitHub Pages

Setiap kali ada push ke branch `master`, GitHub Actions akan otomatis:

1. Install dependency dengan Node.js 22
2. Build website Astro
3. Deploy hasil build ke GitHub Pages

Status deployment bisa dicek di tab **Actions**:
[https://github.com/satyaaditech/ninja-urban-farming/actions](https://github.com/satyaaditech/ninja-urban-farming/actions)

---

## 🛠️ Teknologi

- [Astro](https://astro.build) v7 — framework web statis
- [GitHub Pages](https://pages.github.com) — hosting gratis
- [GitHub Actions](https://github.com/features/actions) — CI/CD untuk auto-deploy
- Markdown — untuk semua konten
- Obsidian — untuk knowledge management

---

## 📄 Lisensi

Proyek ini adalah proyek pribadi. Semua konten dalam Bahasa Indonesia.

---

## 💡 Catatan Penting

- Semua konten website ada di folder `website/src/content/` sebagai file Markdown.
- Jika ingin menambah SOP, formula, atau data klinis baru, cukup tambahkan file Markdown di folder content yang sesuai.
- Untuk backup seluruh project, cukup push repo ini ke GitHub.
