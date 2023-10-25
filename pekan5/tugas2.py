ket = ["1 adalah persegi" , "2 adalah lingkaran" , "3 adalah segitiga"]

for k in ket :
    print(k)

luas_bangun_datar = int(input("Masukkan kode untuk menghitung luas bangun datar : "))

match luas_bangun_datar:
    case 1:
        panjang_sisi = int(input("Masukkan sisi persegi : "))
        hasil3 = panjang_sisi * panjang_sisi
        print("Luas persegi adalah : ", hasil3)

    case 2:
        jari_jari = int(input("Masukkan jari-jari lingkaran"))
        hasil2 = 3.14 * jari_jari * jari_jari
        print("Luas lingkaran adalah : ", hasil2)    

    case 3:
        alas = int(input("Masukkan alas segitiga : "))
        tinggi = int(input("Masukkan tinggi segitiga : "))
        hasil = 0.5 * alas * tinggi
        print("Luas segitiga adalah : ", hasil)

    case _:
        print("Kode yang anda masukkan tidak valid.")    
    

        