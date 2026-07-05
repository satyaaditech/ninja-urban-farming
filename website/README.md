# 🥷 Ninja Urban Farming — Website

Website statis untuk proyek **Ninja Urban Farming**, dibuat dengan [Astro](https://astro.build) v7 dan dioptimalkan untuk deployment ke **GitHub Pages**.

## 🚀 Menjalankan Secara Lokal

### Prasyarat

- Node.js 18+ (terinstall: v22.21.0)
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

## 📁 Struktur Folder

```
website/
├── public/              # Aset statis (gambar, favicon)
│   └── images/          # Semua gambar website
├── src/
│   ├── components/      # Komponen reusable
│   │   ├── Navigation.astro
│   │   ├── Footer.astro
│   │   └── ImagePlaceholder.astro
│   ├── layouts/         # Layout halaman
│   │   └── Layout.astro
│   ├── content/         # Konten Markdown (content collections)
│   │   ├── sop/         # SOP budidaya
│   │   ├── formulas/    # Formula & resep
│   │   └── guides/      # Panduan umum
│   ├── pages/           # Halaman website
│   │   ├── index.astro
│   │   ├── tentang.astro
│   │   ├── sop/
│   │   │   ├── index.astro
│   │   │   └── [slug].astro
│   │   ├── katalog/
│   │   │   └── index.astro
│   │   └── klinis/
│   │       └── index.astro
│   └── content.config.ts  # Definisi content collections (Astro v7)
├── public/images/       # Tempat gambar nanti
├── astro.config.mjs     # Konfigurasi Astro + GitHub Pages
├── package.json
└── README.md
```

## 🔗 Deploy ke GitHub Pages

### Langkah 1: Buat Repository GitHub

1. Buka GitHub → New Repository
2. Nama repository: `ninja-urban-farming` (atau nama lain)
3. Jangan inisialisasi README (sudah ada di lokal)

### Langkah 2: Update `astro.config.mjs`

Ganti `base` dengan nama repository-mu:

```js
export default defineConfig({
  site: 'https://USERNAME.github.io',
  base: '/ninja-urban-farming',
  // ...
});
```

### Langkah 3: Push ke GitHub

```bash
cd website
git init
git add .
git commit -m "Initial commit: Ninja Urban Farming website"
git branch -M main
git remote add origin https://github.com/USERNAME/ninja-urban-farming.git
git push -u origin main
```

### Langkah 4: Aktifkan GitHub Pages

1. Buka repository di GitHub
2. Settings → Pages
3. Source: GitHub Actions
4. Gunakan workflow Astro bawaan (akan otomatis terdeteksi)

Atau deploy manual dari branch `gh-pages`.

## 🖼️ Placeholder Gambar

Semua gambar saat ini menggunakan komponen `ImagePlaceholder.astro`. Setiap placeholder memiliki keterangan lengkap tentang:
- Subjek gambar
- Sudut pandang
- Elemen visual yang harus ada
- Warna dominan
- Gaya ilustrasi
- Bahasa teks

Saat fine-tuning nanti, ganti placeholder dengan gambar nyata di folder `public/images/`.

## 📊 Integrasi Google Sheets

Bagian **Katalog Resep** akan dihubungkan dengan Google Sheets untuk fitur:
- Pencarian resep
- Filter kategori
- Konversi dosis
- Tampilan praktis

Cara setup:
1. Buat Google Sheets baru
2. Publish to web (File → Share → Publish to web)
3. Copy URL CSV
4. Update konfigurasi di `src/pages/katalog/index.astro`

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
2. Gunakan frontmatter sesuai schema di `src/content/config.ts`

## ⚙️ Konfigurasi Penting

Jika nama repository GitHub-mu berbeda, ubah di `astro.config.mjs`:

```js
base: '/nama-repository-mu'
```

Jika deploy ke domain custom, ubah:

```js
site: 'https://www.domainkamu.com',
base: '/', // atau kosongkan
```

## 🛠️ Teknologi

- [Astro](https://astro.build) — Static site generator
- [MDX](https://mdxjs.com) — Markdown dengan komponen
- [GitHub Pages](https://pages.github.com) — Hosting gratis
- [Google Sheets](https://sheets.google.com) — Database gratis untuk katalog

## 📄 Lisensi

Proyek ini untuk dokumentasi edukasi urban farming.
