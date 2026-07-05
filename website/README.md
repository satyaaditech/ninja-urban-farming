# 🥷 Ninja Urban Farming — Website

Website statis untuk proyek **Ninja Urban Farming**, dibuat dengan [Astro](https://astro.build) v7 dan dioptimalkan untuk deployment ke **GitHub Pages**.

🟢 **Website sudah online di:** [https://satyaadiditech.github.io/ninja-urban-farming/](https://satyaadiditech.github.io/ninja-urban-farming/)

---

## 🚀 Menjalankan Secara Lokal

### Prasyarat

- Node.js **>=22.12.0** (Astro v7 membutuhkan Node.js 22+)
- npm atau yarn

### Langkah 1: Install Dependensi

```bash
cd website
npm install
```

### Langkah 2: Jalankan Server Development

```bash
npm run dev
```

Buka browser di: `http://localhost:4321/ninja-urban-farming/`

### Langkah 3: Build untuk Production

```bash
npm run build
```

Hasil build ada di folder `dist/`.

### Langkah 4: Preview Build Lokal

```bash
npm run preview
```

---

## 📁 Struktur Folder

```
website/
├── .github/workflows/      # GitHub Actions untuk auto-deploy
├── public/                 # Aset statis
│   ├── data/               # Data publik (CSV, dll)
│   └── favicon.svg
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
│   │   ├── index.astro
│   │   ├── tentang.astro
│   │   ├── sop/
│   │   │   ├── index.astro
│   │   │   └── [slug].astro
│   │   ├── katalog/
│   │   │   ├── index.astro
│   │   │   └── [slug].astro
│   │   └── klinis/
│   │       ├── index.astro
│   │       ├── tanaman/
│   │       │   ├── index.astro
│   │       │   └── [slug].astro
│   │       └── lele/
│   │           ├── index.astro
│   │           └── [slug].astro
│   └── content.config.ts   # Definisi content collections (Astro v7)
├── astro.config.mjs        # Konfigurasi Astro + GitHub Pages
├── package.json
└── README.md
```

---

## 🔗 Deploy ke GitHub Pages

Deploy dilakukan otomatis oleh GitHub Actions setiap kali ada push ke branch `master`.

### Konfigurasi Saat Ini

File `.github/workflows/deploy.yml` sudah terkonfigurasi untuk:
- Build project dari folder `website/`
- Deploy hasil build ke GitHub Pages

Konfigurasi Astro ada di `astro.config.mjs`:

```js
export default defineConfig({
  site: 'https://satyaadiditech.github.io',
  base: '/ninja-urban-farming',
  // ...
});
```

### Status Deployment

Cek status terbaru di tab Actions:
[https://github.com/satyaaditech/ninja-urban-farming/actions](https://github.com/satyaaditech/ninja-urban-farming/actions)

---

## 🖼️ Placeholder Gambar

Semua gambar saat ini menggunakan komponen `ImagePlaceholder.astro`. Setiap placeholder memiliki keterangan lengkap tentang:
- Subjek gambar
- Sudut pandang
- Elemen visual yang harus ada
- Warna dominan
- Gaya ilustrasi
- Bahasa teks

Saat fine-tuning nanti, ganti placeholder dengan gambar nyata di folder `public/images/`.

---

## 📝 Menambah Konten Baru

### Menambah SOP Baru

1. Buat file `.md` di `src/content/sop/`
2. Gunakan frontmatter:

```yaml
---
title: "Judul SOP"
description: "Deskripsi singkat"
pubDate: 2026-07-05
category: "SOP"
tags: ["tag1", "tag2"]
---
```

3. Tulis konten dalam Markdown
4. Halaman detail otomatis dibuat di `/sop/nama-file`

### Menambah Formula Baru

1. Buat file `.md` di `src/content/formulas/`
2. Gunakan frontmatter sesuai schema di `src/content.config.ts`

### Menambah Data Klinis

1. Untuk tanaman: buat file `.md` di `src/content/klinis-tanaman/`
2. Untuk lele: buat file `.md` di `src/content/klinis-lele/`
3. Gunakan frontmatter sesuai schema masing-masing

---

## ⚙️ Konfigurasi Penting

Jika nama repository GitHub berubah, ubah di `astro.config.mjs`:

```js
base: '/nama-repository-mu'
```

Jika deploy ke domain custom, ubah:

```js
site: 'https://www.domainkamu.com',
base: '/', // atau kosongkan
```

---

## 🛠️ Teknologi

- [Astro](https://astro.build) v7 — Static site generator
- [MDX](https://mdxjs.com) — Markdown dengan komponen
- [GitHub Pages](https://pages.github.com) — Hosting gratis
- [GitHub Actions](https://github.com/features/actions) — CI/CD untuk auto-deploy

---

## 📄 Lisensi

Proyek ini untuk dokumentasi edukasi urban farming.
