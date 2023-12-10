def balikan(daftar_buah):
    buah_terbalik = []

    jumlah = 0
    for buah in daftar_buah:
        jumlah += 1

    for i in range(jumlah - 1, -1, -1):
        buah_terbalik.append(daftar_buah[i])

    return buah_terbalik

daftar_buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

hasil = balikan(daftar_buah)
print("Urutan terbalik dari buah-buahan:", hasil)


