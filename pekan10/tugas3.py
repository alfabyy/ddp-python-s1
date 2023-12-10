def duplikasi(buah):
    buah_duplikasi = []

    for buah_kedua in buah:
        buah_duplikasi += [buah_kedua, buah_kedua]

    return buah_duplikasi

buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

hasil = duplikasi(buah)
print("Buah :", hasil)
