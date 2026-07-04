# 11 — ART BIBLE & ASSET INVENTORY

> **Target:** Solo developer + AI assistant. Daftar ini mencakup SEMUA aset visual dan audio yang harus dibuat. Gunakan sebagai checklist development.

---

## 1. Style Guide Visual

| Element | Spec |
|---------|------|
| **Art Style** | Low-poly stylized realism (mirip *Loomian Legacy* / *Adopt Me* tapi lebih grounded) |
| **Skala** | 1 stud = 10 cm. Raised bed 200×100 cm = 20×10 stud |
| **Palet Warna** | Lihat `05-UI-UX-Design.md` Section 7.1 |
| **Pencahayaan** | `Lighting.Technology = "Future"` — PBR-ready. `OutdoorAmbient = (0.7, 0.7, 0.7)` |
| **Target Poly** | Mobile-friendly: max 800 tris per model utama, max 300 tris per prop |

---

## 2. ENVIRONMENT ASSETS

### 2.1 Zona 1 — Stasiun Nutrisi (Bawah Atap)

| Asset ID | Nama | Poly | Texture | Animasi | Prioritas | Status |
|----------|------|------|---------|---------|-----------|--------|
| `ENV_roof_galvalume` | Atap galvalum | 400 | 1024×1024 (metal corrugated) | — | P0 | ⬜ |
| `ENV_roof_pillars` | Tiang penyangga atap (4 buah) | 100/each | 256×256 (galvanized steel) | — | P0 | ⬜ |
| `ENV_floor_concrete` | Lantai cor Zona 1 | 200 | 1024×1024 (concrete) | — | P0 | ⬜ |
| `ENV_fence_backyard` | Pagar batas halaman | 150 | 512×512 (wood/bamboo) | — | P1 | ⬜ |
| `ENV_background_city` | Siluet kota background | 500 | 1024×512 (low-poly skyline) | — | P2 | ⬜ |

### 2.2 Zona 2 — Area Terbuka

| Asset ID | Nama | Poly | Texture | Animasi | Prioritas | Status |
|----------|------|------|---------|---------|-----------|--------|
| `ENV_ground_soil` | Tanah/ground Zona 2 | — | `MaterialService` terrain | — | P0 | ⬜ |
| `ENV_path_stone` | Jalur setapak batu (min 40cm lebar) | 100/each | 512×512 (stone) | — | P0 | ⬜ |
| `ENV_sky` | Skybox urban siang/malam | — | `Sky` object (6-sided) | Day cycle | P0 | ⬜ |

---

## 3. SUBSYSTEM ASSETS — LELE BIOFLOK

| Asset ID | Nama | Poly | Texture | Animasi | Prioritas | Status |
|----------|------|------|---------|---------|-----------|--------|
| `LELE_gallon_body` | Galon air 19L (tembus pandang) | 300 | 512×512 (blue-tinted translucent) | — | P0 | ⬜ |
| `LELE_gallon_stand` | Dudukan galon kayu | 150 | 256×256 (wood) | — | P0 | ⬜ |
| `LELE_gallon_cap_valve` | Tutup galon dengan stop kran | 100 | 256×256 (plastic + brass) | Rotasi katup (buka/tutup) | P0 | ⬜ |
| `LELE_manifold_pipes` | Pipa manifold + 4 cabang | 200 | 256×256 (PVC white) | — | P0 | ⬜ |
| `LELE_aerator_pump` | Pompa aerator 18W | 200 | 512×512 (plastic) | — | P0 | ⬜ |
| `LELE_airstone` | Batu aerasi (3 buah) | 50/each | 128×128 (porous stone) | — | P0 | ⬜ |
| `LELE_fish_model` | Ikan lele (15–20 per galon) | 250 | 256×256 (dark grey) | Berenang (idle loop), megap-megap (stres), mati (floating) | P0 | ⬜ |
| `LELE_net_tool` | Serokan kecil (tool) | 150 | 256×256 (mesh + handle) | Scoop | P0 | ⬜ |
| `LELE_scale_tool` | Timbangan digital (tool) | 100 | 256×256 (plastic + screen) | — | P0 | ⬜ |
| `LELE_feed_bowl` | Mangkok pakan | 50 | 128×128 (plastic) | — | P1 | ⬜ |
| `LELE_ph_kit` | Kit tes pH (tool) | 50 | 128×128 (strip + card) | Dip | P1 | ⬜ |

**VFX Khusus Lele:**
- `VFX_bubbles` — ParticleEmitter gelembung dari batu aerasi (loop)
- `VFX_water_cloudy` — Efek kekeruhan air saat amonia tinggi (ColorCorrection pada gallon mesh)
- `VFX_fish_stress` — Garis merah berdenyut di sekitar ikan (Beam/Ring)
- `VFX_fish_disease_cotton` — Partikel putih berbulu (Saprolegnia)
- `VFX_fish_disease_ich` — Bintik putih statis pada texture (White Spot)

---

## 4. SUBSYSTEM ASSETS — BSF MAGGOT

| Asset ID | Nama | Poly | Texture | Animasi | Prioritas | Status |
|----------|------|------|---------|---------|-----------|--------|
| `BSF_biopond_box` | Box/ember biopond | 400 | 512×512 (plastic dark) | — | P0 | ⬜ |
| `BSF_ramp` | Papan miring 45° | 150 | 256×256 (wood) | — | P0 | ⬜ |
| `BSF_collector` | Wadah panen prepupa | 100 | 256×256 (plastic) | — | P0 | ⬜ |
| `BSF_larvae` | Larva BSF (~50-100 per biopond) | 100 | 128×128 (cream/pale) | Menggeliat (wriggle), merayap naik ramp (climb) | P0 | ⬜ |
| `BSF_prepupae` | Prepupa BSF (hitam) | 100 | 128×128 (dark brown/black) | Sama larva + climb ramp | P0 | ⬜ |
| `BSF_breeding_cage` | Kandang kawin kelambu | 300 | 256×256 (mesh fabric) | — | P0 | ⬜ |
| `BSF_adult_fly` | Lalat BSF dewasa | 100 | 128×128 (black metallic) | Terbang (hover), kawin | P0 | ⬜ |
| `BSF_egg_slat` | Bilah kayu tempat telur | 50 | 128×128 (wood) | — | P0 | ⬜ |

**VFX Khusus BSF:**
- `VFX_bsf_swarm` — Partikel kawanan lalat di kandang kawin (loop)
- `VFX_bsf_odor` — Partikel "bau" hijau saat substrat terlalu basah

---

## 5. SUBSYSTEM ASSETS — AYAM PETELUR

| Asset ID | Nama | Poly | Texture | Animasi | Prioritas | Status |
|----------|------|------|---------|---------|-----------|--------|
| `AYAM_coop` | Kandang ayam (struktur utama) | 800 | 1024×1024 (wood + mesh wire) | — | P0 | ⬜ |
| `AYAM_nest_box` | Kotak sarang bertelur (2–3 buah) | 150/each | 512×512 (wood + straw) | — | P0 | ⬜ |
| `AYAM_feeder` | Tempat pakan | 100 | 256×256 (plastic/wood) | — | P0 | ⬜ |
| `AYAM_waterer` | Tempat air minum | 80 | 256×256 (plastic) | — | P1 | ⬜ |
| `AYAM_chicken_model` | Ayam kampung (5 ekor) | 500 | 512×512 (brown/white/black variants) | Idle (diam), scratch (mengais), eat (makan), lay_egg (bertelur), walk (jalan) | P0 | ⬜ |
| `AYAM_egg_model` | Telur ayam | 50 | 128×128 (white/brown) | — | P0 | ⬜ |
| `AYAM_litter_material` | Material deep litter (daun + sekam) | — | 512×512 tileable | — | P0 | ⬜ |

**VFX Khusus Ayam:**
- `VFX_litter_steam` — Partikel uap halus dari deep litter (fermentasi aktif)
- `VFX_litter_ammonia` — Partikel bau saat C:N tidak seimbang

---

## 6. SUBSYSTEM ASSETS — RAISED BEDS & TANAMAN

### 6.1 Struktur Bedengan

| Asset ID | Nama | Poly | Texture | Animasi | Prioritas | Status |
|----------|------|------|---------|---------|-----------|--------|
| `BED_boards_long` | Papan cor panjang (200cm) | 150/each | 512×512 (wood grain) | — | P0 | ⬜ |
| `BED_boards_short` | Papan cor pendek (100cm) | 100/each | 512×512 (wood grain) | — | P0 | ⬜ |
| `BED_plastic_liner` | Mulsa plastik pelapis dalam | — | 256×256 (black plastic) | — | P0 | ⬜ |
| `BED_top_mulch` | Mulsa permukaan daun mangga | — | 512×512 tileable (dry leaves) | — | P0 | ⬜ |

### 6.2 Tanaman (11 spesies × 4–5 growth stages)

Setiap tanaman butuh varian model per fase. TOTAL: ~55 model tanaman.

| Asset ID Base | Spesies | Fase 1: Semai | Fase 2: Veg Awal | Fase 3: Veg Akhir | Fase 4: Panen | Fase 5: Bunga/Buah | Prioritas |
|---------------|---------|---------------|-------------------|-------------------|---------------|---------------------|-----------|
| `PLANT_kangkung` | Kangkung | Poly: 30 | Poly: 60 | Poly: 100 | Poly: 150 | — | P0 |
| `PLANT_sawi` | Sawi | 30 | 60 | 120 | 180 | — | P0 |
| `PLANT_caisim` | Caisim | 30 | 60 | 120 | 180 | — | P0 |
| `PLANT_pakcoy` | Pakcoy | 30 | 70 | 130 | 200 | — | P0 |
| `PLANT_bayam_hijau` | Bayam Hijau | 30 | 50 | 80 | 120 | — | P0 |
| `PLANT_bayam_merah` | Bayam Merah | 30 | 50 | 80 | 120 | — | P1 |
| `PLANT_selada` | Selada | 30 | 60 | 100 | 180 | Bolting (tangkai bunga) | P0 |
| `PLANT_tomat` | Tomat | 30 | 60 | 120 | 200 | Bunga → buah hijau → buah merah | P0 |
| `PLANT_cabai_rawit` | Cabai Rawit | 30 | 60 | 100 | 180 | Bunga → buah hijau → buah merah | P0 |
| `PLANT_cabai_keriting` | Cabai Keriting | 30 | 60 | 100 | 180 | Bunga → buah hijau → buah merah | P1 |
| `PLANT_terong` | Terong | 30 | 70 | 130 | 200 | Bunga → buah ungu | P0 |
| `PLANT_kacang_panjang` | Kacang Panjang | 30 | 80 (+lanjaran) | 150 | 220 | Bunga → polong hijau | P0 |
| `PLANT_pepaya` | Pepaya California | — | 200 | 400 | 800 | Bunga → buah hijau → buah oranye | P1 |
| `PLANT_stroberi` | Stroberi | 30 | 60 | 80 | 100 | Bunga → buah merah | P1 |

**Tekstur Tanaman Spesial:**
- Semua tanaman menggunakan tekstur atlas yang sama per spesies
- Defisiensi N: overlay kuning (shader `uniformYellow`)
- Defisiensi Mg: overlay pola retikulat kuning (shader `interveinalChlorosis`)
- Defisiensi P: overlay ungu di daun tua
- Defisiensi K: overlay cokelat di tepi daun
- Defisiensi Ca: busuk ujung buah (tekstur cokelat/hitam)
- Semua shader defisiensi = `SurfaceAppearance.Color` + opacity lerp

---

## 7. TOOLS & PROPS

| Asset ID | Nama | Poly | Texture | Prioritas | Status |
|----------|------|------|---------|-----------|--------|
| `TOOL_measuring_spoon` | Sendok takar | 80 | 256×256 | P0 | ⬜ |
| `TOOL_watering_can` | Gembor | 200 | 512×512 | P0 | ⬜ |
| `TOOL_spray_bottle` | Botol semprot | 150 | 256×256 | P0 | ⬜ |
| `TOOL_shredder_machine` | Mesin pencacah daun | 400 | 512×512 | P0 | ⬜ |
| `TOOL_thermometer` | Termometer digital | 60 | 128×128 | P1 | ⬜ |
| `PROP_composter_drum` | Tong komposter aerob | 300 | 512×512 | P0 | ⬜ |
| `PROP_ee_container_s` | Kontainer EE kecil (5L) | 100 | 256×256 | P0 | ⬜ |
| `PROP_ee_container_l` | Kontainer EE besar (20L) | 150 | 256×256 | P0 | ⬜ |
| `PROP_em4_jerigen` | Jerigen EM-Aktif | 120 | 256×256 | P0 | ⬜ |
| `PROP_crafting_station` | Stasiun crafting booster | 400 | 512×512 | P1 | ⬜ |
| `PROP_yellow_trap` | Yellow sticky trap | 40 | 128×128 | P1 | ⬜ |
| `PROP_ajir_lanjaran` | Ajir/lanjaran bambu | 30 | 128×128 | P0 | ⬜ |
| `PROP_shade_net` | Paranet 50% shade | 200 | 512×512 (mesh) | P2 | ⬜ |

---

## 8. CHARACTER & NPC

| Asset ID | Nama | Poly | Texture | Animasi | Prioritas | Status |
|----------|------|------|---------|---------|-----------|--------|
| `CHAR_ninja_mentor` | NPC Mentor Ninja | 800 | 1024×1024 (farmer outfit) | Idle, walk, point, wave, celebrate | P0 | ⬜ |
| `CHAR_player_default` | Karakter pemain (R15) | R15 rig | 1024×1024 | Default Roblox anims | P0 | ⬜ |
| `CHAR_player_outfits` | Outfit kustom (3 varian) | — | 512×512 per outfit | — | P1 | ⬜ |

---

## 9. UI ASSETS

| Asset ID | Nama | Dimensi | Format | Prioritas | Status |
|----------|------|---------|--------|-----------|--------|
| `UI_logo` | Logo game | 512×256 | PNG | P0 | ⬜ |
| `UI_icons_sub_systems` | 8 ikon subsistem | 64×64 each | PNG sprite sheet | P0 | ⬜ |
| `UI_icons_parameters` | Ikon parameter (pH, temp, DO, dll.) | 32×32 each | PNG sprite sheet | P0 | ⬜ |
| `UI_icons_actions` | Ikon aksi (feed, flush, harvest, etc.) | 48×48 each | PNG sprite sheet | P0 | ⬜ |
| `UI_icons_diseases` | Ikon gejala penyakit | 64×64 each | PNG sprite sheet | P0 | ⬜ |
| `UI_icons_deficiency` | Ikon defisiensi (N, P, K, Ca, Mg, Fe, water, light) | 48×48 each | PNG sprite sheet | P0 | ⬜ |
| `UI_panel_bg` | Background panel UI | 256×256 tileable | PNG (semi-transparent dark) | P0 | ⬜ |
| `UI_radial_menu_bg` | Background radial menu | 256×256 | PNG | P0 | ⬜ |
| `UI_button_primary` | Tombol primer (9-slice) | 128×64 | PNG 9-slice | P0 | ⬜ |
| `UI_button_secondary` | Tombol sekunder (9-slice) | 128×64 | PNG 9-slice | P0 | ⬜ |
| `UI_progress_bar` | Progress bar (9-slice) | 256×32 | PNG 9-slice | P0 | ⬜ |
| `UI_gauge_ph` | Pengukur pH | 200×40 | PNG | P0 | ⬜ |
| `UI_font_main` | Font utama (Gotham/Fredoka One) | — | TTF/OTF | P0 | ⬜ |
| `UI_font_mono` | Font monospace (Roboto Mono) | — | TTF/OTF | P0 | ⬜ |

---

## 10. AUDIO ASSETS

### 10.1 Ambient (Looping)

| Asset ID | Nama | Durasi | Trigger | Prioritas | Status |
|----------|------|--------|---------|-----------|--------|
| `SFX_ambient_day` | Ambient siang (burung, angin) | 60s loop | Day phase | P0 | ⬜ |
| `SFX_ambient_night` | Ambient malam (jangkrik) | 60s loop | Night phase | P0 | ⬜ |
| `SFX_ambient_rain_light` | Hujan ringan | 30s loop | Rain event | P0 | ⬜ |
| `SFX_ambient_rain_heavy` | Hujan lebat | 30s loop | Heavy rain event | P0 | ⬜ |
| `SFX_ambient_city_hum` | Dengung kota jauh | 30s loop | Always (low volume) | P1 | ⬜ |

### 10.2 Mekanis (Looping)

| Asset ID | Nama | Durasi | Trigger | Prioritas | Status |
|----------|------|--------|---------|-----------|--------|
| `SFX_aerator_hum` | Dengung aerator | Loop | Pump ON. Pitch shift with load | P0 | ⬜ |
| `SFX_aerator_overheat` | Aerator overheat warning | Loop | Bleeding valve closed >2h | P1 | ⬜ |
| `SFX_shredder_run` | Mesin pencacah | 5s | Shredder active | P0 | ⬜ |

### 10.3 Interaksi (One-Shot)

| Asset ID | Nama | Durasi | Trigger | Prioritas | Status |
|----------|------|--------|---------|-----------|--------|
| `SFX_valve_open` | Buka katup (flush) | 2s | Flush action | P0 | ⬜ |
| `SFX_water_splash` | Percikan air | 1s | Water interaction | P0 | ⬜ |
| `SFX_water_flow` | Air mengalir | 3s | Watering plants | P0 | ⬜ |
| `SFX_feed_scoop` | Menyendok pakan | 0.5s | Feed scoop | P0 | ⬜ |
| `SFX_feed_pour` | Menuang pakan ke galon | 1s | Feed action | P0 | ⬜ |
| `SFX_egg_collect` | Koleksi telur (clink) | 0.5s | Collect egg | P0 | ⬜ |
| `SFX_chicken_cluck` | Ayam berkotek | 1s | Random idle | P0 | ⬜ |
| `SFX_chicken_scratch` | Ayam mengais | 0.5s | Scratch anim | P1 | ⬜ |
| `SFX_bsf_buzz` | Lalat BSF berdengung | 2s | Near breeding cage | P0 | ⬜ |
| `SFX_bsf_prepupae_drop` | Prepupa jatuh ke wadah | 0.3s | Prepupae collect | P0 | ⬜ |
| `SFX_fish_splash` | Ikan memercik | 0.5s | Fish jump/splash | P0 | ⬜ |
| `SFX_composter_turn` | Putar komposter | 1s | Turn composter | P1 | ⬜ |
| `SFX_harvest_plant` | Panen sayuran (pop) | 0.5s | Harvest plant | P0 | ⬜ |
| `SFX_harvest_leafy` | Panen sayuran daun (crunch) | 0.5s | Harvest leafy veg | P0 | ⬜ |

### 10.4 UI Feedback (One-Shot)

| Asset ID | Nama | Durasi | Trigger | Prioritas | Status |
|----------|------|--------|---------|-----------|--------|
| `SFX_ui_click` | Klik tombol | 0.1s | Button press | P0 | ⬜ |
| `SFX_ui_success` | Ding sukses | 0.5s | Action success | P0 | ⬜ |
| `SFX_ui_error` | Buzz error | 0.3s | Action fail | P0 | ⬜ |
| `SFX_ui_alert` | Peringatan klinis | 0.8s | Clinical alert | P0 | ⬜ |
| `SFX_ui_achievement` | Fanfare achievement | 2s | Achievement unlock | P1 | ⬜ |
| `SFX_ui_levelup` | Nada naik (level up) | 1.5s | Level up | P1 | ⬜ |
| `SFX_ui_loop_health` | Nada orkestra bertahap | 3s | Loop Health milestone | P2 | ⬜ |
| `SFX_ui_kaching` | Kaching kredit | 0.3s | Earn credits | P0 | ⬜ |

### 10.5 Hewan (One-Shot)

| Asset ID | Nama | Durasi | Trigger | Prioritas | Status |
|----------|------|--------|---------|-----------|--------|
| `SFX_fish_eat` | Ikan makan | 0.3s | Feed fish | P1 | ⬜ |
| `SFX_fish_stress` | Ikan stres (gasping) | 1s | Fish at surface | P1 | ⬜ |
| `SFX_chicken_egg_lay` | Ayam bertelur | 1s | Egg laid | P1 | ⬜ |

---

## 11. SPRITE SHEET RINGKASAN

| Sheet | Isi | Dimensi | Grid |
|-------|-----|---------|------|
| `spritesheet_subsystems` | 8 ikon subsistem | 256×64 | 8×1 (32px) |
| `spritesheet_parameters` | 12 ikon parameter | 384×32 | 12×1 (32px) |
| `spritesheet_actions` | 8 ikon aksi | 384×48 | 8×1 (48px) |
| `spritesheet_diseases` | 8 ikon penyakit ikan + 7 tanaman | 960×64 | 15×1 (64px) |
| `spritesheet_deficiency` | 8 ikon defisiensi | 384×48 | 8×1 (48px) |

---

## 12. PRODUCTION CHECKLIST

Gunakan checklist ini untuk tracking progres. Centang `⬜ → ✅` saat aset selesai.

**Prioritas P0 (wajib untuk Fase 1):** ~65 aset
**Prioritas P1 (wajib untuk Fase 3):** ~20 aset
**Prioritas P2 (nice-to-have):** ~10 aset

**TOTAL: ~95 aset yang harus dibuat.**
