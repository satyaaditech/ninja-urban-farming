# 13 — CODING STANDARDS & CONVENTIONS

> **Target:** Solo developer + AI assistant. Standar ini memastikan kode konsisten — terutama saat AI (opencode) membantu menulis kode. Tanpa standar, kode hasil AI dan kode manual akan bentrok gaya.

---

## 1. Luau Configuration

### 1.1 Strict Mode

Semua file `.lua` dan `.server.lua` / `.client.lua` WAJIB menggunakan strict mode:

```lua
--!strict
```

**Alasan:** Type checking mencegah 40% bug umum (nil access, type mismatch) sebelum runtime.

### 1.2 Type Definitions

Semua tipe kompleks didefinisikan di `ReplicatedStorage/Shared/Types.lua`:

```lua
-- Types.lua
export type WaterState = {
    volume_L: number,
    pH: number,
    -- ...
}

return {}
```

Module lain mengimpor tipe:

```lua
local Types = require(ReplicatedStorage.Shared.Types)
type WaterState = Types.WaterState
```

---

## 2. Naming Conventions

| Element | Convention | Contoh |
|---------|-----------|--------|
| **ModuleScript** | PascalCase | `WaterChemistry.lua`, `FishGrowth.lua` |
| **Local variable** | camelCase | `local waterState`, `local fishCount` |
| **Function (local)** | camelCase | `local function calculatePH()` |
| **Function (module export)** | camelCase | `WaterChemistry.calculatePH()` |
| **Constant** | UPPER_SNAKE_CASE | `local MAX_FISH_PER_GALLON = 20` |
| **RemoteEvent** | PascalCase (verb) | `PerformAction`, `SyncState` |
| **Bool variable** | is/has/should prefix | `local isActive`, `local hasDisease` |
| **Module table** | PascalCase (noun) | `local WaterChemistry = {}` |
| **Enum-like string** | snake_case | `"ammonia_stress"`, `"layu_fusarium"` |
| **Private function** | _camelCase prefix | `local function _internalHelper()` |

---

## 3. File Structure Template

Setiap ModuleScript mengikuti template ini:

```lua
--!strict

-- === HEADER ===
-- Module: WaterChemistry.server.lua
-- Author: [nama]
-- Description: Menghitung perubahan parameter kimia air per tick simulasi
-- Dependencies: Constants.lua, Types.lua
-- Last Modified: 2026-07-04

-- === IMPORTS ===
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Shared = ReplicatedStorage:WaitForChild("Shared")
local Constants = require(Shared:WaitForChild("Constants"))
local Types = require(Shared:WaitForChild("Types"))

-- === TYPE IMPORTS ===
type WaterState = Types.WaterState
type Fish = Types.Fish

-- === CONSTANTS ===
local NH3_TOXIC_THRESHOLD = Constants.Water.NH3_TOXIC_THRESHOLD
local DEFAULT_TEMPERATURE = 28

-- === MODULE TABLE ===
local WaterChemistry = {}

-- === PUBLIC FUNCTIONS ===

-- Menghitung perubahan pH dalam satu tick simulasi
function WaterChemistry.calculatePHChange(
    currentState: WaterState,
    fishArray: { Fish },
    deltaHours: number
): number
    -- implementasi
    return 0
end

-- === PRIVATE FUNCTIONS ===

local function _validatePH(value: number): boolean
    return value >= 0 and value <= 14
end

-- === RETURN ===
return WaterChemistry
```

---

## 4. Server-Client Separation

| Folder | Boleh di `require()` oleh | Isi |
|--------|--------------------------|-----|
| `ServerScriptService/` | Server scripts ONLY | Logika simulasi, DataStore, ekonomi |
| `StarterPlayer/StarterPlayerScripts/` | Client scripts ONLY | Input, kamera, haptic |
| `StarterGui/` | Client scripts ONLY | UI, HUD, panel |
| `ReplicatedStorage/Shared/` | Server AND Client | Types, Constants, Formulas (pure functions) |

**Aturan Emas:** Shared modules HANYA berisi pure functions + data. Tidak boleh ada side effect (DataStore access, Instance creation, RemoteEvent fire).

---

## 5. Remote Communication Pattern

```lua
-- === SERVER: Event Handler ===
local PerformAction = ReplicatedStorage.Remotes:WaitForChild("PerformAction")

PerformAction.OnServerEvent:Connect(function(player, request)
    -- 1. VALIDASI
    if not _validateRequest(player, request) then
        return _sendError(player, "Invalid request")
    end

    -- 2. COOLDOWN CHECK
    if not _checkCooldown(player, request.action) then
        return _sendError(player, "Action on cooldown")
    end

    -- 3. EXECUTE
    local result = _executeAction(player, request)

    -- 4. RESPOND
    _sendResult(player, result)
end)

-- === CLIENT: Event Caller ===
local function performAction(action, targetId, params)
    PerformAction:FireServer({
        action = action,
        targetId = targetId,
        params = params or {},
    })
end
```

---

## 6. Error Handling Pattern

```lua
-- Gunakan pcall untuk operasi yang bisa gagal
local success, result = pcall(function()
    return DataStore:GetAsync(key)
end)

if not success then
    warn("DataStore read failed for key:", key, "Error:", result)
    return _getDefaultData()  -- fallback
end

-- Jangan pernah throw error ke client
-- Server selalu return { success: boolean, message: string, data: {} }
```

---

## 7. Comment Conventions

```lua
-- Gunakan -- untuk komentar singkat (satu baris)
-- Jangan komentar yang menyatakan hal obvious:
-- ❌ local x = 5  -- set x ke 5
-- ✅ local MAX_RETRY = 5  -- batas retry DataStore sebelum fallback

-- Gunakan --[=[ ... ]=] untuk komentar panjang (multi-baris)
--[=[
    Algoritma pertumbuhan ikan:
    1. Hitung efisiensi pakan dari kualitas air
    2. Terapkan formula ABW baru
    3. Periksa transisi fase
    4. Evaluasi risiko penyakit
]=]

-- Gunakan TODO untuk technical debt (disertai nama dan tanggal)
-- TODO(satya 2026-07-04): Implementasikan sampling setiap 10 hari
```

---

## 8. Performance Rules

| Aturan | Alasan |
|--------|--------|
| Hindari loop di `Heartbeat` | 60x/detik — setiap ms mahal |
| Jangan `WaitForChild()` di loop | Cache reference sekali di init |
| Gunakan `table.create()` untuk array besar | 3x lebih cepat dari `{}` |
| Batch DataStore write | Jangan write setiap tick — akumulasi dulu |
| `Debris:AddItem()` untuk cleanup | Jangan destroy manual dengan delay |
| Hindari `FindFirstChild()` di hot path | Cache atau gunakan `CollectionService` tags |
| ParticleEmitter rate dibatasi | Max 500 partikel aktif total |
| Gunakan `CFrame` untuk posisi | `Vector3` lebih lambat untuk transform |

---

## 9. Testing Convention

```lua
-- File: ServerScriptService/Tests/WaterChemistry.test.lua

return function()
    local WaterChemistry = require(script.Parent.Parent.WaterChemistry)

    describe("WaterChemistry", function()
        it("menghitung penurunan pH dari akumulasi amonia", function()
            local state = {
                pH = 7.5,
                ammonia_NH3_mgL = 0.8,
                dissolvedO2_mgL = 3.0,
                flocMaturity = 0.5,
                microbialActivity = 0.5,
            }
            local fishArray = {}
            local deltaHours = 6

            local deltaPH = WaterChemistry.calculatePHChange(state, fishArray, deltaHours)
            expect(deltaPH).to.be.a("number")
            expect(deltaPH).to.be.lessThan(0)  -- pH harus turun
        end)
    end)
end
```

---

## 10. PR Template (Untuk Review AI)

Karena development dilakukan solo + AI assistant, tidak ada PR formal — tapi setiap sesi AI yang menghasilkan kode harus mengikuti checklist ini:

```
## AI Code Review Checklist

### ✅ Sebelum commit, verifikasi:

- [ ] `--!strict` di baris pertama setiap file .lua
- [ ] Tidak ada `print()` — gunakan `warn()` untuk debugging
- [ ] Tidak ada hardcoded magic numbers — semua di Constants.lua
- [ ] Semua RemoteEvent/FireServer punya validasi server
- [ ] `pcall` untuk semua DataStore operation
- [ ] Tidak ada `while true do` tanpa `task.wait()`
- [ ] `require()` path benar (cek casing — case-sensitive di Roblox)
- [ ] Type annotations di semua function parameter & return
- [ ] Tidak ada shared module yang mengakses DataStore langsung
- [ ] StateDelta hanya berisi field yang BERUBAH (bukan full state)
```

---

## 11. Project Structure (Final)

```
ServerScriptService/
├── SimulationEngine/
│   ├── Init.server.lua
│   ├── TimeManager.server.lua
│   ├── LeleBioflok/
│   │   ├── WaterChemistry.lua
│   │   ├── FishGrowth.lua
│   │   ├── DiseaseEngine.lua
│   │   └── GallonManager.lua
│   ├── BSF_Maggot/
│   │   ├── Lifecycle.lua
│   │   ├── SubstrateManager.lua
│   │   └── HarvestSystem.lua
│   ├── AyamPetelur/
│   │   ├── ChickenBehavior.lua
│   │   ├── DeepLitter.lua
│   │   └── EggProduction.lua
│   ├── RaisedBed/
│   │   ├── SoilChemistry.lua
│   │   ├── PlantGrowth.lua
│   │   ├── PlantDisease.lua
│   │   ├── DeficiencyEngine.lua
│   │   └── PestSystem.lua
│   ├── KomposterEE/
│   │   ├── CompostEngine.lua
│   │   └── EcoEnzyme.lua
│   ├── OrganicBoosters/
│   │   ├── KBooster.lua
│   │   ├── AminorGrow.lua
│   │   ├── CalPhos.lua
│   │   ├── MagElixir.lua
│   │   ├── HumoNinja.lua
│   │   ├── JMS_IMO.lua
│   │   ├── HumicFulvic.lua
│   │   └── EM_Active.lua
│   ├── ClosedLoopTracker.lua
│   ├── EconomyManager.lua
│   ├── ClinicalCaseGenerator.lua
│   ├── OfflineProgression.lua
│   └── TimeSystem.lua
├── ServerCore/
│   ├── DataStoreManager.server.lua
│   ├── RemoteHandler.server.lua
│   ├── AntiCheat.server.lua
│   └── ErrorLogger.server.lua
└── Tests/
    ├── TestRunner.server.lua
    ├── LeleBioflok/
    └── RaisedBed/

ReplicatedStorage/
├── Remotes/
│   ├── PerformAction
│   ├── CraftRecipe
│   ├── SubmitDiagnosis
│   ├── PurchaseItem
│   ├── ConfigurePlacement
│   ├── SetTimeScale
│   ├── RequestTimeSkip
│   ├── SyncState
│   ├── StateDelta
│   ├── ClinicalAlert
│   ├── TimeUpdate
│   ├── AchievementUnlocked
│   ├── CatchupNotification
│   └── LoopHealthUpdate
└── Shared/
    ├── Types.lua
    ├── Constants.lua
    ├── Formulas.lua
    ├── DiseaseDatabase.lua
    ├── DeficiencyConfig.lua
    ├── RecipeDatabase.lua
    └── SpeciesConfig.lua

StarterPlayer/StarterPlayerScripts/
├── ClientInit.client.lua
├── InputManager.client.lua
├── CameraController.client.lua
└── HapticFeedback.client.lua

StarterGui/
├── GuiController.client.lua
├── HUD/
├── Panels/
├── Modals/
└── Components/
```

---

*Dokumen Berikutnya: 14-Testing-QA-Plan.md — Rencana Pengujian & QA*
