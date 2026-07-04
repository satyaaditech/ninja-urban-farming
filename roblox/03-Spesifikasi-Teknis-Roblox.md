# 03 — SPESIFIKASI TEKNIS ROBLOX STUDIO

---

## 1. Gambaran Umum

Dokumen ini menetapkan arsitektur teknis untuk mengimplementasikan Ninja Urban Farming sebagai game Roblox menggunakan fitur-fitur terbaru Roblox Studio (skrip Luau, API modern, dan rendering canggih). Semua logika simulasi bersifat server-otoritatif. Klien menangani rendering, input, UI, dan prediksi lokal.

---

## 2. Tumpukan Teknologi (API Roblox)

| Kategori | API / Layanan |
|----------|----------------|
| **Skrip** | Luau (typed, strict mode), ModuleScripts untuk semua logika |
| **Persistensi Data** | `DataStoreService` (progres pemain), `MemoryStoreService` (state multiplayer langsung), `MessagingService` (event lintas server) |
| **Fisika** | `Workspace.Gravity`, `BasePart.CustomPhysicalProperties` untuk daya apung (air), `Constraints` untuk sambungan pipa/manifold |
| **UI** | `ScreenGui`, `Frame`, `TextLabel`, `ImageLabel`, `ScrollingFrame`, `ViewportFrame` (pratinjau 3D) |
| **Input** | `UserInputService`, `ContextActionService`, `ProximityPrompt` (interaksi) |
| **Audio** | `SoundService`, objek `Sound` dengan ambient berlapis/looping, `DynamicSoundGroup` untuk mixing |
| **Pencahayaan** | `Lighting.TimeOfDay`, `Atmosphere`, `Sky`, `SunRays`, `Bloom`, `ColorCorrection` — siklus siang/malam dinamis |
| **Terrain** | Editor `Terrain` untuk lanskap dasar, `MaterialService` untuk tekstur terrain |
| **Material** | `MaterialService` dengan PBR `MaterialVariants` 2023+ untuk tanah, air, kayu, logam yang realistis |
| **Surface Appearance** | `SurfaceAppearance` untuk tekstur detail pada model Galon, Biopond, Raised Bed |
| **Partikel** | `ParticleEmitter` untuk gelembung air (aerator), uap kompos, terbang BSF, serbuk sari tanaman |
| **Beams** | `Beam` untuk semprotan air dari selang, tetesan dari pipa |
| **TweenService** | Semua animasi UI, interpolasi pertumbuhan tanaman, rotasi katup |
| **CollectionService** | Menandai semua objek interaktif (mis., "Interactable", "Subsystem", "WaterSource") |
| **RunService** | `Heartbeat` (render klien), `Stepped` (fisika), `PostSimulation` (tick server) |
| **TeleportService** | Berpindah antar mode game (cerita, sandbox, kelas) |
| **LocalizationService** | Dukungan multi-bahasa (ID, EN, + bahasa mendatang) |
| **Analitik** | `LogService` untuk laporan crash; analitik kustom via `HttpService` ke dasbor eksternal |

---

## 3. Arsitektur: Simulasi Server-Otoritatif

### 3.1 Hierarki ModuleScript

```
ServerScriptService/
├── SimulationEngine/
│   ├── Init.server.lua             # Bootstrap, pemuatan modul
│   ├── TimeManager.server.lua      # Skala waktu game, siklus siang/malam
│   ├── LeleBioflok/
│   │   ├── WaterChemistry.lua      # Kalkulasi pH, NH3, NO2, DO
│   │   ├── FishGrowth.lua          # ABW, fase, pakan, kematian
│   │   ├── DiseaseEngine.lua       # Deteksi pemicu klinis, progresi
│   │   └── GallonManager.lua       # State per galon, flushing, aerasi
│   ├── BSF_Maggot/
│   │   ├── Lifecycle.lua           # Telur → larva → prepupa → pupa → dewasa
│   │   ├── SubstrateManager.lua    # Jenis pakan, dekomposisi, bau
│   │   └── HarvestSystem.lua       # Migrasi ramp, auto-koleksi
│   ├── AyamPetelur/
│   │   ├── ChickenBehavior.lua     # Mengais, makan, stres
│   │   ├── DeepLitter.lua          # Model fermentasi, keseimbangan C:N
│   │   └── EggProduction.lua       # Kalkulasi laju, faktor kualitas
│   ├── RaisedBed/
│   │   ├── SoilChemistry.lua       # NPK, pH, kelembapan, KTK, mikroba
│   │   ├── PlantGrowth.lua         # Kurva pertumbuhan spesifik spesies
│   │   ├── PlantDisease.lua        # Pemicu + progresi penyakit
│   │   ├── DeficiencyEngine.lua    # Deteksi defisiensi nutrisi (N, P, K, Ca, Mg, Fe)
│   │   └── PestSystem.lua          # Tekanan hama, kerusakan, pengendalian
│   ├── KomposterEE/
│   │   ├── CompostEngine.lua       # Dekomposisi, suhu, kematangan
│   │   └── EcoEnzyme.lua           # Fermentasi, maturasi, kualitas
│   ├── OrganicBoosters/
│   │   ├── KBooster.lua
│   │   ├── AminorGrow.lua
│   │   ├── CalPhos.lua
│   │   ├── MagElixir.lua
│   │   ├── HumoNinja.lua
│   │   ├── JMS_IMO.lua
│   │   ├── HumicFulvic.lua
│   │   └── EM_Active.lua
│   ├── ClosedLoopTracker.lua       # Aliran sumber daya, skor Loop Health
│   ├── EconomyManager.lua          # Kredit, pengeluaran, pasar
│   ├── ClinicalCaseGenerator.lua   # Pembuatan tantangan prosedural
│   ├── OfflineProgression.lua      # Simulasi catch-up saat player login
│   └── TimeSystem.lua              # Jam game, konfigurasi kecepatan
├── ServerCore/
│   ├── DataStoreManager.server.lua # Simpan/muat data + retry + migrasi
│   ├── RemoteHandler.server.lua    # Handler untuk semua RemoteEvent
│   ├── AntiCheat.server.lua        # Validasi + cooldown + rate limit
│   └── ErrorLogger.server.lua      # Pencatatan error + ring buffer

ReplicatedStorage/
├── Shared/
│   ├── Constants.lua               # Semua parameter tuning, ambang, resep
│   ├── Types.lua                   # Definisi tipe Luau
│   ├── Formulas.lua                # Fungsi kalkulasi bersama (ABW, kalkulasi pakan)
│   ├── DiseaseDatabase.lua         # Definisi kondisi klinis
│   └── RecipeDatabase.lua          # Semua resep crafting

StarterPlayer/
├── StarterPlayerScripts/
│   ├── ClientInit.client.lua       # Bootstrap klien
│   ├── InputManager.client.lua     # Keyboard, mouse, sentuh, gamepad
│   ├── CameraController.client.lua # Orbit, zoom, fokus pada subsistem
│   └── HapticFeedback.client.lua   # Getaran mobile pada interaksi

StarterGui/
├── GuiController.client.lua        # Orkestrator UI utama
├── HUD/
│   ├── DashboardHUD.lua            # Monitor parameter tingkat atas
│   ├── TimeDisplay.lua             # Jam game, indikator siang/malam
│   ├── AlertSystem.lua             # Peringatan klinis, pengingat
│   └── QuickActions.lua            # Tombol aksi kontekstual
├── Panels/
│   ├── LelePanel.lua               # Kimia air, status ikan per galon
│   ├── BSF_Panel.lua               # Tahap siklus hidup, status substrat
│   ├── ChickenPanel.lua            # Produksi telur, kondisi litter
│   ├── GardenPanel.lua             # Nutrisi tanah, pertumbuhan, penyakit
│   ├── CompostPanel.lua            # Progres dekomposisi
│   ├── CraftingPanel.lua           # Browser resep, antrian crafting
│   ├── EconomyPanel.lua            # Buku besar pemasukan/pengeluaran
│   ├── LoopHealthPanel.lua         # Dasbor efisiensi siklus tertutup
│   └── SettingsPanel.lua           # Audio, video, bahasa, aksesibilitas
├── Modals/
│   ├── ClinicalCaseModal.lua       # Antarmuka diagnosis, pemilihan pengobatan
│   ├── TutorialModal.lua           # Overlay panduan langkah demi langkah
│   ├── HarvestModal.lua            # Hasil panen, grading
│   └── CertificationModal.lua      # Antarmuka ujian, hasil
└── Components/
    ├── ParameterBar.lua            # Pengukur parameter yang dapat digunakan ulang
    ├── ProgressWheel.lua           # Indikator progres fermentasi/pertumbuhan
    ├── SymptomViewer.lua           # Pembantu diagnosis visual close-up
    └── MiniMap.lua                 # Peta gambaran zona
```

### 3.2 Aliran Data

```
[Input Klien] → RemoteEvent → [Validasi Server]
                                     │
                                     ▼
                            [Server Simulation Engine]
                            (Pembaruan state otoritatif)
                                     │
                                     ▼
                     [RemoteEvent] → [Client Renderer]
                     (State direplikasi)   (UI + Visual)
```

**RemoteEvents (Klien → Server):**
- `PerformAction` — aksi generik: flush katup, beri pakan ikan, tanam benih, panen, dll.
- `CraftRecipe` — mulai crafting booster/EE/EM4
- `SubmitDiagnosis` — kirim diagnosis klinis dan pengobatan
- `PurchaseItem` — beli dari pasar
- `ConfigurePlacement` — atur tata letak zona, sambungkan pipa
- `SetTimeScale` — ubah akselerasi waktu
- `RequestTimeSkip` — lompat waktu (tutorial only, max 3 token)

**RemoteEvents (Server → Klien):**
- `SyncState` — sinkronisasi state penuh saat bergabung (atau sinkronisasi delta setelahnya)
- `StateDelta` — perubahan parameter inkremental setiap tick
- `ClinicalAlert` — pemicu UI diagnosis dengan gejala
- `AchievementUnlocked` — notifikasi
- `TimeUpdate` — waktu game saat ini, fase hari
- `CatchupNotification` — ringkasan offline progression saat login
- `MentorDialogue` — dialog NPC Mentor Ninja (story mode)
- `LoopHealthUpdate` — update skor Loop Health + breakdown

---

## 4. Arsitektur Tick Simulasi

### 4.1 Tick Server (30 detik nyata = 1 langkah simulasi)

```
ServerTick (setiap 30 detik):
  untuk setiap subsistem:
    1. Baca state saat ini
    2. Terapkan kalkulasi delta yang diskalakan waktu
    3. Periksa ambang pemicu klinis
    4. Tulis state baru
    5. Hasilkan StateDelta untuk klien yang berlangganan
  
  Perbarui skor LoopHealth
  Perbarui ekonomi (pendapatan/pengeluaran pasif)
  Periksa kondisi achievement
  Simpan ke DataStore (setiap 5 menit atau pada event signifikan)
```

### 4.2 Tick Klien (setiap frame via Heartbeat)

```
ClientTick (setiap frame):
  1. Interpolasi state visual (pertumbuhan tanaman, kekeruhan air, efek partikel)
  2. Perbarui nilai HUD dari StateDelta terbaru
  3. Proses input
  4. Perbarui kamera
  5. Periksa highlight kedekatan interaksi
```

### 4.3 Skala Waktu

```
deltaSimulasi = deltaNyata * skalaWaktu

pemetaan skalaWaktu:
  "1x" (normal)     = 1 hari game per 15 menit nyata → skalaWaktu = 96
  "2x" (cepat)      = 1 hari game per 7.5 menit nyata → skalaWaktu = 192
  "4x" (lompat)     = 1 hari game per 3.75 menit nyata → skalaWaktu = 384
  "krisis"          = 1 jam game per 30 detik nyata → skalaWaktu = 120
  "jeda"            = 0
```

---

## 5. Model Data & Persistensi

### 5.1 Skema Data Pemain (DataStore)

```lua
type DataPemain = {
    -- Meta
    playerId: number,
    versiSimpanan: number,
    terakhirDisimpan: number,  -- os.time()
    totalWaktuBermain: number,
    modeGame: "cerita" | "sandbox" | "kelas",
    babCerita: number,  -- 0–16
    tutorialSelesai: boolean,

    -- Ekonomi
    kredit: number,
    totalDihasilkan: number,
    totalDibelanjakan: number,

    -- Lele Bioflok
    galonLele: { [indeksGalon: number]: StateGalonLele },

    -- Maggot BSF
    stateBSF: StateKoloniBSF,
    totalBSFDipanen_g: number,

    -- Ayam Petelur
    stateAyam: StateKoloniAyam,
    totalTelurDikumpulkan: number,
    stateDeepLitter: StateDeepLitter,

    -- Raised Beds
    raisedBeds: { [indeksBed: number]: StateRaisedBed },

    -- Komposter & EE
    komposter: { [indeksKomposter: number]: StateKomposter },
    batchEE: { [indeksBatch: number]: StateEE },

    -- Booster yang Di-craft (inventaris)
    inventaris: { [itemId: string]: number },

    -- State EM4
    stateEMAktif: StateEMAktif?,

    -- Tata letak farm
    penempatanZona: DataPenempatanZona,

    -- Progres
    achievements: { [achievementId: string]: boolean },
    kasusKlinisDiselesaikan: number,
    akurasiKlinis: number,
    riwayatLoopHealth: { number },
    sertifikasi: { [certId: string]: { lulus: boolean, skor: number, tanggal: number } },

    -- Pengaturan
    bahasa: string,  -- "id" | "en"
    modeAksesibilitas: "default" | "sederhana" | "butaWarna" | "tts",
    volumeAudio: { master: number, musik: number, sfx: number, ambient: number },
}
```

### 5.3 Simulasi Offline (Offline Progression)

Saat pemain logout, sistem menyimpan timestamp dan menerapkan simulasi catch-up saat login kembali:

```lua
-- TimeManager.server.lua
function TimeManager:CalculateOfflineProgress(playerData)
    local lastLogout = playerData.lastLogoutTimestamp or os.time()
    local offlineSeconds = os.time() - lastLogout

    -- Batas aman: maksimal 24 jam disimulasikan
    local simSeconds = math.min(offlineSeconds, 86400)

    if simSeconds <= 0 then return end

    local gameDays = (simSeconds * self.timeScale) / 86400

    -- ATURAN SIMULASI OFFLINE:
    -- 1. Tidak ada krisis/penyakit dipicu (no crisis mode)
    -- 2. Pakan diasumsikan 50% dari normal
    -- 3. Tanaman auto-water minimal (30% lebih lambat)
    -- 4. Fermentasi dan kompos berjalan NORMAL

    for _, gallon in pairs(playerData.galonLele) do
        gallon:SimulateGrowth(gameDays * 0.5)
        gallon:SimulateChemistry(gameDays * 0.3)
        gallon.diseaseCheckSuspended = true
    end

    for _, bed in pairs(playerData.raisedBeds) do
        bed:SimulateGrowth(gameDays * 0.7)
        bed.pestCheckSuspended = true
    end

    playerData:SimulateFermentation(gameDays)
    playerData:SimulateComposting(gameDays)

    self:ClearSuspensionFlags(playerData)

    return {
        gameDaysPassed = gameDays,
        offlineHours = offlineSeconds / 3600,
    }
end
```

**Skema Data Tambahan:**

```lua
type DataPemain = {
    -- ... field yang sudah ada ...

    -- Meta offline
    lastLogoutTimestamp: number,  -- os.time() saat terakhir logout
}
```

**Notifikasi Catch-Up (Client UI):**

Saat login, tampilkan popup ringkasan sebelum pemain masuk ke farm. Contoh:

> "Kamu offline 8.5 jam. 🐟 Lele tumbuh +4.2g | 🌱 Kangkung tumbuh 3 hari | ♻ Kompos 12% lebih matang | 🧪 Eco-Enzyme batch #2 siap panen!"

---

## 6. Strategi Visual & Rendering

### 6.1 Desain Lingkungan

| Area | Perlakuan Visual |
|------|----------------|
| **Zona 1 (Stasiun Nutrisi)** | Di bawah atap galvalum — bayangan lembut, pencahayaan terkontrol, atap logam reflektif |
| **Zona 2 (Produksi)** | Matahari penuh — cerah, bayangan dinamis bergeser dengan siklus hari, tanaman teranimasi angin |
| **Latar Belakang** | Siluet cakrawala urban (low-poly) — memperkuat konteks "urban farming" |
| **Tanah** | Tekstur tanah PBR menggunakan `MaterialService`, terrain dengan bercak rumput |

### 6.2 Kebutuhan Model

| Aset | Jumlah Poligon (maks) | Resolusi Tekstur | Catatan |
|-------|-----------------|-------------------|-------|
| Galon (tangki lele) | 300 tris | 512×512 | Material transparan untuk visibilitas air |
| Raised Bed | 200 tris | 256×256 (serat kayu) | Skala 200×100×20 cm |
| Biopond BSF | 400 tris | 512×512 | Ramp miring, kontainer penampungan |
| Kandang Ayam | 800 tris | 512×512 | Deep litter terlihat di dalam |
| Drum Komposter | 300 tris | 256×256 | Animasi berputar |
| Kontainer EE | 200 tris | 256×256 | Berbagai ukuran |
| Model Ayam | 500 tris | 512×512 | 2–3 state animasi |
| Model Lalat BSF | 100 tris | 128×128 | Entitas kecil mirip partikel |
| Model Ikan Lele | 250 tris | 256×256 | Animasi berenang |
| Model Tanaman | 50–150 tris per tanaman | 256×256 | Varian tahap tumbuh (semai → matang) |
| Karakter Pemain | R15 rig | Standar | Varian outfit petani ninja |
| Alat (serokan, sendok, gembor) | 100–200 tris | 256×256 | Animasi dipegang |

### 6.3 Indikator Parameter Visual

Parameter harus memiliki **perubahan world-space yang terlihat**, bukan hanya angka UI:

| Parameter | Indikator Visual |
|-----------|-----------------|
| Amonia tinggi | Air berubah kuning-hijau keruh; ikan melayang di permukaan (pose vertikal statis) |
| DO rendah | Animasi ikan megap-megap; gelembung lebih sedikit/kecil dari aerator |
| pH rendah | Air sedikit lebih jernih tetapi stres ikan terlihat (gerakan tak menentu) |
| Saprolegnia | Partikel putih berbulu menempel di permukaan model ikan |
| Layu Fusarium | Daun menguning dari bawah → cokelat; tanaman merunduk saat jam "siang" in-game |
| Antraknosa | Bercak melingkar gelap pada tekstur model buah |
| Defisiensi Nitrogen | Penguningan daun merata (shader klorosis) |
| Defisiensi Magnesium | Klorosis interveinal — kuning di antara urat hijau |
| Tanah sehat | Tekstur gelap, remah; cacing tanah terlihat |
| Kematangan kompos | Pergeseran warna: segar (hijau/cokelat) → aktif (partikel uap) → matang (gelap, remah) |
| Deep litter aktif | Partikel uap lembut; ayam mengais teranimasi |
| Prepupa BSF siap | Larva cokelat tua/hitam memanjat ramp (gerakan teranimasi) |

### 6.4 Siang/Malam & Cuaca

| Waktu | Pencahayaan |
|------|----------|
| 05:00–06:00 | Fajar — oranye hangat, bayangan panjang |
| 06:00–11:00 | Pagi — cerah, putih netral |
| 11:00–14:00 | Siang — tajam di atas, bayangan pendek |
| 14:00–17:00 | Sore — keemasan hangat, bayangan memanjang |
| 17:00–18:30 | Senja — oranye/merah muda, bayangan sangat panjang |
| 18:30–05:00 | Malam — cahaya bulan, ambient redup, suara nokturnal |

**Kejadian Cuaca (acak atau dipicu skenario):**

| Cuaca | Efek pada Gameplay |
|---------|-------------------|
| Cerah (probabilitas 70%) | Kondisi normal |
| Mendung (15%) | Penguapan berkurang, laju fotosintesis lebih rendah (-15%) |
| Hujan Ringan (10%) | Penyiraman otomatis untuk raised bed, substrat BSF lebih basah, ayam mencari naungan |
| Hujan Lebat (4%) | Risiko percikan tanah raised bed, penurunan pH di galon lele (air hujan asam ~pH 5.6), risiko banjir |
| Gelombang Panas (1%) | Suhu air melonjak, DO menurun, stres ikan meningkat |

---

## 7. Sistem Interaksi

### 7.1 Jenis Interaksi

```
JenisInteraksi:
  "klik"       — Klik sederhana pada objek (kumpulkan telur, flush katup)
  "tahan"      — Tahan selama durasi (putar kompos, aduk EE, aerasi manual)
  "seret"      — Seret item ke target (tambah pakan ke biopond, tuang air)
  "pilih"      — Pilih dari menu (pilih pengobatan, pilih resep)
  "ukur"       — Gunakan alat untuk membaca nilai (strip pH, termometer, timbangan)
```

### 7.2 ProximityPrompts

Semua objek interaktif menggunakan `ProximityPrompt` dengan label kontekstual:

```lua
-- Contoh: Katup flush galon
local prompt = Instance.new("ProximityPrompt")
prompt.ActionText = "Buka Keran (Flush)"
prompt.ObjectText = "Galon Lele #1"
prompt.HoldDuration = 1.5  -- tahan 1.5 detik untuk flush
prompt.RequiresLineOfSight = true
prompt.MaxActivationDistance = 8
```

### 7.3 Sistem Alat

Alat yang dapat dipasang pemain:

| Alat | Fungsi | Visual |
|------|----------|--------|
| **Sendok Takar** | Menyendok dan mengukur pakan/bubuk | Dipegang di tangan |
| **Timbangan Digital** | Menimbang ikan, mengukur bahan | Diletakkan di permukaan, overlay UI |
| **Kit Tes pH** | Membaca pH air | Celup strip → bandingkan carta warna |
| **Termometer** | Mengukur suhu air/kompos/tanah | Celup → baca tampilan digital |
| **Gembor** | Menyiram tanaman / mengaplikasikan booster cair | Dibawa, miringkan untuk menuang |
| **Serokan** | Menangkap ikan untuk sampling | Animasi menyerok |
| **Botol Semprot** | Mengaplikasikan EE, PesNab, minyak mimba | Partikel semprot + kabut |
| **Mesin Pencacah** | Mencacah daun untuk kompos/litter | Mesin stasioner, input pakan |

---

## 8. Desain Audio

### 8.1 Lapisan Suara

| Lapisan | Konten | Jenis |
|-------|---------|------|
| **Ambient** | Kicau burung (pagi), jangkrik (malam), dengung kota jauh, hujan | Looping |
| **Mekanis** | Dengung aerator (konstan, pitch bergeser dengan beban), pompa air, pencacah | Looping |
| **Hewan** | Ayam berkotek, lele memercik, BSF berdengung | One-shot / looping |
| **Air** | Menetes, memercik, mengalir (katup terbuka), hujan di atap | One-shot |
| **UI** | Klik tombol, notifikasi, peringatan, fanfare achievement | One-shot |
| **Suara** | Garis panduan NPC Mentor Ninja (opsional, dapat di-toggle) | One-shot |

---

## 9. Anggaran Performa

| Metrik | Target | Alasan |
|--------|--------|-----------|
| Heartbeat server | ~30ms (tick 30 detik nyata) | Simulasi tidak per-frame; batching efisien |
| FPS klien | Target 60 FPS (minimal 30 FPS di mobile) | Performa standar Roblox |
| Memori (server) | < 200 MB per instans server | Terkelola dengan hingga 10 pemain bersamaan |
| Memori (klien) | < 500 MB | Streaming aset, anggaran tekstur |
| Bandwidth jaringan (server→klien) | < 50 KB/s per pemain | Delta state kompak, tanpa sinkronisasi penuh setelah awal |
| Bandwidth jaringan (klien→server) | < 5 KB/s per pemain | Event aksi kecil |
| Total parts per farm | < 5.000 parts | Dalam pedoman performa Roblox |
| Jumlah partikel | < 500 partikel aktif | Emitter dioptimalkan dengan batas laju |
| Waktu eksekusi skrip (server) | < 5ms per tick pada heartbeat | Menyisakan ruang untuk overhead engine Roblox |
| Operasi DataStore | < 60 + 10 per pemain per menit | Jauh dalam batas Roblox |

---

## 10. Anti-Cheat & Validasi

### 10.1 Aturan Validasi Server

Semua event klien-ke-server harus melewati validasi:
- Cooldown aksi ditegakkan (tidak boleh panen spam cepat)
- Kepemilikan sumber daya diperiksa (tidak dapat mengubah farm pemain lain)
- Rentang parameter divalidasi (tidak dapat mengatur pH ke 100)
- Integritas transaksi (tidak dapat menghabiskan kredit yang tidak dimiliki)
- Bahan resep diverifikasi (tidak dapat crafting tanpa item yang dibutuhkan)
- Akselerasi waktu dibatasi laju per sesi

### 10.2 Mitigasi Eksploitasi Umum

| Eksploitasi | Mitigasi |
|---------|-----------|
| Speed hacking | Server memvalidasi cooldown aksi |
| Injeksi kredit | Server adalah otoritas tunggal saldo kredit |
| Manipulasi parameter | Semua simulasi di server; klien hanya menampilkan |
| Duplikasi | ID unik untuk semua entitas; server melacak pembuatan |
| Teleport ke area terlarang | Pemeriksaan batas zona di server |
| Injeksi skrip | Filtering standar Roblox; tidak ada penggunaan `loadstring` |

---

## 11. Arsitektur Multiplayer Co-Op (Pasca-Peluncuran)

### 11.1 Model Berbagi Farm

- Setiap pemain memiliki farm sendiri (lahan privat)
- Lahan bersebelahan dapat "ditautkan" untuk perdagangan sumber daya
- Sumber daya bersama: kompos komunitas, batch EE lebih besar, fasilitas BSF bersama
- Papan peringkat: skor Loop Health kooperatif

### 11.2 Model Kepercayaan

- Farm setiap pemain disimulasikan secara independen di server
- Sumber daya bersama memiliki "pelacakan kontribusi" (siapa menambah apa)
- Perdagangan: pemain A menawarkan sumber daya → pemain B menerima → server memvalidasi dan mentransfer
- Tidak ada modifikasi langsung subsistem pemain lain

---

## 12. Strategi Pengujian

### 12.1 Pengujian Unit (Luau)

```lua
-- Contoh struktur pengujian menggunakan TestService
-- Tes untuk formula simulasi
test("Kalkulasi ABW dengan 20 ikan pada 5g dengan FR 6%", function()
    local hasil = calculateDailyFeed(20, 5, 0.06)
    assertEquals(hasil, 6) -- 20 * 5 * 0.06 = 6 gram
end)

test("Penurunan pH dari akumulasi amonia", function()
    local waterState = { pH = 7.5, amonia = 0.1 }
    simulateAmmoniaBuildup(waterState, 6) -- 6 jam
    assert(waterState.pH < 7.5)
    assert(waterState.amonia > 0.1)
end)
```

### 12.2 Pengujian Integrasi

- Simulasikan siklus 75 hari game penuh dalam mode otomatis → verifikasi milestone pertumbuhan
- Injeksi kondisi klinis → verifikasi deteksi + hasil pengobatan
- Stress test: 10 pemain bersamaan dengan subsistem maksimum

### 12.3 Milestone Playtesting

| Fase | Fokus | Durasi |
|-------|-------|----------|
| Alpha (internal) | Akurasi simulasi inti, perbaikan bug | 4 minggu |
| Alpha (edukator) | 5–10 guru menguji mode kelas | 2 minggu |
| Beta (tertutup) | 100–500 pemain, semua mode | 4 minggu |
| Beta (terbuka) | Beta publik, pengujian monetisasi | 2 minggu |
| Peluncuran | Rilis penuh | — |

---

*Dokumen Berikutnya: 04-Kerangka-Edukasi.md — Kerangka Pendidikan & Asesmen*
