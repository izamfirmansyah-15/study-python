keranjang = [
    {"nama": "Obat Batuk", "qty": 3, "harga": 15000},
    {"nama": "Obat Batuk", "qty": 3, "harga": 15000},
    {"nama": "Paracetamol", "qty": 2, "harga": 8000},
    {"nama": "Vitamin C", "qty": 1, "harga": 32000},
]
total = sum(i["qty"] * i["harga"] for i in keranjang)
print("==============================")
print("Barang yang dibeli: ",keranjang[0]["qty"],keranjang[0]["nama"],"dan",keranjang[1]["qty"],keranjang[1]["nama"],"dan",keranjang[2]["qty"],keranjang[2]["nama"],"dan",keranjang[3]["qty"],keranjang[3]["nama"])
print("Total harga: ",total)