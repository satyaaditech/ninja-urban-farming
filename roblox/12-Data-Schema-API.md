# 12 — DATA SCHEMA & API CONTRACT

> **Fungsi:** Kontrak antara logika server dan client. Semua programmer menggunakan dokumen ini sebagai referensi tunggal. Setiap perubahan harus diperbarui di sini.

---

## 1. DataStore Schema

### 1.1 Player Data (Key: `player_{userId}`)

```lua
-- Types.lua (ReplicatedStorage/Shared/)
export type PlayerData = {
    -- === META ===
    playerId: number,
    saveVersion: number,              -- inkrementasi setiap schema berubah
    lastSaved: number,                -- os.time()
    lastLogoutTimestamp: number,      -- os.time() saat logout (untuk offline progression)
    totalPlayTime: number,            -- detik real-time
    gameMode: "story" | "sandbox" | "classroom",
    storyChapter: number,             -- 0–16
    tutorialCompleted: boolean,
    tutorialTimeSkipsUsed: number,    -- max 3 (tutorial only)

    -- === EKONOMI ===
    credits: number,                  -- default: 100
    totalEarned: number,
    totalSpent: number,

    -- === LELE BIOFLOK ===
    leleGallons: {
        [number]: {                   -- index: 1, 2, 3
            active: boolean,
            waterState: WaterState,
            fishArray: { Fish },
            feedHistory: { FeedRecord },
            clinicalHistory: { ClinicalRecord },
        }
    },

    -- === BSF MAGGOT ===
    bsfState: BSFColonyState | nil,
    bsfHarvestedTotal_g: number,

    -- === AYAM PETELUR ===
    chickenState: ChickenColonyState | nil,
    totalEggsCollected: number,
    deepLitterState: DeepLitterState | nil,

    -- === RAISED BEDS ===
    raisedBeds: {
        [number]: {                   -- index: 1–4
            active: boolean,
            soilState: SoilState,
            plantData: PlantData | nil,
            diseaseHistory: { DiseaseRecord },
        }
    },

    -- === KOMPOSTER & EE ===
    composters: { [number]: ComposterState },
    eeBatches: { [string]: EEState },  -- key: batchId

    -- === INVENTORI ===
    inventory: { [string]: number },   -- key: itemId, value: quantity

    -- === EM4 ===
    emActiveState: EMActiveState | nil,

    -- === BOOSTER CRAFTING ===
    craftingQueue: { CraftingJob },

    -- === TATA LETAK ===
    zonePlacement: ZonePlacementData,

    -- === PROGRES ===
    achievements: { [string]: boolean },
    clinicalCasesSolved: number,
    clinicalAccuracy: number,         -- 0.0–1.0
    loopHealthHistory: { number },
    certifications: {
        [string]: {
            passed: boolean,
            score: number,
            date: number,
        }
    },
    playerLevel: number,              -- 1–30
    playerTitle: string,

    -- === PENGATURAN ===
    language: "id" | "en",
    accessibilityMode: "default" | "simplified" | "colorblind" | "tts",
    audioVolume: {
        master: number,
        music: number,
        sfx: number,
        ambient: number,
    },
}
```

### 1.2 Sub-Types

```lua
export type WaterState = {
    volume_L: number,                 -- max 15
    temperature_C: number,
    pH: number,                       -- 0–14, ideal 7.0–8.0
    dissolvedO2_mgL: number,
    ammonia_NH3_mgL: number,
    nitrite_NO2_mgL: number,
    nitrate_NO3_mgL: number,
    totalSuspendedSolids_mgL: number,
    flocMaturity: number,             -- 0.0–1.0
    alkalinity_mgL: number,
    microbialActivity: number,        -- 0.0–1.0
    salinity_gL: number,              -- affected by salt additions
    diseaseCheckSuspended: boolean,   -- untuk offline progression
}

export type Fish = {
    id: string,                       -- GUID
    length_cm: number,
    weight_g: number,
    phase: "starter" | "grower" | "finisher",
    health: number,                   -- 0.0–1.0
    stressLevel: number,              -- 0.0–1.0
    feedingEfficiency: number,        -- 0.0–1.0
    diseaseStatus: string | nil,
    daysInTank: number,
}

export type SoilState = {
    pH: number,
    nitrogen_N: number,               -- mg/kg
    phosphorus_P: number,             -- mg/kg
    potassium_K: number,              -- mg/kg
    calcium_Ca: number,               -- mg/kg
    magnesium_Mg: number,             -- mg/kg
    iron_Fe: number,                  -- mg/kg
    organicMatter_percent: number,
    moisture_percent: number,
    temperature_C: number,
    CEC_meq100g: number,
    microbialActivity: number,        -- 0.0–1.0 (relatif, bukan CFU absolut)
    compaction: number,               -- 0.0–1.0
    humicAcid_content: number,        -- 0.0–1.0
    diseasePressure: { [string]: number },
    pestPressure: { [string]: number },
    pestCheckSuspended: boolean,      -- untuk offline progression
}

export type PlantData = {
    species: string,
    growthStage: string,
    daysSincePlanting: number,
    health: number,                   -- 0.0–1.0
    deficiencyLevels: {               -- 0.0–1.0 per nutrient
        N: number,
        P: number,
        K: number,
        Ca: number,
        Mg: number,
        Fe: number,
        waterExcess: number,
        waterDeficit: number,
    },
    diseaseStatus: string | nil,
    pestInfestation: { [string]: number },
    yield_grams: number,
    quality: number,                  -- 0.0–1.0
    harvestCount: number,             -- untuk tanaman regrowth
}

export type BSFColonyState = {
    eggs_count: number,
    larvae_count: number,
    larvae_totalWeight_g: number,
    prepupae_count: number,
    pupae_count: number,
    adultFlies_count: number,
    adultAge_hours: number,
    colonyHealth: number,
    substrateMoisture: number,
    substrateCNRatio: number,
    odorLevel: number,
}

export type ChickenColonyState = {
    chickens: { Chicken },
    feedComposition: {
        commercial_percent: number,   -- default: 50
        vegetable_percent: number,    -- default: 25
        maggot_percent: number,       -- default: 25
    },
}

export type Chicken = {
    id: string,
    breed: "kampung" | "petelur",
    age_days: number,
    health: number,
    hunger: number,
    eggProductionRate: number,
    eggQuality: number,
    stressLevel: number,
}

export type DeepLitterState = {
    depth_cm: number,
    carbonLayer_cm: number,
    nitrogenInput_g: number,
    moisture_percent: number,
    temperature_C: number,
    decompositionRate: number,
    compostMaturity: number,          -- 0.0–1.0 (siap panen di 1.0)
    odorLevel: number,
    microbeActivity: number,
}

export type ComposterState = {
    organicMass_kg: number,
    carbonRich_kg: number,
    nitrogenRich_kg: number,
    CN_ratio: number,
    moisture_percent: number,
    temperature_C: number,
    aerationLevel: number,
    maturity: number,
    eeApplied: boolean,
    daysActive: number,
}

export type EEState = {
    batchId: string,
    fruitPeels_kg: number,
    brownSugar_kg: number,
    water_L: number,
    ratio: string,                    -- "3:1:10"
    fermentationDays: number,
    maturity: number,
    pH: number,
    volume_L: number,
    quality: "basic" | "mature" | "aged",
}

export type EMActiveState = {
    starterEM4_mL: number,
    molasses_mL: number,
    water_L: number,
    fermentationDays: number,
    maturity: number,
    pH: number,
    volume_L: number,
    quality: "failed" | "active" | "potent",
}

export type CraftingJob = {
    [string]: {                       -- jobId
        recipeId: string,
        startDay: number,
        fermentationDays: number,
        completeDay: number,
        status: "fermenting" | "complete" | "failed",
        ingredients: { [string]: number },
    }
}

export type ZonePlacementData = {
    zone1Buildings: { [string]: CFrame },  -- posisi setiap objek
    zone2Buildings: { [string]: CFrame },
}
```

---

## 2. RemoteEvent Contract

### 2.1 Client → Server

| Event Name | Parameter | Return | Rate Limit | Validasi |
|-----------|-----------|--------|------------|----------|
| `PerformAction` | `{ action: string, targetId: string, params: {} }` | `{ success: boolean, message: string, data: {} }` | 1 per 0.5s | Target ownership, action cooldown |
| `CraftRecipe` | `{ recipeId: string }` | `{ success: boolean, jobId: string }` | 1 per 2s | Ingredients check, crafting station active |
| `SubmitDiagnosis` | `{ gallonIndex: number, diagnosis: string, treatments: {string} }` | `{ success: boolean, score: number, report: ClinicalReport }` | 1 per 5s | Valid gallon, valid diagnosis IDs |
| `PurchaseItem` | `{ itemId: string, quantity: number }` | `{ success: boolean, newBalance: number }` | 1 per 1s | Credit check |
| `ConfigurePlacement` | `{ zoneData: ZonePlacementData }` | `{ success: boolean }` | 1 per 10s | Bounds check, overlap check |
| `SetTimeScale` | `{ scale: number }` | `{ success: boolean }` | 1 per 5s | Max scale 4x, no crisis mode skip |
| `RequestTimeSkip` | `{ targetDay: number }` | `{ success: boolean, daysSkipped: number }` | Tutorial only (max 3) | Token check, tutorial phase check |

**Contoh `PerformAction.params`:**

```lua
-- Flush gallon
{ action = "flush", targetId = "gallon_1", params = { percent = 50 } }

-- Feed fish
{ action = "feed", targetId = "gallon_1", params = { grams = 6.6, bibisStatus = "complete" } }

-- Harvest plant
{ action = "harvest", targetId = "bed_1" }

-- Collect eggs
{ action = "collect_eggs", targetId = "chicken_coop" }

-- Ninja sampling
{ action = "sample_fish", targetId = "gallon_1", params = { fishCount = 5 } }

-- Apply treatment
{ action = "treat_fish", targetId = "gallon_1", params = { treatments = {"fast", "flush", "salt"} } }
```

### 2.2 Server → Client

| Event Name | Parameter | Frekuensi | Notes |
|-----------|-----------|-----------|-------|
| `SyncState` | `PlayerData` (full) | Once on join | Gunakan compression jika data >4KB |
| `StateDelta` | `{ changes: {} }` | Every 30s tick | Hanya field yang berubah |
| `ClinicalAlert` | `{ alertId: string, gallonIndex: number, symptoms: {string}, urgency: "low" | "medium" | "critical" }` | On clinical trigger | Paksa buka modal diagnosis |
| `TimeUpdate` | `{ gameDay: number, gameHour: number, dayPhase: string }` | Every 10s | Untuk HUD clock |
| `AchievementUnlocked` | `{ achievementId: string, title: string }` | On achievement | Popup + fanfare |
| `CatchupNotification` | `{ offlineHours: number, messages: {string} }` | Once on login | Offline progression summary |
| `MentorDialogue` | `{ dialogueId: string, text: string, choices: {string} }` | Story mode trigger | NPC interaction |
| `LoopHealthUpdate` | `{ score: number, breakdown: {} }` | Every 5 min | Dashboard update |

### 2.3 RemoteFunction (Request-Response)

| Function Name | Parameter | Return | Notes |
|--------------|-----------|--------|-------|
| `GetDiagnosisOptions` | `{ gallonIndex: number }` | `{ options: {DiagnosisOption} }` | Valid diagnoses based on current state |
| `GetRecipeDetails` | `{ recipeId: string }` | `RecipeDetail` | Full recipe including ingredient availability |
| `GetClassroomAssignments` | `{ classId: string }` | `{ assignments: {Assignment} }` | Teacher mode only |

---

## 3. BindableEvent (Internal Server)

Digunakan untuk komunikasi antar module di server:

| Event Name | Source Module | Target Module | Parameter |
|-----------|--------------|---------------|-----------|
| `DayChanged` | TimeManager | All simulation engines | `{ newDay: number }` |
| `HourChanged` | TimeManager | Day/night cycle | `{ newHour: number, dayPhase: string }` |
| `WeatherChanged` | TimeManager | All systems | `{ weather: string, intensity: number }` |
| `ClinicalCaseTriggered` | DiseaseEngine | AlertSystem | `{ case: ClinicalCase }` |
| `EconomyTransaction` | Any | EconomyManager | `{ type: "credit" | "debit", amount: number, source: string }` |
| `ResourceFlowed` | Any | ClosedLoopTracker | `{ from: string, to: string, resource: string, quantity: number }` |

---

## 4. MemoryStoreService (Live State)

Untuk data yang tidak perlu dipersistensi permanen:

| Key Pattern | Content | TTL |
|------------|---------|-----|
| `server_{serverId}_players` | Active player list | Session |
| `classroom_{classId}_assignments` | Active assignments cache | 1 hour |
| `leaderboard_loop_health` | Top 100 scores | 30 min |

---

## 5. MessagingService (Cross-Server)

Untuk multiplayer co-op (future):

| Topic | Message | Notes |
|-------|---------|-------|
| `FarmTrade_{serverId}` | `{ fromPlayer: number, toPlayer: number, offer: {}, status: string }` | Resource trading |
| `FarmVisit_{serverId}` | `{ visitorId: number, farmOwnerId: number }` | Social visits |

---

## 6. DataStore Budget

| Operation | Estimated Size | Frequency | Budget Usage |
|-----------|---------------|-----------|--------------|
| Player save (full) | ~4 KB | Every 5 min + on leave | ~50 req/player/hour |
| Player save (delta) | ~500 B | Every 30s tick | ~120 req/player/hour |
| Leaderboard update | ~200 B | Every 30 min | 2 req/player/hour |

**Budget Roblox:** 60 + (10 × playerCount) requests per minute.
**Proyeksi penggunaan:** <50% budget pada 10 concurrent players. Aman.

---

## 7. Versioning & Migration

```lua
local SAVE_VERSION = 1  -- increment setiap schema berubah

local MIGRATIONS = {
    [1] = function(data)
        -- v1 ke v2: tambah field baru dengan default
        if data.deficiencyHistory == nil then
            data.deficiencyHistory = {}
        end
        data.saveVersion = 2
        return data
    end,
    -- Tambah migration function baru di sini saat schema berubah
}
```

---

*Dokumen Berikutnya: 13-Coding-Standards.md — Konvensi Kode & PR Template*
