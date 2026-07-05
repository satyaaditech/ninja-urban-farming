# 🥷 Ninja Urban Farming

Repositori utama proyek **Ninja Urban Farming** — panduan komprehensif berbahasa Indonesia tentang pertanian perkotaan organik dalam sistem closed-loop.

🟢 **Website sudah online dan aktif di:** [https://satyaadiditech.github.io/ninja-urban-farming/](https://satyaadiditech.github.io/ninja-urban-farming/)

Repo ini berisi:
- Manuscript buku utama
- Draft konten dan pipeline editorial
- Obsidian vault untuk knowledge management
- Website statis yang dideploy otomatis ke GitHub Pages

---

## 🌐 Website

Website proyek ini dibangun dengan [Astro](https://astro.build) v7 dan di-deploy otomatis ke **GitHub Pages** melalui **GitHub Actions**.

**URL aktif:** [https://satyaadiditech.github.io/ninja-urban-farming/](https://satyaadiditech.github.io/ninja-urban-farming/)

**Status deployment:** [Lihat di GitHub Actions](https://github.com/satyaaditech/ninja-urban-farming/actions)

### Menjalankan Website Secara Lokal

Prasyarat: Node.js **>=22.12.0** (Astro v7 membutuhkan Node.js 22+)

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
    ├── .github/workflows/      # GitHub Actions untuk auto-deploy ke GitHub Pages
    ├── public/                 # Aset statis
    │   └── data/               # Data CSV dan file publik lainnya
    ├── src/
    │   ├── components/         # Komponen reusable
    │   │   ├── Navigation.astro
    │   │   ├── Footer.astro
    │   │   └── ImagePlaceholder.astro
    │   ├── layouts/            # Layout halaman
    │   │   └── Layout.astro
    │   ├── content/            # Konten Markdown (content collections)
    │   │   ├── sop/            # SOP budidaya
    │   │   ├── formulas/       # Katalog resep formula
    │   │   ├── klinis-tanaman/ # Penyakit tanaman
    │   │   └── klinis-lele/    # Penyakit ikan lele
    │   ├── data/               # Data JSON untuk katalog
    │   ├── pages/              # Halaman website
    │   └── content.config.ts   # Skema content collections Astro v7
    ├── astro.config.mjs        # Konfigurasi Astro + GitHub Pages
    └── package.json
```

---

## 🌱 Konten Website

Website saat ini mencakup:

- **Beranda** — pengenalan sistem Ninja Urban Farming
- **SOP Budidaya** — 7 panduan operasional tanaman (kangkung, tomat, selada, sawi, bayam, daun bawang, seledri)
- **Katalog Resep** — 53+ formula organik untuk pupuk, pestisida, fungisida, media tanam, pakan, dll.
- **Klinis Tanaman** — 6 penyakit/hama umum pada tanaman
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
- Website akan otomatis rebuild dan redeploy setiap kali ada push ke branch `master`.
- Untuk backup seluruh project, cukup push repo ini ke GitHub.
