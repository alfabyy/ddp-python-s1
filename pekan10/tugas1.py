def lulus(hasil_akhir):
    nama = [siswa["nama"] for siswa in hasil_akhir if siswa["nilai"] > 65]
    return nama

hasil_akhir = [
    {"nama": "Reza", "nilai": 70},
    {"nama": "Ciut", "nilai": 63},
    {"nama": "Dian", "nilai": 80},
    {"nama": "Badu", "nilai": 40}
]

hasil_lulus = lulus(hasil_akhir)
print("Siswa yang lulus :", hasil_lulus)
