# 15 — ERROR HANDLING & DISASTER RECOVERY

> **Fungsi:** Semua "what if" yang harus ditangani. Apa yang terjadi kalau DataStore gagal? Kalau player disconnect saat crafting? Kalau parameter corruption? Dokumen ini adalah safety net.

---

## 1. Error Categories

| Kategori | Contoh | Dampak |
|----------|--------|--------|
| **Network** | DataStore timeout, RemoteEvent loss, MemoryStore failure | Progres tidak tersimpan, state tidak sync |
| **Data** | Schema mismatch, data corruption, save overflow | Data rusak, pemain kehilangan progres |
| **Logic** | Division by zero, nil reference, infinite loop | Server crash, instance freeze |
| **Client** | Disconnect, low memory, device crash | Kehilangan sesi, crafting terputus |
| **Platform** | Roblox outage, API deprecation, update breaking changes | Game tidak bisa diakses |

---

## 2. DataStore Error Handling

### 2.1 Retry Strategy

```lua
-- DataStoreManager.server.lua
local MAX_RETRIES = 3
local RETRY_DELAY = 2  -- detik

function DataStoreManager:SaveWithRetry(playerId, data)
    for attempt = 1, MAX_RETRIES do
        local success, result = pcall(function()
            return self.dataStore:SetAsync("player_" .. playerId, data)
        end)

        if success then
            return true
        end

        warn(string.format(
            "DataStore save failed (attempt %d/%d): %s",
            attempt, MAX_RETRIES, tostring(result)
        ))

        if attempt < MAX_RETRIES then
            task.wait(RETRY_DELAY * attempt)  -- exponential backoff
        end
    end

    -- Semua retry gagal → simpan di memory cache + log error
    self.memoryCache[playerId] = data
    self:LogCriticalError("DataStoreSaveFailed", playerId, data)
    return false
end
```

### 2.2 Fallback Behavior

| Skenario | Fallback |
|----------|----------|
| `GetAsync` gagal (first-time player) | Return `_getDefaultData()` — pemain baru |
| `GetAsync` gagal (returning player) | Gunakan `memoryCache` jika ada. Jika tidak → **jangan overwrite**, minta pemain rejoin |
| `SetAsync` gagal (3x retry exhausted) | Simpan di `memoryCache`. Coba lagi di tick berikutnya. Log error. |
| `UpdateAsync` gagal | Rollback ke nilai sebelumnya. Jangan partial update. |
| DataStore budget exceeded | Queue save requests. Proses satu per satu. |

### 2.3 Data Corruption Recovery

```lua
function DataStoreManager:LoadWithValidation(playerId)
    local success, rawData = pcall(function()
        return self.dataStore:GetAsync("player_" .. playerId)
    end)

    if not success then
        return self:_handleLoadFailure(playerId, rawData)
    end

    -- Validasi struktur
    if not self:_validateSchema(rawData) then
        warn("Data corruption detected for player", playerId)
        return self:_recoverCorruptedData(playerId, rawData)
    end

    -- Migrasi version lama
    if rawData.saveVersion < SAVE_VERSION then
        rawData = self:_migrateData(rawData)
    end

    return rawData
end

function DataStoreManager:_validateSchema(data): boolean
    -- Cek field wajib ada
    if type(data) ~= "table" then return false end
    if data.playerId == nil then return false end
    if data.credits == nil then return false end
    if data.leleGallons == nil then return false end
    -- ... validasi field wajib lainnya
    return true
end

function DataStoreManager:_recoverCorruptedData(playerId, rawData)
    -- Strategi recovery: pertahankan field yang valid, reset field korup

    local recovered = self:_getDefaultData()
    recovered.playerId = playerId

    -- Pertahankan field yang masih valid
    if type(rawData) == "table" then
        if type(rawData.credits) == "number" then
            recovered.credits = rawData.credits  -- pulihkan kredit
        end
        if type(rawData.achievements) == "table" then
            recovered.achievements = rawData.achievements  -- pulihkan achievements
        end
        -- Field lain di-reset ke default
    end

    return recovered
end
```

---

## 3. Client Disconnect Handling

### 3.1 Saat Disconnect

| Situasi | Handling |
|---------|----------|
| Disconnect saat idle | Auto-save state terakhir. Offline progression diterapkan saat rejoin. |
| Disconnect saat crafting | Crafting job disimpan dengan `status="fermenting"`. Timer jalan normal via offline progression. |
| Disconnect saat clinical case aktif | Case dibatalkan — tidak ada penalti. Pemain bisa diagnosis ulang setelah rejoin. |
| Disconnect saat transaksi ekonomi | Transaksi di-rollback jika belum complete. `EconomyManager` gunakan atomic write. |

### 3.2 Session Recovery

```lua
-- Saat player rejoin
function OnPlayerJoin(player)
    local data = DataStoreManager:LoadWithValidation(player.UserId)

    -- Terapkan offline progression
    local catchup = TimeManager:CalculateOfflineProgress(data)
    if catchup then
        -- Tampilkan notifikasi catch-up ke client
        CatchupNotification:FireClient(player, {
            offlineHours = catchup.offlineHours,
            messages = catchup.messages,
        })
    end

    -- Kirim full state sync
    SyncState:FireClient(player, data)
end
```

---

## 4. Runtime Error Handling

### 4.1 Server-Side Error Boundaries

Setiap module wajib punya error boundary:

```lua
-- SimulationEngine/Init.server.lua
local function safeTick()
    local success, err = pcall(function()
        LeleBioflok:Tick(deltaHours)
    end)
    if not success then
        warn("LeleBioflok tick failed:", err)
        ErrorLogger:Log("LeleBioflokTickError", err)
        -- Jangan propagate error — subsystem lain harus tetap jalan
    end
end
```

### 4.2 Edge Cases per Subsistem

| Subsistem | Edge Case | Handling |
|-----------|-----------|----------|
| **Lele** | Semua ikan mati | Galon tetap ada tapi kosong. Player harus beli benih baru. Tampilkan pesan "Semua ikan mati. Belajar dari ini, Ninja." |
| **Lele** | Parameter di luar range (pH = -1) | Clamp ke batas fisika (0–14). Log error untuk investigasi. |
| **Lele** | Pakan = 0 gram (lupa feeding) | Ikan tidak mati langsung. Health turun gradual. Alert setelah 2 hari tanpa pakan. |
| **Tanaman** | Semua tanaman mati | Bedengan tetap ada. Soil tetap hidup. Player harus tanam ulang. |
| **BSF** | Semua larva mati | Biopond kosong. Player harus beli telur BSF baru. |
| **Ayam** | Semua ayam mati | Kandang kosong. Player beli DOC baru. |
| **Komposter** | Tidak pernah diputar | Dekomposisi lambat (50% speed). Tidak gagal — hanya lebih lama. |
| **EE** | Kontaminasi (lupa burp bulan pertama) | Batch gagal. Bau busuk. Player harus buang dan mulai ulang. |
| **Ekonomi** | Kredit negatif | Tidak mungkin. Semua transaksi cek saldo dulu. |
| **Crafting** | Bahan tidak cukup | Crafting tidak bisa dimulai. Tampilkan bahan yang kurang. |

### 4.3 Division by Zero Prevention

```lua
-- Di semua kalkulasi yang melibatkan pembagian:
function safeDivide(numerator, denominator, fallback)
    if denominator == 0 or denominator ~= denominator then  -- NaN check
        return fallback
    end
    return numerator / denominator
end

-- Contoh penggunaan:
local ratio = safeDivide(nitrogenInput, carbonLayer, 0)
```

---

## 5. Roblox Platform Issues

| Issue | Detection | Handling |
|-------|-----------|----------|
| **DataStore outage** | `pcall` gagal 3x berturut | Notifikasi ke player: "Server penyimpanan sedang sibuk. Progres Anda aman di memori. Coba lagi nanti." Simpan di memory cache. |
| **MessagingService down** | `pcall` gagal | Multiplayer features dinonaktifkan graceful. Solo play tetap berfungsi. |
| **MemoryStore timeout** | Timeout error | Fallback ke DataStore untuk leaderboard. |
| **Roblox global outage** | HTTP 503 | Game tetap playable (semua simulasi server-side). Hanya save yang tertunda. |

---

## 6. Rollback Strategy

### 6.1 Kapan Rollback Diperlukan

| Situasi | Tindakan |
|---------|----------|
| Bug ekonomi → player dapat kredit tidak sah | Rollback ekonomi player yang terpengaruh. Beri kompensasi 100 Kredit + pesan apology. |
| Data corruption masal | Restore dari backup terakhir (data disimpan dengan `saveVersion`). |
| Update merusak save | Migrasi data via `MIGRATIONS` table. Kalau gagal → fallback ke default untuk field baru. |

### 6.2 Rollback Procedure

```
1. IDENTIFIKASI: Player mana yang terpengaruh? (query log)
2. BACKUP: Simpan data korup sebagai backup_{playerId}_{timestamp}
3. ROLLBACK: Overwrite dengan data terakhir yang valid
4. KOMPENSASI: Beri player kredit/gratis item
5. KOMUNIKASI: Kirim pesan in-game ke player yang terpengaruh
6. RC: Root cause analysis → fix bug → test → deploy
```

---

## 7. Monitoring & Alerting

### 7.1 Key Metrics

| Metric | Cara Monitor | Alert Threshold |
|--------|-------------|-----------------|
| DataStore error rate | `pcall` failure count | >5% per hour |
| Save latency | `os.clock()` delta | >3 detik |
| Server tick time | `workspace:GetServerTimeNow()` | >10ms per tick |
| Client disconnect rate | `Players.PlayerRemoving` count | >20% per hour |
| Memory usage | `Stats:GetTotalMemoryUsageMb()` | >400MB |
| Error log spike | `ErrorLogger` count | >50 errors per hour |

### 7.2 Error Logger

```lua
-- ErrorLogger.server.lua
local ErrorLogger = {}
local errorLog = {}

function ErrorLogger.Log(category, message, data)
    local entry = {
        timestamp = os.time(),
        category = category,
        message = tostring(message),
        data = data,
    }
    table.insert(errorLog, entry)

    -- Batasi ukuran log (ring buffer)
    if #errorLog > 1000 then
        table.remove(errorLog, 1)
    end

    -- Log ke Roblox console
    warn(string.format("[%s] %s", category, message))

    -- Opsional: kirim ke external analytics
    -- HttpService:PostAsync(webhookUrl, HttpService:JSONEncode(entry))
end

function ErrorLogger.GetRecentErrors(count)
    local start = math.max(1, #errorLog - count)
    return { unpack(errorLog, start, #errorLog) }
end

return ErrorLogger
```

---

## 8. Disaster Recovery Runbook

### Skenario 1: DataStore Corrupt

```
1. Deteksi: _validateSchema() return false
2. Isolasi: Tandai playerId sebagai "corrupted"
3. Recovery: Jalankan _recoverCorruptedData()
4. Verifikasi: Cek field kritis (credits, achievements) pulih
5. Komunikasi: Tampilkan pesan "Data kamu mengalami masalah kecil. Beberapa progres telah dipulihkan."
```

### Skenario 2: Memory Leak

```
1. Deteksi: Memory usage >400MB dan naik terus
2. Investigasi: Jalankan garbage collection (`collectgarbage("collect")`)
3. Mitigasi: Restart server jika memory >500MB selama >5 menit
4. Pencegahan: Audit object lifecycle — pastikan semua Instance di-destroy
```

### Skenario 3: Infinite Loop

```
1. Deteksi: Server tick time >100ms dan naik
2. Investigasi: Cek error log, identifikasi module penyebab
3. Mitigasi: Disable module yang bermasalah. Subsystem lain tetap jalan.
4. Fix: Root cause → perbaiki loop condition
```

---

*Dokumen Berikutnya: 16-Build-Release.md — Pipeline Build & Rilis*
