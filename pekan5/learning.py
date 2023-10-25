print("""
=====================================================================      
Sistem Penghitung Berat Badan Ideal

Pilih Jenis kelamin :
1 = Laki-laki
2 = Perempuan             
""")

# bb = int(input("Masukkan Berat Badan : "))
jk = int(input("Masukkan Jenis Kelamin : "))
tb = int(input("Masukkan Tinggi Badan : "))

match jk:
    case 1:
        ideal = (tb - 100) - (tb - 100) * 0,1
        print("Berat badan ideal laki-laki adalah untuk tinggi", tb, "adalah", ideal)

    case 2:
        ideal = (tb - 100) - (tb - 100) * 0,15
        print("Berat badan ideal perempuan adalah untuk tinggi", tb, "adalah", ideal)

    case _:
        print("Pilihan yang anda masukkan tidak valid.")    
    


