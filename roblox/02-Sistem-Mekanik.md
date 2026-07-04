# 02 — SISTEM MEKANIK: Mekanik Game Detail

---

## SISTEM 1: LELE BIOFLOK (Sistem 3 Galon)

### 1.1 Setup Tangki & Perangkat Keras

| Properti | Nilai | Representasi Game |
|----------|-------|---------------------|
| Jenis tangki | Galon air mineral 19L (terbalik) | Model 3D: galon tembus pandang berwarna biru, bagian atas dipotong |
| Jumlah | 3 galon, terhubung | Model individual, sambungan pipa terlihat |
| Aerasi | Pompa udara 18W, manifold 4 cabang | Aliran gelembung animasi; suara: dengung rendah |
| Drainase | Stop kran di tutup bawah | Katup interaktif; pemain klik untuk flushing |
| Posisi | Di bawah atap galvalum (Stasiun Nutrisi) | Area Zona 1, terlindung dari hujan |

**Mekanik Game:**
- Pemain harus merakit sistem: tempatkan galon di dudukan → sambungkan pipa manifold → colokkan aerator (toggle ON/OFF via UI)
- Setiap galon adalah kontainer simulasi independen
- Katup bleeding (cabang ke-4): jika pemain lupa membukanya, motor aerator menunjukkan partikel "overheat" setelah 2 jam game

### 1.2 Simulasi Kimia Air

Air di setiap galon memiliki model kimia real-time:

```
WaterState {
    volume_L:          number (maks 15L terpakai, 4L ruang kepala)
    temperature_C:     number (suhu ruang + pengubah panas atap)
    pH:                number (ideal 7.0–8.0)
    dissolvedO2_mgL:   number (ideal > 4.0)
    ammonia_NH3_mgL:   number (toksik > 0.5)
    nitrite_NO2_mgL:   number (toksik > 1.0)
    nitrate_NO3_mgL:   number (menguntungkan, terakumulasi)
    totalSuspendedSolids_mgL: number (indikator kepadatan flok)
    flocMaturity:       0.0–1.0 (seberapa mapan koloni biofilm)
    alkalinity_mgL:    number (kapasitas penyangga)
    microbialActivity: 0.0–1.0 (populasi bakteri aktif)
}
```

**Tick Simulasi (setiap 30 detik nyata = ~1.2 jam game pada kecepatan default):**

```
Δamonia = + (pakan_terurai * laju_metabolisme_ikan * kepadatan) - (kematanganFlok * aktivitasMikroba * oksigenTerlarut * 0.8)
Δnitrit  = + (amonia_teroksidasi) - (nitrit_teroksidasi_oleh_flok)
Δnitrat  = + (nitrit_teroksidasi)
ΔpH      = - (akumulasi_amonia * 0.15) + (aerasi_menyala * 0.02) - (CO2_dari_ikan * 0.01)
ΔDO      = + (output_aerator * aerasi_menyala) - (konsumsi_ikan * kepadatan) - (aktivitasMikroba * 0.3)
```

**Aksi Pemain yang Mempengaruhi Air:**
- Flushing (buka katup bawah): menghilangkan 30–50% volume → mengurangi NH₃, NO₂⁻, TSS secara proporsional
- Top-up air: menambah air bersih → mengencerkan semua konsentrasi, dapat menggeser pH jika pH air sumber berbeda
- Menambah dolomit/kapur: menaikkan pH +0.3 per aplikasi (batas 8.5)
- Menambah probiotik EM4: meningkatkan aktivitasMikroba sebesar 0.15, mempercepat kematanganFlok
- Menambah molase: memberi makan bakteri, menurunkan DO sementara (bakteri mengonsumsi O₂)
- Menambah garam (NaCl): menaikkan salinitas, mempengaruhi osmoregulasi (tidak ada perubahan kimia langsung tetapi memblokir toksisitas nitrit)

### 1.3 Model Pertumbuhan & Populasi Ikan

Setiap galon melacak ikan individual sebagai array:

```
Fish {
    id:             string
    panjang_cm:     number
    berat_g:        number (ABW — Average Body Weight)
    fase:           "starter" | "grower" | "finisher"
    kesehatan:      0.0–1.0
    tingkatStres:   0.0–1.0
    efisiensiPakan: 0.0–1.0 (dipengaruhi kualitas air)
    statusPenyakit: null | "stres_amonia" | "saprolegnia" | "aeromonas" | "kembung" | "anoksia" | "kepala_pecah" | "kuning" | "bintik_putih"
    hariDalamTangki: number
}
```

**Aturan Penebaran:**
- Kepadatan maks: 20 ekor per galon (15–20 optimal sesuai buku)
- Total untuk 3 galon: 45–60 ekor
- Ukuran benih minimal: 7–9 cm (game menegakkan ini)
- Mekanik aklimatisasi: pemain harus mengapungkan kantong selama 15 menit (waktu game) sebelum melepas, atau tingkatStres melonjak +0.4

**Fase Pertumbuhan (dipetakan ke tabel ABW buku):**

| Fase | Hari | Panjang (cm) | ABW (g) | Kode Pelet | Protein % | Feeding Rate (FR) |
|-------|------|-------------|---------|-------------|-----------|-------------------|
| Starter | 1–28 | 7–10 | 3–8 | PF-1000 / 781-1 | 31–35% | 5–6% |
| Grower | 29–56 | 11–15 | 9–30 | 781-2 | 28–32% | 4–5% |
| Finisher | 57–75 | >15 | 31–125 | 781-3 | 26–30% | 3% |

**Formula Pertumbuhan (per hari):**

```
pertambahanBerat = (FR * ABW * efisiensiPakan * (1 - tingkatStres)) - (biayaPemeliharaan * ABW^0.8)
```

- `efisiensiPakan` menurun saat: pH < 6.5, DO < 2, NH₃ > 1.0, suhu < 22°C atau > 32°C
- `tingkatStres` meningkat dengan: air buruk, kepadatan berlebih, keberadaan penyakit, sering dipegang
- Kematian terjadi ketika: kesehatan turun di bawah 0.1 selama > 12 jam game

### 1.4 Mekanik Pemberian Pakan

**Perhitungan Pakan Harian (pemain harus menghitung atau menggunakan kalkulator in-game):**

```
PakanHarian (g) = JumlahIkan × ABW (g) × FR (desimal)
Pagi (40%) = PakanHarian × 0.4
Sore (60%) = PakanHarian × 0.6
```

**Implementasi Game:**
- Pemain menggunakan UI timbangan digital → input jumlah ikan, ABW, FR → menghitung gram yang dibutuhkan
- Referensi "Sendok Makan": 1 sdm ≈ 8–10g pelet kering
- Pemain menyendok pelet menggunakan sendok takar interaktif
- **Syarat Fermentasi (Bibis):** Pemain WAJIB mencampur pelet dengan larutan EM4 + molase dan inkubasi selama 1–2 jam game (atau semalaman). Jika diberi kering:
  - Efisiensi pakan turun 40%
  - Risiko "Kembung Pakan" meningkat 25%
- Overfeeding: pelet berlebih membusuk → lonjakan amonia dalam 4 jam game

**Ninja Sampling (setiap 10 hari game):**
- Pemain menangkap 5 ikan acak dengan serokan kecil
- Menimbang bersama di timbangan digital → menghitung ABW baru
- Memperbarui formula pakan untuk 10 hari ke depan
- Jika pemain melewatkan sampling, menggunakan ABW basi → pakan kurang/berlebih

### 1.5 Sistem Penyakit & SOP Klinis

Setiap kondisi klinis (A–H dari buku) dipicu oleh ambang parameter spesifik:

| Kondisi Klinis | Ambang Pemicu | Gejala Visual |
|-------------------|-------------------|-----------------|
| **A: Stres Amonia** (Menggantung vertikal, kumis keriting) | NH₃ > 0.5 DAN DO < 3.0 selama 6 jam | Ikan melayang vertikal di permukaan, kumis tampak keriting/patah, lapisan lendir kusam |
| **B: Saprolegniasis** (Jamur kapas) | Suhu turun >5°C dalam <2 jam ATAU pH < 6.0 selama 24 jam | Bercak putih berbulu di tubuh, ikan "flashing" (menggesekkan diri ke dinding) |
| **C: Aeromonas** (Luka merah, sirip gripis, dropsy) | Akumulasi pakan tak termakan DAN DO < 2.0 selama 12 jam | Bintik merah di perut, sirip compang-camping, perut bengkak (efek partikel dropsy) |
| **D: Kembung Pakan** (Perut keras buncit, berenang miring) | Diberi pelet kering 3+ kali berturut-turut | Perut kembung keras, berenang miring/terbalik, tanpa lesi eksternal |
| **E: Krisis Anoksia** (Kejadian mati lampu) | Aerator MATI selama >1 jam (kejadian terjadwal atau aksi pemain) | Semua ikan megap-megap di permukaan, gerakan panik, beberapa mengambang miring |
| **F: Kepala Pecah** (Defisiensi Vitamin C) | Pelet tersimpan terkena panas atap >7 hari | Retakan tengkorak terlihat, ikan berenang melingkar (animasi berputar) |
| **G: Penyakit Kuning** (Keracunan aflatoksin) | Pakan berjamur digunakan ATAU sisa dapur terkontaminasi | Warna kuning-oranye di perut dan mata, tubuh kurus, lesu |
| **H: Bintik Putih** (Ich) | Fluktuasi suhu >5°C dalam 24 jam (ayunan siang/malam) | Bintik putih seperti garam di tubuh, flashing konstan, megap-megap |

**Tindakan Pengobatan (pemain memilih dari menu SOP):**

| Kondisi | Pilihan Pengobatan | Efektivitas |
|-----------|------------------|---------------|
| A: Stres Amonia | Puasakan 24–48 jam + flush 50% air + tingkatkan aerasi + garam 1g/L | 90% jika tertangani dalam 12 jam |
| B: Saprolegnia | Salt bath (10–15g/L, 10–15 menit) untuk ikan sakit + ekstrak daun pepaya/sirih di tangki utama | 85% jika diobati dini |
| C: Aeromonas | Flush 50% + puasa 3 hari + ekstrak bawang putih + ekstrak daun mengkudu | 70% jika tertangkap sebelum dropsy; 30% setelah dropsy |
| D: Kembung Pakan | Puasa 3 hari + ekstrak daun pepaya → evaluasi SOP bibis | 95% jika tertangkap dini |
| E: Anoksia | JANGAN DIBERI PAKAN + turunkan level air 20% + aerasi manual (percikkan) setiap 30 menit | 80% jika listrik pulih dalam 3 jam |
| F: Kepala Pecah | Ganti pakan lama + pakan direndam ekstrak jeruk nipis/jambu biji | 60% pemulihan; pencegahan adalah kunci |
| G: Penyakit Kuning | Musnahkan pakan lama + flush 50% + puasa 3 hari + bibis kunyit/temulawak selama 5 hari | 40% pemulihan; kerusakan hati sering permanen |
| H: Bintik Putih | Isolasi tangki + garam 2g/L + ekstrak daun sirih merah + flush 40% harian selama 5 hari | 85% dengan protokol penuh |

**Perhitungan Keberhasilan Pengobatan:**

```
tingkatKeberhasilan = efektivitasDasar × (1 - penaltiKeterlambatan) × (1 - penaltiSalahDiagnosis)
penaltiKeterlambatan = jamSejakPemicu / jendelaKritis
penaltiSalahDiagnosis = 0.5 jika pengobatan salah diterapkan lebih dulu
```

- Jika pengobatan gagal ATAU pemain tidak melakukan apa-apa, kematian massal terjadi
- Pemain menerima "Laporan Kasus Klinis" setelah setiap kejadian penyakit dengan apa yang mereka lakukan benar/salah
- Laporan ini berkontribusi pada profil asesmen pembelajar

### 1.6 Panen & Sortir

- Pemicu panen: ABW mencapai 100–125g (ukuran konsumsi 10 ekor/kg)
- Tercapai pada ~75 hari game (~18.75 jam pada kecepatan default)
- **Syarat sortir (Bulan 1.5):** Pemain harus memeriksa semua ikan, memisahkan individu "monster" kanibal ke galon terpisah
  - Jika tidak disortir: 1–2 ikan dimakan per hari oleh yang monster
- Aksi panen: Pemain menyerok ikan → ditimbang → digrading → disimpan atau dikonsumsi

---

## SISTEM 2: MAGGOT BSF (Black Soldier Fly — Pabrik Protein)

### 2.1 Setup Biopond

| Properti | Nilai |
|----------|-------|
| Kontainer | Box/ember plastik lebar |
| Ramp | Papan miring 45° menuju kontainer penampungan |
| Substrat | Sampah dapur + opsional kompos setengah matang |
| Penutup | Kasa jaring (mencegah kabur, memungkinkan aliran udara) |
| Lokasi | Di bawah atap galvalum (kelembapan terkontrol) |

### 2.2 Simulasi Siklus Hidup BSF

```
KoloniBSF {
    jumlah_telur:       number (diletakkan di bilah kayu dalam kandang kawin)
    jumlah_larva:       number (di biopond)
    beratTotalLarva_g:  number
    jumlah_prepupa:     number (bermigrasi naik ramp)
    jumlah_pupa:        number (di kandang kawin)
    jumlah_lalatDewasa: number (di kandang kasa)
    umurLalatDewasa_jam: number (umur 5–8 hari)
    kesehatanKoloni:    0.0–1.0
}
```

**Tahap Siklus Hidup (diskalakan ke waktu nyata):**

| Tahap | Durasi | Waktu Game (default) | Mekanik |
|-------|----------|---------------------|---------|
| Telur → Larva | 3–4 hari | ~1 jam | Telur menetas di bilah kayu → pemain memindahkan ke biopond |
| Larva (makan) | 14–18 hari | ~4–5 jam | Konsumsi 2–5× berat tubuh/hari dalam substrat |
| Prepupa (migrasi) | 1–2 hari | ~30 menit | Berubah hitam, memanjat ramp 45° → otomatis jatuh ke wadah panen |
| Pupa | 7–10 hari | ~2–2.5 jam | Dalam kandang kawin kasa dengan tumpukan kayu |
| Lalat Dewasa | 5–8 hari | ~1.5–2 jam | Kawin, bertelur di kayu, mati |

### 2.3 Manajemen Substrat

**Jenis Pakan & Efek:**

| Jenis Substrat | Laju Pertumbuhan Larva | Ukuran Prepupa | Tingkat Bau | Catatan |
|---------------|-------------------|---------------|------------|-------|
| Sampah dapur (umum) | 1.0× | Normal | Sedang | Baseline |
| Sisa pepaya | 1.3× | Besar | Rendah | Meningkatkan kadar asam laurat pada maggot (±50–55% dari total asam lemak) |
| Kompos setengah matang | 1.2× | Sedang | Rendah | Menambah mikroba menguntungkan |
| Sayuran busuk | 0.7× | Kecil | Sangat Tinggi | Risiko kontaminasi patogen |
| Daun mangga kering | NEGATIF | — | — | JANGAN DITAMBAHKAN — membunuh larva, menyebabkan becek |

**Mekanik Anti-Bau:**
- Jika substrat terlalu basah: tingkatBau naik, kepuasan tetangga turun
- Aksi pemain: tambah serbuk gergaji/bekatul → semprot EE (1:1000) → mengurangi bau 60%

### 2.4 Mekanik Auto-Harvest

- Deteksi prepupa: ketika larva berubah cokelat tua/hitam (isyarat visual)
- Migrasi: prepupa otomatis merayap naik ramp 45°
- Pengumpulan: jatuh ke wadah panen (pemain mendengar suara "plop")
- Hasil panen: gunakan sebagai pakan ayam atau jual/tukar
- Jika tidak dipanen dalam 2 hari game: prepupa menjadi pupa di wadah panen → siklus berlanjut

---

## SISTEM 3: AYAM PETELUR (Sistem Deep Litter)

### 3.1 Setup Kandang

| Properti | Nilai |
|----------|-------|
| Lantai | Tanah (bukan semen!), deep litter |
| Ketebalan litter | 15–20 cm |
| Komposisi litter | Daun mangga kering (Karbon) + sekam padi + tanah |
| Struktur | Kandang tertutup sederhana di bawah atap galvalum |
| Kapasitas | 5–10 ayam petelur (skala urban) |

### 3.2 Model Fermentasi Deep Litter

```
DeepLitter {
    ketebalan_cm:       number (ideal 15–20)
    lapisanKarbon_cm:   number (daun mangga)
    inputNitrogen_g:    number (akumulasi kotoran)
    kelembapan_persen:  number (ideal 40–60%)
    suhu_C:             number (panas fermentasi)
    lajuDekomposisi:    0.0–1.0
    kematanganKompos:   0.0–1.0 (siap pada 1.0 = ~6 bulan waktu game)
    tingkatBau:         0.0–1.0
    aktivitasMikroba:   0.0–1.0
}
```

**Logika Fermentasi:**

```
Δdekomposisi = (lapisanKarbon * aktivitasMikroba * kelembapan_optimal * suhu_optimal) / ketebalan_cm
ΔkematanganKompos = lajuDekomposisi / totalHariKeMatang
ΔtingkatBau = (inputNitrogen / lapisanKarbon) - (lajuDekomposisi * 0.5)
```

- Jika rasio C:N terlalu rendah (terlalu banyak kotoran, terlalu sedikit karbon): bau amonia → tingkatBau naik → keluhan tetangga
- Jika kelembapan terlalu tinggi (>70%): titik anaerobik → bau busuk, lalat
- Aksi pemain: tambah daun mangga kering untuk menyeimbangkan C:N
- **Auto-mixing:** Ayam mengais litter (animasi berulang) → otomatis mengaerasi tumpukan
- **Panen:** Setelah 6 bulan game (~45 jam), pemain dapat memanen kompos matang penuh untuk raised bed

### 3.3 Perilaku & Produksi Ayam

```
Ayam {
    ras:                "kampung" | "petelur"
    umur_hari:          number
    kesehatan:          0.0–1.0
    lapar:              0.0–1.0
    lajuProduksiTelur:  number (telur/hari)
    kualitasTelur:      0.0–1.0 (dipengaruhi pakan)
    tingkatStres:       0.0–1.0
}
```

**Komposisi Pakan (Formula Ninja):**

| Komponen | Persentase | Efek |
|-----------|-----------|--------|
| Pakan komersial | 50% | Nutrisi dasar |
| Sayuran afkir | 25% | Serat, vitamin, **karotenoid (warna kuning telur)** |
| Maggot BSF segar | 25% | Boost protein, asam laurat → kesehatan imun |

**Formula Produksi Telur:**

```
telurPerHari = lajuDasar × kesehatan × (1 - tingkatStres) × pengaliKualitasPakan
pengaliKualitasPakan = 1.0 + (persenMaggot * 0.3) + (variasiSayuran * 0.1)
```

- Laju dasar: 0.7–1.0 telur/hari per ayam (kampung), 0.8–1.2 (ras petelur)
- Pakan maggot: +30% boost produksi, +15% kesehatan ayam → penyerapan karotenoid dari sayuran lebih efisien → kuning telur lebih baik (efek tidak langsung)
- Koleksi telur: pemain berinteraksi dengan kotak sarang → mengumpulkan telur setiap hari (rutinitas pagi)

---

## SISTEM 4: RAISED BEDS (Produksi Sayuran)

### 4.1 Konstruksi Bedengan

| Properti | Nilai |
|----------|-------|
| Dimensi | 200 cm × 100 cm × 20 cm (P×L×T) |
| Material | Papan cor semen (papan cor) |
| Pelapis | Mulsa plastik distaples hanya di dinding dalam |
| Mulsa atas | 2–3 cm cacahan daun mangga kering |
| Jarak jalur | Min 40 cm antar bedengan |
| Lokasi | Zona 2 — sinar matahari penuh, area terbuka |

**Mekanik Perakitan:**
- Pemain crafting: 2 papan utuh (200cm) + 1 papan dipotong jadi 2 (masing-masing 100cm) → dipaku bersama
- Staples mulsa plastik ke dinding dalam (tugas interaktif)
- Isi dengan campuran tanah → aplikasikan mulsa atas

### 4.2 Model Tanah

```
KondisiTanah {
    pH:                 number (ideal 6.0–7.0 untuk kebanyakan sayuran)
    nitrogen_N:         number (mg/kg)
    fosfor_P:           number (mg/kg)
    kalium_K:           number (mg/kg)
    kalsium_Ca:         number (mg/kg)
    magnesium_Mg:       number (mg/kg)
    bahanOrganik_persen: number
    kelembapan_persen:  number
    suhu_C:             number
    KTK_meq100g:        number (Kapasitas Tukar Kation)
    CFUmikroba:         number (colony forming units — abstraksi gameplay: nilai relatif, bukan pengukuran laboratorium)
    pemadatan:          0.0–1.0 (0 = gembur, 1 = beton)
    kandunganAsamHumat: 0.0–1.0
    tekananPenyakit:    { jenisPatogen: keparahan_0_ke_1 }
    tekananHama:        { jenisHama: keparahan_0_ke_1 }
}
```

**Sumber Input Nutrisi:**

| Sumber | N | P | K | Ca | Mg | Bahan Organik |
|--------|---|---|---|---|----------------|
| Air lele (flush harian) | TINGGI | Rendah | Sedang | Rendah | Rendah | Rendah |
| Kompos (matang) | Sedang | Sedang | Sedang | Sedang | Sedang | TINGGI |
| Eco-Enzyme (1:1000) | Rendah | Rendah | Rendah | Rendah | Rendah | Sedang (mikroba) |
| K-Booster (gedebog pisang) | Rendah | Rendah | TINGGI | Rendah | Rendah | Rendah |
| Aminor-Grow (hidrolisat lele) | TINGGI | Rendah | Rendah | Rendah | Rendah | Rendah |
| Cal-Phos Liquid (cangkang telur + tulang) | Rendah | TINGGI | Rendah | TINGGI | Rendah | Rendah |
| Mag-Elixir (garam Epsom) | — | — | — | — | TINGGI | — |
| Humo-Ninja (biochar tercharge) | Sedang | Sedang | Sedang | Sedang | Sedang | TINGGI (boost KTK) |
| JMS-IMO (mikroba bambu) | — | — | — | — | — | TINGGI (mikroba) |
| Kompos deep litter ayam | TINGGI | TINGGI | TINGGI | Sedang | Sedang | TINGGI |

### 4.3 Model Pertumbuhan Tanaman

```
Tanaman {
    spesies:            "kangkung" | "sawi" | "caisim" | "pakcoy" | "bayam" | "selada" | "tomat" | "cabai" | "terong" | "kacang_panjang"
    tahapTumbuh:        "semai" | "vegetatif" | "pembungaan" | "pembuahan" | "matang" | "senescence"
    hariSejakTanam:     number
    kesehatan:          0.0–1.0
    klorosisDaun:       0.0–1.0 (indikator menguning)
    statusPenyakit:     null | "fusarium" | "layu_bakteri" | "antraknosa" | "late_blight" | "virus_gemini" | "damping_off" | "karat_putih"
    infestasiHama:      { hama: keparahan }
    hasil_gram:         number (porsi dapat dimakan)
    kualitas:           0.0–1.0 (grade pasar)
}
```

**Formula Laju Pertumbuhan:**

```
pertumbuhanHarian = lajuPertumbuhanDasar × faktorCahaya × faktorAir × faktorNutrisi × faktorSuhu × (1 - penaltiPenyakit) × (1 - penaltiHama)
```

**Parameter Spesifik Spesies:**

| Spesies | Hari ke Panen | Kebutuhan Cahaya | Kebutuhan Air | Kebutuhan N | Kebutuhan P | Kebutuhan K | Kebutuhan Ca |
|---------|----------------|------------|------------|--------|--------|--------|---------|
| Kangkung | 25–30 | Tinggi | Tinggi | TINGGI | Rendah | Sedang | Rendah |
| Sawi/Caisim | 30–35 | Tinggi | Tinggi | TINGGI | Rendah | Sedang | Rendah |
| Pakcoy | 25–30 | Sedang-Tinggi | Sedang | TINGGI | Rendah | Sedang | Rendah |
| Bayam | 20–25 | Matahari penuh | Sedang | Tinggi | Rendah | Sedang | Rendah |
| Selada | 30–40 | Semi-naungan | Sedang | Sedang | Rendah | Sedang | Rendah |
| Tomat | 75–90 | Matahari penuh | Sedang | Sedang | TINGGI | TINGGI | TINGGI |
| Cabai | 75–90 | Matahari penuh | Sedang | Sedang | TINGGI | TINGGI | TINGGI |
| Terong | 70–85 | Matahari penuh | Sedang | Sedang | TINGGI | TINGGI | TINGGI |
| Kacang Panjang | 50–60 | Matahari penuh | Rendah | FIKSASI N | Sedang | Tinggi | Sedang |

**Mekanik Khusus — Legum (Kacang Panjang/Buncis):**
- Simbiosis Rhizobium: memfiksasi N₂ atmosferik, menambah nitrogen ke tanah
- Menanam legum dalam rotasi meregenerasi bedengan yang kehabisan nitrogen
- Bonus: daun lembayung diberikan ke ayam meningkatkan kualitas telur

### 4.4 Penyakit Tanaman & SOP Klinis

Berdasarkan matriks klinis tanaman buku (A–G):

| Kondisi Klinis | Pemicu | Gejala Visual |
|-------------------|---------|-----------------|
| **A: Layu Fusarium** | Kelembapan tanah >80% DAN pH <5.5 | Daun bawah menguning → layu siang hari → pulih malam → akhirnya seluruh tanaman mengering cokelat dan mati tegak. Jaringan pembuluh berwarna cokelat di dalam. |
| **B: Layu Bakteri** (Ralstonia) | Kelembapan tinggi DAN air terkontaminasi | Layu mendadak dalam 2–3 hari saat masih hijau. Potong batang dalam air → keluar cairan putih susu (bacterial ooze). |
| **C: Antraknosa** (Patek pada cabai) | Cipratan hujan + N berlebih tanpa Ca | Bercak cokelat melingkar cekung pada buah, cincin konsentris, buah membusuk dan rontok. |
| **D: Late Blight** (Phytophthora pada tomat) | Kelembapan >90% + cuaca basah dingin + pemangkasan buruk | Bercak basah gelap pada tepi daun → cokelat/hitam → bulu putih di sisi bawah → busuk batang. |
| **E: Virus Gemini** (Kuning keriting) | Vektor kutu kebul (Bemisia tabaci) hadir | Klorosis kuning cerah, daun keriting menangkup, kerdil ekstrem, tidak berbuah. |
| **F: Damping-Off** (Pythium pada semaian) | Media semai terlalu basah + aliran udara buruk | Semaian roboh di garis tanah, batang terjepit cokelat, pucuk masih hijau sebelum mati. |
| **G: Karat Putih** (Albugo pada kangkung) | Jarak tanam terlalu rapat + kelembapan terperangkap | Lepuh putih di sisi bawah daun, bercak kuning di sisi atas, daun keriting dan kering. |

**Pengobatan (Aksi Pemain dari SOP):**

| Kondisi | Pengobatan | Senyawa Aktif Utama |
|-----------|---------------------|---------------------|
| A: Fusarium | Singkirkan tanaman sakit. Aplikasikan abu kayu (2 genggam per tanaman) + Trichoderma + EE 1:500 ke tanah | K₂CO₃/CaO (alkalin) + mikoparasitisme Trichoderma |
| B: Layu Bakteri | SEGERA cabut dan musnahkan tanaman terinfeksi (jangan dikomposkan!). Aplikasikan abu + Trichoderma ke tanah tersisa | Sanitasi + sawar pH alkalin |
| C: Antraknosa | Singkirkan buah terinfeksi. Semprot susu segar (1:5) setiap 3 hari ATAU baking soda (5g/L + sabun) | Protein whey → singlet oksigen; NaHCO₃ → permukaan alkalin |
| D: Late Blight | Pangkas daun bawah 30cm dari tanah. Semprot belerang (3g/L air hangat + sabun) secara kabut | Belerang elemental → gangguan mitokondria pada oomycetes |
| E: Virus Gemini | TIDAK ADA OBAT. Jika >70% kuning, cabut dan bakar. Kendalikan vektor: minyak mimba (5ml/L + sabun) setiap 3 hari + yellow sticky trap | Azadirachtin (IGR) pada kutu kebul; penangkapan fisik |
| F: Damping-Off | Hentikan penyiraman sore. Semprot rebusan kayu manis. Top dressing arang sekam 2mm | Sinamaldehida (antifungal) + penguatan silika |
| G: Karat Putih | Sesuaikan jarak tanam (5–7cm). Semprot larutan kapur sirih (2g/L, ambil bagian atas jernih) + EE 1ml | Ca(OH)₂ pH alkalin → lisis spora |

### 4.5 Manajemen Hama

**Jenis Hama & Pengendalian:**

| Hama | Tanaman Target | Kerusakan | Metode Pengendalian |
|------|-------------|--------|----------------|
| Kutu Daun (Aphids) | Cabai, tomat, terong | Mengisap cairan → daun keriting, kerdil | Semprot PesNab (bawang putih + cabai + sabun) |
| Kutu Kebul (Whitefly) | Cabai, tomat | Vektor virus Gemini + mengisap cairan | Semprot minyak mimba + yellow sticky trap |
| Ulat | Semua sayuran daun | Konsumsi daun | Pemetikan manual + semprot PesNab |
| Belalang | Semua | Mengunyah daun/batang | Jaring + pengusir PesNab |
| Siput/Keong | Semaian, sayuran daun | Kerusakan daun/batang | Pemetikan manual + cincin sawar abu |

**Resep PesNab Super (crafting in-game):**
```
Input: Kulit bawang putih + sisa cabai + 1L air
Proses: Blender + rendam 24 jam → saring → tambah 1 sdt sabun cuci piring (perekat)
Aturan: Hentikan penyemprotan minimal 3 hari sebelum panen
```

---

## SISTEM 5: KOMPOSTER & ECO-ENZYME

### 5.1 Komposter

```
Komposter {
    massaOrganik_kg:    number
    kayaKarbon_kg:      number (daun mangga kering)
    kayaNitrogen_kg:    number (sampah dapur + kotoran)
    rasio_CN:           number (ideal 25–30:1)
    kelembapan_persen:  number (ideal 50–60%)
    suhu_C:             number (fase termofilik: 55–65°C)
    tingkatAerasi:      0.0–1.0 (frekuensi pembalikan)
    kematangan:         0.0–1.0
    aplikasiEE:         boolean (EE 1:1000 disemprot?)
    hariAktif:          number
}
```

**Laju Pengomposan:**

```
Δkematangan = (faktorSuhu × faktorKelembapan × faktorAerasi × boostEE × efisiensiCN) / hariKeMatang
hariKeMatang = 21–28 (hari game) dengan kondisi optimal; EE mengurangi 30%
```

- **Pembalikan:** Pemain harus berinteraksi untuk membalik/mengaerasi drum kompos setiap 3 hari game
- **Semprot EE:** Mengurangi waktu pematangan 30% dan menghilangkan bau
- **Panen:** Kompos matang (cokelat tua, bau tanah, remah) → diaplikasikan ke raised bed

### 5.2 Produksi Eco-Enzyme

```
EcoEnzyme {
    batchID:            string
    kulitBuah_kg:       number (jeruk lebih disukai)
    gulaMerah_kg:       number (atau molase)
    air_L:              number
    rasio:              "3:1:10" (kulit : gula : air)
    hariFermentasi:     number
    kematangan:         0.0–1.0 (penuh pada 90+ hari, dapat digunakan pada 60+)
    pH:                 number (turun dari ~7 → ~3.0)
    volume_L:           number
    kualitas:           "basic" | "matang" | "aged" (aged = 1+ tahun, paling poten)
}
```

**Proses Crafting:**
- Pemain mengisi kontainer: 3 bagian kulit buah + 1 bagian gula merah/molase + 10 bagian air
- Segel + label dengan tanggal
- Bulan pertama: pelepasan gas harian (sendawakan kontainer)
- Pematangan: minimal 3 bulan waktu game (~5.6 jam pada kecepatan default)
- EE "Aged": 1+ tahun waktu game (~22.5 jam) → paling poten untuk aplikasi klinis

**Pengali Penggunaan:**

| Aplikasi | Pengenceran | Efek |
|-------------|----------|--------|
| Akselerator kompos | 1:1000 | +30% kecepatan dekomposisi |
| Semprot daun (imunitas tanaman) | 1:1000 | +15% ketahanan penyakit selama 7 hari |
| Anti-bau biopond | 1:1000 | -60% bau |
| Anti-bau kandang | 1:1000 | -50% bau amonia |
| Siram tanah (pengendalian Fusarium) | 1:500 | -40% tekanan Fusarium |
| Aktivasi EM4 | Sebagai bahan | Media pertumbuhan mikroba |
| Disinfektan umum | 1:100 | Pembersihan permukaan |

---

## SISTEM 6: BIO-MULTIPLIKASI EM4

### 6.1 Produksi EM-Aktif

```
EMAktif {
    starterEM4_mL:      number (1 bagian)
    molase_mL:          number (1 bagian)
    air_L:              number (18–20 bagian)
    hariFermentasi:     number (7–10)
    kematangan:         0.0–1.0
    pH:                 number (target < 4.0)
    volume_L:           number
    kepadatanMikroba:   number (CFU/mL)
    kualitas:           "gagal" | "aktif" | "poten"
}
```

**Mekanik:**
- Rasio input: 1L EM4 : 1L molase : 18–20L air bebas kaporit
- Aksi harian: sendawakan kontainer (lepaskan gas)
- Indikator keberhasilan: aroma fermentasi manis (seperti tape), pH < 4.0
- Kegagalan: bau busuk/basi → kontaminasi, batch harus dibuang
- Hasil: 20L EM-Aktif dari 1L EM4 → menggantikan pembelian toko untuk semua aplikasi
- Penghematan biaya dilacak di dasbor ekonomi pemain

---

## SISTEM 7: CRAFTING BOOSTER ORGANIK (Formula 1–4)

### 7.1 K-BOOSTER NINJA (Booster Buah & Bunga)

**Resep:**
| Bahan | Jumlah | Sumber |
|-----------|----------|--------|
| Batang pisang (gedebog pisang) | 2 kg | Ditanam di farm atau dibeli |
| Sabut kelapa | 1 kg | Dibeli |
| Molase | 250 mL | Dibeli |
| Air cucian beras (leri) | 5 L | Output dapur |
| Eco-Enzyme aged | 50 mL | Produksi farm |

**Crafting:** Cacah → campur dalam wadah tertutup dengan airlock → fermentasi 14 hari game → saring
**Aplikasi:** 10 mL per 1L air, siram tanah mingguan saat fase pembungaan/pembuahan
**Efek:** +25% tingkat fruit set, +20% kadar gula buah (brix), -30% kerontokan bunga

### 7.2 AMINOR-GROW (Supercharger Pertumbuhan Vegetatif)

**Resep:**
| Bahan | Jumlah | Sumber |
|-----------|----------|--------|
| Kepala + jeroan lele | 1 kg | Limbah panen |
| Air kelapa tua | 500 mL | Dibeli |
| Molase | 150 mL | Dibeli |
| Eco-Enzyme | 100 mL | Produksi farm |
| Air bebas kaporit | 3 L | Tampungan air hujan |

**Crafting:** Blender ikan → campur semua di jerigen 5L dengan gas trap → fermentasi 21 hari game → saring
**Aplikasi:** 5 mL per 1L air, semprot kabut daun mingguan pada sayuran daun
**Efek:** +30% laju pertumbuhan daun, +25% kepadatan klorofil, membypass biaya energi konversi nitrogen

### 7.3 CAL-PHOS LIQUID (Kalsium-Fosfor Tulang & Cangkang)

**Resep:**
| Bahan | Jumlah | Sumber |
|-----------|----------|--------|
| Cangkang telur (dicuci, dikeringkan) | 500 g | Output ayam |
| Tulang ikan/ayam | 200 g | Limbah dapur |
| Cuka kayu atau cuka EE aged | 5 L | Produksi farm |

**Crafting:** Sangrai cangkang telur + tulang hingga menghitam → hancurkan menjadi bubuk kasar → tambah cuka (perlahan! gelembung CO₂) → biarkan terbuka 48 jam → segel dan diamkan 10 hari → saring cairan jernih
**Aplikasi:** 2 mL per 1L air (1:500, sangat pekat), semprot pada kluster bunga dan buah muda setiap 10 hari
**Efek:** +35% kandungan kalsium buah, -60% busuk ujung buah, +25% kekerasan buah

### 7.4 MAG-ELIXIR (Klorofil & Anti-Menguning)

**Resep:**
| Bahan | Jumlah | Sumber |
|-----------|----------|--------|
| Garam Epsom (MgSO₄·7H₂O) | 100 g | Dibeli |
| Air kelapa tua | 5 L | Dibeli |
| Eco-Enzyme aged | 25 mL | Produksi farm |

**Crafting:** Larutkan garam Epsom dalam air kelapa → tambah EE → aduk 3 menit → diamkan 24 jam (tanpa fermentasi panjang)
**Aplikasi:** 5 mL per 1L air, semprot daun atau siram tanah, dua kali sebulan
**Efek:** +40% produksi klorofil, menghilangkan penguningan defisiensi magnesium, terutama efektif untuk tanaman semi-naungan (selada di bawah tepi atap)

---

## SISTEM 8: REGENERASI TANAH (Asam Humat, JMS-IMO, Biochar)

### 8.1 SISTEM HUMO-NINJA (Biochar Tercharge)

**Proses:**
1. **Buat biochar:** Bakar lambat daun mangga kering dalam kontainer oksigen rendah → karbonisasi parsial (bukan abu!)
2. **Charge biochar:** Campur 5 kg biochar mentah + 5L air kolam lele + 2 kg kompos matang + 50 mL EE + 100 mL molase
3. **Maturasi:** Segel dan diamkan 7 hari game
4. **Aplikasi:** Campur ke tanah raised bed saat persiapan ATAU gali parit 5 cm sepanjang baris tanaman dan isi

**Efek:**
- +300% KTK (Kapasitas Tukar Kation) — perbaikan tanah permanen
- +60% retensi air di tanah berpasir
- +40% retensi nutrisi (mengurangi leaching)
- Bank nutrisi lepas lambat: menahan K⁺, Ca²⁺, Mg²⁺ dan melepas sesuai permintaan akar
- Efek bertahan sepanjang musim tanam

### 8.2 SERUM JMS-IMO (Larutan Mikroba JADAM)

**Resep:**
| Bahan | Jumlah | Sumber |
|-----------|----------|--------|
| Tanah humus rumpun bambu | 200 g | Dikumpulkan dari lingkungan |
| Kentang rebus (dilumatkan) | 200 g | Dapur |
| Garam krosok | 10 g | Dibeli |
| Air bebas kaporit | 10 L | Air hujan |

**Crafting:**
1. Rebus dan lumatkan kentang
2. Masukkan humus + kentang dalam kantong kain (seperti kantung teh raksasa)
3. Larutkan garam dalam 10L air di wadah lebar
4. Rendam kantong, peras 5 menit → air berubah abu-abu keruh
5. Aerasi (sambung ke cabang aerator) ATAU aduk kuat 3×/hari
6. Tunggu 24–48 jam → klimaks ditandai busa putih tebal + aroma seperti ragi
7. WAJIB digunakan dalam 72 jam atau mikroba mati kelaparan

**Aplikasi:** Encerkan 1:10, siram tanah raised bed saat senja sebelum tanam ATAU mingguan setelah panen
**Efek:**
- +500% CFU mikroba dalam tanah (dari 10³ ke 10⁹ CFU/mL — aproksimasi gameplay, arah dan orde magnitude benar)
- Memperkenalkan: Trichoderma (pengendali patogen), Mycorrhiza (penyerapan P), Pseudomonas (pelarut P), Azotobacter (fiksasi N)
- Mengubah Al-P/Fe-P terkunci menjadi fosfor tersedia tanaman
- Sekresi glomalin → agregasi tanah → kegemburan tanah permanen

### 8.3 Humat-Fulvat Teraktivasi (Peningkatan Humat Komersial)

**Resep:**
| Bahan | Jumlah |
|-----------|----------|
| Bubuk Potassium Humate (98% larut) | 100 g |
| Eco-Enzyme aged | 500 mL |
| Molase | 200 mL |
| Air kolam lele | 2 L |
| Air bebas kaporit | 10 L |

**Crafting:** Larutkan humat → tambah air kolam + molase + EE → aerasi 48 jam → siap saat lapisan cokelat keemasan muncul di permukaan
**Aplikasi:** 50 mL per 10L air (1:200), siram tanah 250 mL per tanaman cabai/tomat, dua minggu sekali
**Efek:** Mengkhelat Fe²⁺, Zn²⁺, Mn²⁺ menjadi bentuk tersedia tanaman; asam fulvat menembus membran akar secara instan

### 8.4 Ekstraksi Humat Alkalin DIY (100% Gratis)

**Proses:** Ekstrak asam humat langsung dari kompos daun mangga matang menggunakan lindi abu kayu
- Lindi: 1 kg abu kayu dalam 10L air hangat → endapkan 24 jam → ambil air jernih alkalin atas (pH ~11–12)
- Ekstraksi: 2 kg kompos matang + 10L lindi → aduk kuat → diamkan 48 jam (aduk harian)
- Saring → netralkan dengan EE hingga pH 6.5–7.5
**Efek:** Menghasilkan cairan Kalium Humat dengan biaya nol; manfaat identik dengan produk komersial

---

## SISTEM 9: INTEGRASI SIKLUS TERTUTUP & EKONOMI

### 11.1 Pelacakan Aliran Sumber Daya

Game melacak semua pertukaran sumber daya antar subsistem:

```
AliranSumberDaya {
    tanggal:            hariGame
    sumber:             IDsubsistem
    tujuan:             IDsubsistem
    jenisSumberDaya:    "air" | "nutrisi" | "pakan" | "kompos" | "maggot" | "kotoran" | "telur" | "ikan" | "sayuran" | "ee"
    jumlah:             number
    kualitas:           number
}
```

### 11.2 Skor Loop Health (0–100)

Metrik "Loop Health" mengevaluasi efisiensi sistem:

```
LoopHealth = (
    tingkatDaurUlangAir × 0.2 +
    tingkatPemulihanNutrisi × 0.25 +
    tingkatAlihFungsiLimbah × 0.2 +
    indeksKemandirian × 0.25 +
    skorZeroWaste × 0.1
) × 100
```

- **Daur Ulang Air:** % air digunakan kembali (lele → tanaman) vs. input air segar
- **Pemulihan Nutrisi:** % nutrisi dari aliran limbah dikembalikan ke produksi
- **Alih Fungsi Limbah:** % limbah organik diproses melalui BSF/kompos vs. dibuang
- **Kemandirian:** % input diproduksi di farm vs. dibeli
- **Zero Waste:** Kebalikan dari output limbah eksternal

### 11.3 Ekonomi In-Game

**Mata Uang:** "Kredit Ninja" (dapat diperoleh) dan Robux (premium)

**Aliran Pendapatan yang Dapat Diperoleh:**
| Aktivitas | Pendapatan |
|----------|--------|
| Panen lele (per kg) | 25–35 Kredit |
| Kumpulkan telur (per butir) | 3–5 Kredit |
| Panen sayuran (per kg) | 15–25 Kredit |
| Jual maggot berlebih (per 100g) | 8–12 Kredit |
| Jual kompos matang (per kg) | 5–10 Kredit |
| Jual Eco-Enzyme aged (per L) | 15–20 Kredit |
| Selesaikan tantangan klinis | 50–200 Kredit |
| Capai milestone Loop Health | 100–500 Kredit |
| Lulus ujian sertifikasi | 500–1.000 Kredit |

**Pengeluaran:**
| Item | Biaya |
|------|------|
| Pakan komersial (per kg) | 10 Kredit |
| Benih lele (per 20 ekor) | 50 Kredit |
| DOC ayam (per ekor) | 30 Kredit |
| Benih tanaman (per paket) | 5–15 Kredit |
| Starter EM4 (per L) | 25 Kredit |
| Garam Epsom (per 100g) | 15 Kredit |
| Potassium Humate (per 100g) | 20 Kredit |
| Minyak mimba (per 100mL) | 30 Kredit |
| Cuka kayu (per L) | 10 Kredit |
| Ekspansi infrastruktur | 100–1.000 Kredit |

---

## SISTEM 10: JADWAL & RUTINITAS HARIAN

Berdasarkan "Jadwal Harian Ninja (15 Menit/Hari)" dari buku:

| Waktu | Tugas | Aksi Game |
|------|------|-------------|
| **Pagi** | Kumpulkan telur | Klik kotak sarang |
| | Flush galon lele (buka katup bawah bergantian) | Klik katup 1→2→3 |
| | Siram raised bed dengan air buangan lele | Seret gembor ke bedengan |
| | Beri pakan lele (pelet terfermentasi, dosis terhitung) | Takar → campur → tuang |
| | Beri pakan ayam | Isi tempat pakan dengan ransum |
| **Sore** | Tambah sisa dapur ke biopond BSF | Klik untuk menambah |
| | Cacah daun kering → komposter atau deep litter | Klik mesin pencacah → tambah |
| | Pakan sore: lele + ayam | Mirip dengan pagi |
| **Akhir Pekan** | Panen sayuran | Klik tanaman matang |
| | Semprot EE (1:1000) pada semua subsistem | Aksi semprot pada kandang, biopond, tanaman |
| | Pindahkan telur BSF dari kandang kawin ke biopond | Pindahkan bilah kayu bertelur |

**Otomasi Rutinitas (Dapat Dibuka):**
Setelah menyelesaikan tutorial terbimbing, pemain dapat menyewa NPC "Asisten Ninja" yang otomatis menyelesaikan tugas rutin pada efisiensi 80%. Otomasi penuh berbiaya 200 Kredit/minggu.

---

## SISTEM 11: PEMBUAT KASUS KLINIS

Untuk mode tantangan/kelas, pembuat kasus klinis prosedural menciptakan skenario diagnostik:

```
KasusKlinis {
    sistemTerkena:      IDsubsistem
    gejala:             string[] (isyarat terlihat)
    parameterTersembunyi: { namaParam: nilaiAbnormal }
    diagnosisBenar:     IDpenyakit
    pengobatanBenar:    IDpengobatan[]
    batasWaktu:         jam_waktuGame
    kesulitan:          "pemula" | "menengah" | "lanjutan"
    pengalih:           IDpenyakit[] (kondisi yang tampak mirip)
}
```

**Tingkat Kesulitan:**
- **Pemula:** Gejala tunggal, pembacaan parameter jelas, tanpa pengalih
- **Menengah:** Beberapa gejala, pembacaan parameter butuh interpretasi, 1–2 pengalih
- **Lanjutan:** Gejala tumpang tindih dari beberapa sistem, beberapa parameter tersembunyi, butuh deduksi dari informasi parsial

---

*Dokumen Berikutnya: 03-Spesifikasi-Teknis-Roblox.md — Arsitektur Teknis & Implementasi Roblox Studio*
