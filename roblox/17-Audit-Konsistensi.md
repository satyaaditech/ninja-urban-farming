# 17 — LAPORAN AUDIT KONSISTENSI: Cross-Document Consistency Audit

*Audit oleh Senior Game Developer — membandingkan semua 16 dokumen.*

---

## Ringkasan

| Kategori | Jumlah Temuan | Status Perbaikan |
|----------|--------------|-----------------|
| 🔴 KRITIS — Naming inconsistency (will cause compile errors) | 3 | ✅ Diperbaiki |
| 🟠 TINGGI — Missing references in architecture doc | 4 | ✅ Diperbaiki |
| 🟡 SEDANG — Wrong labels/numbers | 2 | ✅ Diperbaiki |
| 🟢 RENDAH — Minor clarity issues | 1 | ✅ Diperbaiki |
| **TOTAL** | **10** | **✅ 10/10 SELESAI** |

---

## 🔴 KRITIS: Naming Inconsistency

RemoteEvent names berbeda antara `03-Spesifikasi-Teknis-Roblox.md` (dokumen arsitektur original) dan `12-Data-Schema-API.md` (kontrak API otoritatif) + `13-Coding-Standards.md`.

| # | Nama di 03 (SALAH) | Nama di 12 & 13 (BENAR) | Dampak jika tidak diperbaiki |
|---|---------------------|------------------------|------------------------------|
| 1 | `DiagnoseCase` | `SubmitDiagnosis` | Client akan fire event yang tidak dilisten server → diagnosis tidak berfungsi |
| 2 | `ConfigureSetup` | `ConfigurePlacement` | Player tidak bisa atur tata letak farm |
| 3 | `SetTimeSpeed` | `SetTimeScale` | Time acceleration tidak berfungsi |

**Akar Masalah:** `03` ditulis pertama sebagai arsitektur awal. `12` ditulis kemudian sebagai kontrak API final dengan nama yang lebih deskriptif. `03` tidak pernah disinkronkan ulang.

---

## 🟠 TINGGI: Missing References in 03

`03-Spesifikasi-Teknis-Roblox.md` tidak mencantumkan fitur yang ditambahkan di dokumen lain:

| # | Yang Hilang di 03 | Ada di Dokumen | Dampak |
|---|-------------------|---------------|--------|
| 4 | RemoteEvents tidak lengkap: `RequestTimeSkip`, `CatchupNotification`, `MentorDialogue`, `LoopHealthUpdate` | 12 Section 2.2, 13 Section 4 | Developer membaca 03 akan melewatkan event-event ini |
| 5 | `DeficiencyEngine.lua` tidak ada di folder `RaisedBed/` | 13 Section 11, 08 Section 10.15 | Defisiensi tanaman tidak akan ada yang handle di server |
| 6 | `OfflineProgression.lua` tidak ada di `SimulationEngine/` | 13 Section 11, 03 Section 5.3 (kode tapi tidak di hierarchy) | Offline progression tidak terintegrasi |
| 7 | `ServerCore/` folder tidak ada di hierarchy 03 | 13 Section 11 | DataStoreManager, RemoteHandler, AntiCheat, ErrorLogger tidak punya tempat |

---

## 🟡 SEDANG: Wrong Labels / Numbers

| # | Lokasi | Masalah | Perbaikan |
|---|--------|---------|-----------|
| 8 | `02-Sistem-Mekanik.md` line 415 | Header: "Berdasarkan matriks klinis tanaman buku **(A–F)**:" — tapi tabel berisi A sampai **G** (7 penyakit) | Ubah ke **(A–G)** |
| 9 | `06-Roadmap-Development.md` K3 & K4 vs `01-Master-Plan.md` | 06 menyebut ekspansi pasca-peluncuran "Farm-to-Table" dan "Tantangan Iklim", tapi 01 Section 8.2 menyebut "Stroberi Vertikultur, Pepaya California, Budikdamber, Hidroponik Sederhana". Keduanya adalah rencana yang berbeda — perlu diklarifikasi mana yang dimaksud. | Ekspansi di 01 adalah untuk **in-game expansion packs (DLC)**. Ekspansi di 06 K3/K4 adalah **konten pasca-peluncuran gratis**. Tambah klarifikasi. |

---

## 🟢 RENDAH: Minor Clarity

| # | Lokasi | Masalah | Perbaikan |
|---|--------|---------|-----------|
| 10 | `03` Section 3.1 | `DiseaseEngine.lua` di `LeleBioflok/` tapi tidak ada `DeficiencyEngine.lua` di `RaisedBed/`. 13 sudah menambahkannya. | Tambahkan `DeficiencyEngine.lua` ke hierarchy 03 |

---

## ✅ YANG SUDAH KONSISTEN (Diverifikasi)

| Aspek | Hasil |
|--------|------|
| Jumlah subsistem (8) | ✅ Konsisten di 01, 02, 03 |
| 8 penyakit ikan (A–H) | ✅ Konsisten di 02, 07, 14 |
| 11 spesies tanaman | ✅ Konsisten di 08, 11 |
| 3 hewan (Lele, BSF, Ayam) | ✅ Konsisten di 01, 02, 08 |
| Parameter kimia air (pH, DO, NH3, dll.) | ✅ Nilai threshold konsisten di 02, 09, 14 |
| Formula ABW & pakan | ✅ Identik di 02, 07, 14 |
| DataStore `saveVersion` & `MIGRATIONS` | ✅ Konsisten di 12, 15, 16 |
| Nama pengobatan organik | ✅ Konsisten di 02, 08, 09 |
| ModuleScript naming (`PascalCase.lua`) | ✅ Konsisten di 03, 13 |
| Struktur folder utama | ✅ Konsisten di 03, 13 |
| State structures (WaterState, SoilState, PlantData, dll.) | ✅ Nama field identik di 02, 12 |
| `--!strict` requirement | ✅ Konsisten di 13, 14 |
| Offline progression rules | ✅ Konsisten di 03 (kode), 07, 12 |
| PR checklist | ✅ Konsisten di 13, 14 |
| Time system (1 game day = 15 real min) | ✅ Konsisten di 01, 07 |
| Tidak ada referensi Puyuh/Kelinci | ✅ Diverifikasi — 0 matches di semua dokumen |

---

## Rencana Perbaikan

Semua 10 temuan akan diperbaiki dengan urutan prioritas:

1. **Perbaiki 03** — sinkronkan RemoteEvent names + hierarchy lengkap (temuan #1–7, #10)
2. **Perbaiki 02** — ubah header "A–F" → "A–G" (temuan #8)
3. **Perbaiki 06** — klarifikasi ekspansi DLC vs konten pasca-peluncuran (temuan #9)

---

*Audit selesai. Perbaikan dimulai.*
