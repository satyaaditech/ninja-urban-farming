import os

filepath = "/Users/satyaadidharma/Urban Farming/Ninja-Urban-Farming.md"

replacements = {
    "**[Diagram 0.1:": """
```mermaid
graph TD
    D[Dapur / Sampah Organik] --> B[Biopond Maggot BSF]
    B --> L[Pakan Lele & Ayam]
    L --> K[Kotoran Lele & Ayam]
    K --> R[Raised Bed Sayuran / Pupuk]
    R --> S[Sayur Segar, Telur, Ikan]
    S --> D
    
    style D fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style L fill:#bfb,stroke:#333,stroke-width:2px
    style K fill:#fbb,stroke:#333,stroke-width:2px
    style R fill:#dfd,stroke:#333,stroke-width:2px
    style S fill:#ff9,stroke:#333,stroke-width:2px
```
""",
    "**[Gambar 2.1:": "![Tampak Atas Zonasi Lahan 75 m²](/Users/satyaadidharma/.gemini/antigravity-ide/brain/75af8033-f434-4a5d-ae54-79ace37cc612/zonasi_lahan_1781050545241.png)",
    "**[Diagram 3.1:": """
```mermaid
graph TD
    A[Aerator 18W] --> M{Manifold 4 Cabang}
    M -->|Cabang 1| G1[Galon 1: Batu Aerasi]
    M -->|Cabang 2| G2[Galon 2: Batu Aerasi]
    M -->|Cabang 3| G3[Galon 3: Batu Aerasi]
    M -->|Cabang 4| B[Bleeding Valve: Udara Bebas]
    G1 -.-> K1[Keran Drainase Bawah 1]
    G2 -.-> K2[Keran Drainase Bawah 2]
    G3 -.-> K3[Keran Drainase Bawah 3]
```
""",
    "**[Diagram 4.1:": """
```mermaid
graph LR
    SD[Sampah Dapur] --> BSF[Biopond BSF]
    BSF -->|Maggot| P[Pakan Ternak]
    P --> KT[Kotoran Ternak]
    KT --> PT[Pupuk Tanaman]
    PT --> S[Sayur & Dapur]
    S -.-> SD
```
""",
    "**[Diagram 4.2:": """
```mermaid
graph LR
    Substrat[Substrat Organik / Maggot] -->|Merayap Naik| Ramp[Ramp Kemiringan 45 Derajat]
    Ramp --> Lubang[Lubang Pengeluaran]
    Lubang --> Panen[Wadah Panen Otomatis]
```
""",
    "**[Gambar 6.1:": "![Galon Bioflok](/Users/satyaadidharma/.gemini/antigravity-ide/brain/75af8033-f434-4a5d-ae54-79ace37cc612/galon_bioflok_1781050525548.png)",
    "**[Gambar 12.5:": "![Virus Gemini pada Cabai](/Users/satyaadidharma/.gemini/antigravity-ide/brain/75af8033-f434-4a5d-ae54-79ace37cc612/virus_gemini_cabai_1781050534779.png)",
    "**[Gambar 11.1:": """
```mermaid
graph TD
    Start[Gejala Lele Sakit?] --> Q1{Apakah Menggantung di Permukaan?}
    Q1 -->|Ya| A[Klinis A / B / C]
    Q1 -->|Tidak| Q2{Apakah Ada Luka Fisik/Kumis Putus?}
    Q2 -->|Ya| D[Klinis D / E]
    Q2 -->|Tidak| Q3{Apakah Perut Buncit / Kumis Keriting?}
    Q3 -->|Ya| F[Klinis F / G / H]
    Q3 -->|Tidak| Z[Pantau Kualitas Air]
```
""",
    "**[Gambar 12.1:": """
```mermaid
graph TD
    Start[Gejala Tanaman Sakit?] --> Q1{Apakah Daun Layu/Kuning?}
    Q1 -->|Ya| A[Klinis A / B: Cek Akar & Batang]
    Q1 -->|Tidak| Q2{Apakah Daun Berlubang/Dimakan?}
    Q2 -->|Ya| C[Klinis C: Hama Ulat/Belalang]
    Q2 -->|Tidak| Q3{Apakah Ada Bercak Jamur/Virus?}
    Q3 -->|Ya| D[Klinis D / E / F: Cek Bentuk Bercak]
    Q3 -->|Tidak| Z[Pantau Nutrisi & Air]
```
"""
}

with open(filepath, 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    replaced = False
    for key, value in replacements.items():
        if line.strip().startswith(key):
            new_lines.append(value + "\n")
            replaced = True
            break
    if not replaced:
        new_lines.append(line)

with open(filepath, 'w') as f:
    f.writelines(new_lines)

print("Visuals injected successfully!")
