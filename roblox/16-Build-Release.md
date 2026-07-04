# 16 — BUILD & RELEASE PIPELINE

> **Target:** Solo developer. Pipeline ini dirancang sederhana — tidak perlu Jenkins atau infrastruktur kompleks. Cukup Roblox Studio + Rojo + GitHub.

---

## 1. Environments

| Environment | Tujuan | Siapa yang Akses | Update Frekuensi |
|------------|--------|-----------------|-----------------|
| **Dev (Local)** | Development harian di Roblox Studio | Developer (kamu) | Continuous (setiap save) |
| **Staging (Test Place)** | Testing sebelum rilis — Roblox place terpisah | Developer + trusted testers | Setiap milestone fase |
| **Production (Live)** | Game publik di Roblox | Semua pemain | Setelah QA pass di staging |

**Setup di Roblox Studio:**
- `NinjaUrbanFarming_Dev.rbxl` — local file, tidak dipublish
- `NinjaUrbanFarming_Staging.rbxl` — publish ke place ID khusus (private)
- `NinjaUrbanFarming_Production.rbxl` — publish ke place ID publik

---

## 2. Versioning Scheme

Format: `v{major}.{minor}.{patch}-{stage}`

| Version | Arti | Contoh |
|---------|------|--------|
| `v0.1.0-alpha` | Fase 0 (Foundation), milestone 1 | Setup proyek selesai |
| `v0.2.0-alpha` | Fase 0, milestone 2 | TimeManager + DataStore selesai |
| `v1.0.0-alpha` | Fase 1 (Lele MVP) selesai | Lele simulator functional |
| `v1.0.0-beta` | Fase 1 di staging, siap testing | Internal testing dimulai |
| `v1.0.0` | Fase 1 live di production | Public release Lele Simulator |
| `v1.0.1` | Hotfix untuk Fase 1 | Bug fix minor |
| `v5.0.0` | Fase 5 selesai | Full game live |

**Setiap fase naik major version. Setiap milestone dalam fase naik minor.**

---

## 3. Rojo Configuration

Rojo digunakan untuk sync file filesystem ke Roblox Studio. Ini memungkinkan version control (Git) untuk file Luau.

### 3.1 `default.project.json`

```json
{
    "name": "NinjaUrbanFarming",
    "tree": {
        "$className": "DataModel",
        "ReplicatedStorage": {
            "$className": "ReplicatedStorage",
            "$path": "src/ReplicatedStorage"
        },
        "ServerScriptService": {
            "$className": "ServerScriptService",
            "$path": "src/ServerScriptService"
        },
        "StarterPlayer": {
            "$className": "StarterPlayer",
            "StarterPlayerScripts": {
                "$className": "StarterPlayerScripts",
                "$path": "src/StarterPlayer/StarterPlayerScripts"
            }
        },
        "StarterGui": {
            "$className": "StarterGui",
            "$path": "src/StarterGui"
        }
    }
}
```

### 3.2 Struktur Folder `src/`

```
src/
├── ReplicatedStorage/
│   ├── Remotes/               # RemoteEvent & RemoteFunction instances
│   └── Shared/                # Types, Constants, Formulas
├── ServerScriptService/
│   ├── SimulationEngine/      # Semua logic simulasi (lihat 13-Coding-Standards)
│   ├── ServerCore/            # DataStore, RemoteHandler, AntiCheat
│   └── Tests/                 # Unit tests
├── StarterPlayer/
│   └── StarterPlayerScripts/  # Client-side scripts
└── StarterGui/                # Semua UI
```

### 3.3 Workflow Harian

```bash
# 1. Edit kode di filesystem (VS Code / editor apapun)
# 2. Buka Roblox Studio
# 3. Rojo sync
rojo serve

# 4. Di Roblox Studio: Rojo plugin → Connect
# 5. Test di Studio
# 6. Commit perubahan
git add .
git commit -m "feat(lele): implement water chemistry tick"
git push
```

---

## 4. Git Workflow

### 4.1 Branch Strategy (Sederhana untuk Solo Dev)

```
main          ← stabil, bisa dipublish kapan saja
  └── dev     ← development aktif
       └── feat/lele-bioflok    ← feature branch
       └── feat/raised-bed
       └── fix/clinical-bug
       └── chore/refactor
```

**Aturan:**
- `main` hanya di-update dari `dev` via merge (bukan commit langsung)
- `dev` adalah branch kerja harian
- Feature branch untuk fitur besar (>50 baris kode baru)
- Fix branch untuk bug fix

### 4.2 Commit Convention

Format: `type(scope): description`

| Type | Kapan |
|------|-------|
| `feat` | Fitur baru |
| `fix` | Bug fix |
| `refactor` | Perbaikan kode tanpa ubah behavior |
| `chore` | Maintenance (update deps, config) |
| `docs` | Dokumentasi |
| `test` | Tambah/perbaiki test |
| `perf` | Performance improvement |

**Contoh:**
```
feat(lele): implement ABW growth formula
fix(lele): correct ammonia calculation when DO < 2.0
refactor(soil): extract nutrient calculation to shared module
chore: update Rojo config for new folder structure
docs: add coding standards for naming conventions
```

### 4.3 `.gitignore`

```gitignore
# Roblox Studio artifacts
*.rbxl
*.rbxlx

# OS files
.DS_Store
Thumbs.db

# Dependencies
node_modules/
Packages/

# Build output
build/
out/

# Rojo
.rojo/
```

---

## 5. Release Process

### 5.1 Pre-Release Checklist

- [ ] Semua unit test pass
- [ ] Smoke test checklist selesai (lihat `14-Testing-QA-Plan.md` Section 7)
- [ ] Tidak ada error di console (F9)
- [ ] DataStore save/load berfungsi (test dengan relog)
- [ ] FPS >30 di mobile, >60 di desktop
- [ ] Tidak ada P0 atau P1 bug terbuka
- [ ] `saveVersion` di-increment jika schema berubah
- [ ] `MIGRATIONS` table di-update jika schema berubah
- [ ] Changelog di-update
- [ ] Version number di-update di `Constants.lua`

### 5.2 Changelog Format

```markdown
# Changelog — Ninja Urban Farming

## v1.0.0-alpha (2026-07-15) — Lele Bioflok MVP

### Added
- 3 gallon biofloc system with water chemistry simulation
- Fish growth model (ABW, starter/grower/finisher phases)
- Feeding system with bibis fermentation
- Clinical disease system A (Ammonia Stress)
- Clinical disease system B (Saprolegniasis)
- Basic economy (credits from harvest)
- HUD with parameter monitoring
- DataStore save/load

### Changed
- (none — first release)

### Fixed
- (none — first release)

### Known Issues
- Offline progression not yet implemented (planned v2.0.0)
- BSF system not yet implemented (planned v3.0.0)
```

### 5.3 Publish Steps

```
1. Buka staging place di Roblox Studio
2. Rojo sync → pastikan semua script terbaru
3. Play test di Studio (smoke test)
4. Publish ke Roblox (File → Publish to Roblox)
5. Test di Roblox client (HP + desktop)
6. Jika semua OK:
   a. Buka production place
   b. Publish dengan version number di description
7. Tag release di Git:
   git tag -a v1.0.0-alpha -m "Lele Bioflok MVP"
   git push --tags
```

---

## 6. Rollback Procedure

Jika rilis production bermasalah:

```
1. IDENTIFIKASI: Cek error log, player reports
2. KEPUTUSAN: Rollback atau hotfix?
   - Hotfix (minor): fix bug → publish sebagai patch version
   - Rollback (major): kembalikan ke version sebelumnya
3. ROLLBACK:
   a. Buka production place di Roblox Studio
   b. Publish versi sebelumnya dari backup .rbxl file
   c. Atau: revert commit di Git → Rojo sync → publish
4. KOMUNIKASI:
   a. Update game description dengan status
   b. Post di Discord/community channel
5. INVESTIGASI: RC analysis → fix → test → re-release
```

---

## 7. Backup Strategy

| Apa | Frekuensi | Tempat |
|-----|-----------|--------|
| Source code (Git) | Setiap commit | GitHub repository |
| `.rbxl` file | Setiap milestone | GitHub Releases + local backup |
| Player DataStore | Automatic (Roblox) | Roblox cloud |
| Asset files (.fbx, .png, .wav) | Setiap selesai edit | GitHub LFS atau folder `assets/` |

---

## 8. Wally Dependencies

Gunakan [Wally](https://wally.run) untuk package management:

### 8.1 `wally.toml`

```toml
[package]
name = "ninja-urban-farming"
version = "0.1.0"
edition = "2021"

[dependencies]
# Testing framework (future)
TestEZ = "roblox/testez@0.4.1"

# UI library (jika dibutuhkan)
# Fusion = "elttob/fusion@0.3.0"

# Signal library
# SleitnickSignal = "sleitnick/signal@2.0.1"
```

### 8.2 Install & Update

```bash
wally install          # install dependencies
wally update           # update ke versi terbaru
rojo sourcemap         # generate sourcemap untuk Rojo
```

---

## 9. Analytics Integration (Optional — Future)

```lua
-- AnalyticsManager.server.lua (stub, aktifkan nanti)
local AnalyticsManager = {}
local webhookUrl = ""  -- isi dengan URL nanti

function AnalyticsManager.TrackEvent(playerId, eventName, properties)
    -- Kirim ke analytics service (Google Analytics, custom webhook, dll.)
    -- Untuk sekarang: log ke ErrorLogger
    ErrorLogger.Log("Analytics", eventName, {
        playerId = playerId,
        properties = properties,
    })
end

-- Events yang di-track:
-- "game_started" — player join pertama kali
-- "tutorial_completed" — selesai tutorial
-- "first_harvest" — panen pertama
-- "clinical_case_solved" — selesai kasus klinis
-- "certification_passed" — lulus sertifikasi
-- "purchase" — transaksi Robux
```

---

## 10. Quick Reference — File Yang Perlu Diupdate Setiap Rilis

| File | Apa yang Diupdate |
|------|------------------|
| `Constants.lua` | `GAME_VERSION = "v1.0.0-alpha"` |
| `CHANGELOG.md` | Tambah entry untuk versi baru |
| `wally.toml` | Update `version` field |
| Game description (Roblox) | Update nomor versi dan changelog ringkas |
| GitHub Release | Tag + changelog + attach `.rbxl` backup |

---

*End of Build & Release Pipeline.*

---

## DOKUMEN SELESAI — 16 DOKUMEN LENGKAP

| # | Dokumen | Status |
|---|---------|--------|
| 01 | Master Plan | ✅ |
| 02 | Sistem Mekanik | ✅ |
| 03 | Spesifikasi Teknis Roblox | ✅ |
| 04 | Kerangka Edukasi | ✅ |
| 05 | UI/UX Design | ✅ |
| 06 | Roadmap Development | ✅ |
| 07 | Gameplay | ✅ |
| 08 | Katalog Komoditas | ✅ |
| 09 | Validasi Ilmiah | ✅ |
| 10 | Audit Senior Developer | ✅ (eksternal) |
| 11 | Art Bible & Asset Inventory | ✅ |
| 12 | Data Schema & API Contract | ✅ |
| 13 | Coding Standards | ✅ |
| 14 | Testing & QA Plan | ✅ |
| 15 | Error Handling & Disaster Recovery | ✅ |
| 16 | Build & Release Pipeline | ✅ |

**Total: 16 dokumen, ~15.000+ baris. Siap development.**
