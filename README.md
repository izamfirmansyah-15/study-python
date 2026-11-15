# Latihan Python — Izam

Repositori latihan belajar Python (backend-first).
Tiap file = satu latihan dari roadmap. Tidak ada kode produksi di sini.

## Struktur

```
belajar-python/
├── requirements.txt   # paket yang dipakai (dari venv)
├── tipe.py            # Tahap 1.1 — variabel & tipe data
├── keranjang.py       # Tahap 1.2-1.3 — list/dict + fungsi
├── belanja.py         # Tahap 1.4 — file JSON + error handling
└── .venv/             # tidak di-commit
```

## Cara menjalankan

```bash
cd ~/hermes/belajar-python
source .venv/bin/activate
python3 tipe.py
```

## Setup ulang (kalau di mesin lain)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
