# 14 — TESTING & QA PLAN

> **Target:** Solo developer. Test case ini berfungsi sebagai checklist verifikasi manual. Setiap kali selesai membangun fitur, jalankan test case terkait sebelum melanjutkan.

---

## 1. Testing Levels

| Level | Frekuensi | Target |
|-------|-----------|--------|
| **Unit Test** | Setiap kali edit ModuleScript | Verifikasi fungsi individual (formula, kalkulasi) |
| **Integration Test** | Setiap selesai 1 subsistem | Verifikasi interaksi antar module |
| **System Test** | Setiap milestone fase | Verifikasi end-to-end: setup → operasi → panen |
| **Regression Test** | Sebelum pindah ke fase berikutnya | Verifikasi fitur lama tidak rusak oleh fitur baru |
| **Performance Test** | Setiap fase | Verifikasi FPS, memori, DataStore budget |

---

## 2. Unit Test Cases — Lele Bioflok

### 2.1 WaterChemistry.lua

| ID | Test Case | Input | Expected Output |
|----|-----------|-------|-----------------|
| `LELE-CHEM-001` | pH turun dari akumulasi amonia | `pH=7.5, NH3=1.0, DO=3.0, flocMaturity=0.5, deltaHours=6` | `deltaPH < 0` (pH turun) |
| `LELE-CHEM-002` | Amonia naik dari pakan tak termakan | `feedDecomposed=10g, fishMetabolicRate=0.02, density=18, flocMaturity=0.3, microbialActivity=0.3, DO=2.0, deltaHours=1` | `deltaNH3 > 0` (amonia naik) |
| `LELE-CHEM-003` | DO turun saat aerator mati | `aeratorOn=false, aeratorOutput=0, fishConsumption=0.01/density=18, microbialActivity=0.3, deltaHours=3` | `deltaDO < -2.0` (DO turun drastis) |
| `LELE-CHEM-004` | Flushing mengurangi NH3 | `NH3=0.8, flushPercent=50` | `newNH3 ≈ 0.4` |
| `LELE-CHEM-005` | Penambahan dolomit menaikkan pH | `pH=6.2` | `newpH ≈ 6.5` (max +0.3 per aplikasi) |
| `LELE-CHEM-006` | pH tidak bisa melebihi 8.5 | `pH=8.4` | `newpH = 8.5` (capped) |
| `LELE-CHEM-007` | Suhu >32°C menurunkan DO | `temperature_C=34, DO=5.0` | `DO turun lebih cepat dari normal` |

### 2.2 FishGrowth.lua

| ID | Test Case | Input | Expected Output |
|----|-----------|-------|-----------------|
| `LELE-FISH-001` | Kalkulasi pakan harian | `fishCount=20, ABW=5, FR=0.06` | `6 gram` (20 × 5 × 0.06) |
| `LELE-FISH-002` | Pembagian pakan pagi/sore | `totalFeed=6` | `pagi=2.4, sore=3.6` |
| `LELE-FISH-003` | ABW naik setelah 1 hari | `ABW=5, FR=0.06, feedingEff=0.8, stress=0.1` | `newABW > 5` |
| `LELE-FISH-004` | Ikan mati saat health <0.1 | `health=0.09, hoursInCriticalState=13` | `fish.alive = false` |
| `LELE-FISH-005` | Transisi fase | `ABW=8.5, phase="starter"` | `phase berubah ke "grower"` |
| `LELE-FISH-006` | Pemberian pakan kering → efisiensi turun 40% | `bibisStatus="none"` | `feedingEfficiency *= 0.6` |
| `LELE-FISH-007` | Pemberian pakan kering 3x → risiko kembung | `dryFeedStreak=3` | `bloatRisk = 0.25` |
| `LELE-FISH-008` | Kanibalisme monster | `fishA.weight_g=80, fishB.weight_g=5, sameGallon=true` | `fishB dimakan jika perbedaan >10x` |

### 2.3 DiseaseEngine.lua

| ID | Test Case | Input | Expected Output |
|----|-----------|-------|-----------------|
| `LELE-DIS-001` | Trigger Amonia Stress | `NH3=0.6, DO=2.5, hoursAboveThreshold=7` | `diseaseStatus = "ammonia_stress"` |
| `LELE-DIS-002` | Trigger Saprolegnia | `temperatureDrop=6°C in 1h, or pH<6.0 for 25h` | `diseaseStatus = "saprolegnia"` |
| `LELE-DIS-003` | Trigger Anoksia | `aeratorOff for >1h` | `diseaseStatus = "anoxia"` |
| `LELE-DIS-004` | Pengobatan benar → sukses | `correctDiagnosis=true, correctTreatment=true, delay=2h, criticalWindow=12h` | `successRate > 80%` |
| `LELE-DIS-005` | Pengobatan salah → gagal | `correctDiagnosis=false` | `successRate < 30%` |
| `LELE-DIS-006` | Pengobatan benar tapi terlambat | `correctDiagnosis=true, delay=10h, criticalWindow=12h` | `successRate < 50%` |

---

## 3. Unit Test Cases — Raised Beds

### 3.1 SoilChemistry.lua

| ID | Test Case | Input | Expected Output |
|----|-----------|-------|-----------------|
| `BED-SOIL-001` | Air lele menambah N tanah | `leleWater_N=50mg/L, volume=2L` | `soil.N meningkat` |
| `BED-SOIL-002` | pH tanah turun dari hujan | `rain_pH=5.6, heavyRain=true` | `soil.pH turun` |
| `BED-SOIL-003` | Abu kayu menaikkan pH | `soil.pH=5.0, ashApplied=2genggam` | `soil.pH naik ke 5.5+` |
| `BED-SOIL-004` | Biochar meningkatkan KTK | `biocharApplied=true, charged=true` | `soil.CEC +300%` |
| `BED-SOIL-005` | Kompos matang menambah semua nutrisi | `compostMaturity=1.0` | `N, P, K semua meningkat` |

### 3.2 PlantGrowth.lua

| ID | Test Case | Input | Expected Output |
|----|-----------|-------|-----------------|
| `BED-PLANT-001` | Tanaman tumbuh per hari | `species="kangkung", allFactors=1.0` | `daysSincePlanting +1, health stable` |
| `BED-PLANT-002` | Kangkung siap panen | `daysSincePlanting=25, species="kangkung"` | `growthStage = "siap_panen"` |
| `BED-PLANT-003` | Tomat butuh 75+ hari | `daysSincePlanting=70, species="tomat"` | `growthStage != "siap_panen"` |
| `BED-PLANT-004` | Tanaman mati tanpa air | `moisture=0.05, daysWithoutWater=5` | `health turun, death imminent` |
| `BED-PLANT-005` | Selada bolting jika >4 jam sun | `species="selada", directSunHours=6` | `boltingRisk naik, quality turun` |

### 3.3 DeficiencyEngine.lua

| ID | Test Case | Input | Expected Output |
|----|-----------|-------|-----------------|
| `BED-DEF-001` | Deteksi defisiensi N | `soil.N < plant.Nneed * 0.35` | `deficiencyLevels.N > 0` |
| `BED-DEF-002` | Defisiensi N → daun TUA kuning (shader) | `deficiencyLevels.N=0.7` | `oldLeafShader = "uniformYellow"` |
| `BED-DEF-003` | Defisiensi Mg → klorosis interveinal | `deficiencyLevels.Mg=0.7` | `oldLeafShader = "interveinalChlorosis"` |
| `BED-DEF-004` | Defisiensi Ca → daun MUDA keriting | `deficiencyLevels.Ca=0.7` | `newLeafShader = "curled"` |
| `BED-DEF-005` | Defisiensi Ca pada tomat → busuk ujung buah | `deficiencyLevels.Ca=0.7, species="tomat", isFruiting=true` | `fruitShader = "blossomEndRot"` |
| `BED-DEF-006` | Defisiensi Ca IRREVERSIBLE pada buah | `fruitAlreadyAffected=true, Ca corrected` | `buah yang sudah busuk TETAP busuk. Buah baru sehat.` |

---

## 4. Integration Test Cases

### 4.1 Closed-Loop Integration

| ID | Test Case | Expected Outcome |
|----|-----------|-----------------|
| `INT-LOOP-01` | Air lele → tanaman (full cycle) | Siram raised bed dengan air flush lele → soil N naik → tanaman tumbuh lebih cepat |
| `INT-LOOP-02` | Dapur → BSF → Ayam → Kompos (full cycle) | Sisa dapur ke biopond → maggot tumbuh → maggot ke ayam → telur meningkat → kotoran ayam ke komposter → kompos matang |
| `INT-LOOP-03` | Kompos → Tanah → Tanaman → Dapur (full cycle) | Kompos matang ke raised bed → soil health naik → tanaman panen → sisa ke dapur (loop tertutup) |
| `INT-LOOP-04` | Loop Health score kalkulasi | Semua resource flow tercatat → Loop Health > 60% achievable |

### 4.2 Clinical Integration

| ID | Test Case | Expected Outcome |
|----|-----------|-----------------|
| `INT-CLIN-01` | Clinical alert → diagnosis → treatment → outcome | Gejala terdeteksi → alert muncul → pemain buka modal → pilih diagnosis → pilih treatment → hasil dihitung |
| `INT-CLIN-02` | Defisiensi berkepanjangan → memicu penyakit | N rendah 7+ hari → tanaman stres → Fusarium risk naik |
| `INT-CLIN-03` | Overfeeding → ammonia spike → fish stress | Pakan berlebih 3 hari → NH3 naik → clinical alert Amonia Stress |

---

## 5. System Test Cases (End-to-End)

| ID | Test Case | Steps | Expected Outcome |
|----|-----------|-------|-----------------|
| `SYS-01` | Setup awal → panen kangkung pertama | 1. Buat galon 2. Isi air + EM4 3. Time-skip 5 hari 4. Tebar benih 5. Rutinitas 10 hari 6. Bangun raised bed 7. Tanam kangkung 8. Time-skip 25 hari | Kangkung siap panen, air lele sehat, pemain paham basic loop |
| `SYS-02` | Siklus lele penuh (75 hari game) | Setup → tebar → feeding 75 hari → panen | 45–60 ekor dipanen, ABW 100g+, mortalitas <10% |
| `SYS-03` | Semua 8 penyakit ikan ter-trigger | Manipulasi parameter untuk trigger tiap penyakit | Semua 8 kondisi muncul, bisa didiagnosis, bisa diobati |
| `SYS-04` | Semua 7 penyakit tanaman ter-trigger | Manipulasi kondisi untuk trigger tiap penyakit | Semua 7 kondisi muncul, bisa didiagnosis, bisa diobati |
| `SYS-05` | Semua 4 booster di-craft dan diaplikasikan | Crafting semua booster → aplikasi ke tanaman | Boost verifikasi efektif (+20% yield) |

---

## 6. Performance Test Cases

| ID | Test Case | Target | Cara Ukur |
|----|-----------|--------|-----------|
| `PERF-01` | FPS di mobile low-end | >30 FPS | `RenderStepped` delta time, Android 4GB RAM |
| `PERF-02` | FPS di desktop | >60 FPS | `RenderStepped` delta time |
| `PERF-03` | Server tick time | <5ms per 30s tick | `workspace:GetServerTimeNow()` delta |
| `PERF-04` | DataStore write size | <4KB per player | `HttpService:JSONEncode(data)` size check |
| `PERF-05` | Partikel aktif total | <500 | `ParticleEmitter` count audit |
| `PERF-06` | Memory usage | <500MB client | `Stats:GetTotalMemoryUsageMb()` |

---

## 7. Smoke Test Checklist (Sebelum Setiap Rilis)

Jalankan checklist ini sebelum naik ke staging/production:

- [ ] Game bisa di-join tanpa error
- [ ] Data player tersimpan dan ter-load dengan benar
- [ ] Semua ProximityPrompt berfungsi
- [ ] HUD menampilkan parameter dengan benar
- [ ] Time system berjalan (hari berganti, siang/malam)
- [ ] Feeding work (pakan berkurang, ikan merespons)
- [ ] Flushing work (parameter air berubah)
- [ ] Minimal 1 penyakit bisa dipicu dan diobati
- [ ] Tanaman bisa ditanam dan dipanen
- [ ] DataStore save/load berfungsi (relog test)
- [ ] Tidak ada error di console (F9)
- [ ] FPS >30 di mobile

---

## 8. Bug Severity Classification

| Severity | Definisi | Response Time |
|----------|---------|---------------|
| **P0 — Critical** | Game crash, data loss, tidak bisa join | Fix IMMEDIATE (dalam jam) |
| **P1 — High** | Fitur utama tidak berfungsi (tidak bisa feeding, tidak bisa panen) | Fix dalam 24 jam |
| **P2 — Medium** | Fitur berfungsi tapi ada bug (visual glitch, angka tidak akurat) | Fix dalam sprint ini |
| **P3 — Low** | Kosmetik, typo, minor annoyance | Fix kapan saja, akumulasi |
| **P4 — Enhancement** | Bukan bug, request fitur | Backlog |

---

## 9. Automated Test (Opsional — Future)

```lua
-- TestRunner.server.lua
local TestService = game:GetService("TestService")
local TestRunner = {}

function TestRunner.RunAll()
    local results = {}

    -- Run unit tests
    local waterChemTests = require(script.Tests.LeleBioflok.WaterChemistry)
    table.insert(results, waterChemTests())

    local fishGrowthTests = require(script.Tests.LeleBioflok.FishGrowth)
    table.insert(results, fishGrowthTests())

    -- Print summary
    local passed = 0
    local failed = 0
    for _, result in results do
        if result.passed then passed += 1 else failed += 1 end
    end
    print(string.format("Tests: %d passed, %d failed", passed, failed))
end

return TestRunner
```

---

*Dokumen Berikutnya: 15-Error-Handling.md — Penanganan Error & Disaster Recovery*
