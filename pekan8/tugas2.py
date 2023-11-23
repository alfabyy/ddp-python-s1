def keterangan(nilai):
    if nilai < 60:
        return "Gagal"
    elif nilai >= 61 and nilai <= 70:
        return "Baik"
    elif nilai >= 71 and nilai <= 80:
        return "Sangat Baik"
    elif nilai >= 81 and nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai tidak valid"

# Contoh penggunaan fungsi
nilai_mahasiswa = int(input("Masukkan nilai mahasiswa : "))
status = keterangan(nilai_mahasiswa)
print("Keterangan\t\t :", status)
