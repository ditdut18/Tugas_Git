

for kode_lokasi, info in data_panen.items():
    print("Kode:", kode_lokasi)
    print("Nama Lokasi:", info["nama_lokasi"])
    print("Hasil Panen:", info["hasil_panen"])
    print("-" * 30)

print("Jagung lokasi2:",
      data_panen["lokasi2"]["hasil_panen"]["jagung"])
print("Nama lokasi3:",
      data_panen["lokasi3"]["nama_lokasi"])


padi_lokasi1 = data_panen["lokasi1"]["hasil_panen"]["padi"]
kedelai_lokasi1 = data_panen["lokasi1"]["hasil_panen"]["kedelai"]

padi_lokasi2 = data_panen["lokasi2"]["hasil_panen"]["padi"]
kedelai_lokasi2 = data_panen["lokasi2"]["hasil_panen"]["kedelai"]

padi_lokasi3 = data_panen["lokasi3"]["hasil_panen"]["padi"]
kedelai_lokasi3 = data_panen["lokasi3"]["hasil_panen"]["kedelai"]

padi_lokasi4 = data_panen["lokasi4"]["hasil_panen"]["padi"]
kedelai_lokasi4 = data_panen["lokasi4"]["hasil_panen"]["kedelai"]

padi_lokasi5 = data_panen["lokasi5"]["hasil_panen"]["padi"]
kedelai_lokasi5 = data_panen["lokasi5"]["hasil_panen"]["kedelai"]


for kode_lokasi, info in data_panen.items():
    padi = info["hasil_panen"]["padi"]
    jagung = info["hasil_panen"]["jagung"]
    

    if padi > 1300 or jagung > 800:
        print(info["nama_lokasi"], "memerlukan perhatian khusus")
    else:
        print(info["nama_lokasi"], "dalam kondisi baik")
