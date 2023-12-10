import module1

print("""
Keterangan Bilangan Bangun Datar :
      
Persegi = 1
Persegi Panjang = 2
Segitiga = 3
Lingkaran = 4
Trapesium = 5
Jajargenjang = 6
Layang-layang = 7
""")

pilih = int(input("Pilih Bilangan Bangun Datar : "))

if pilih == 1 :
    nilai = int(input("Masukkan Sisi : "))
    module1.persegi(nilai)

elif pilih == 2 :
    nilai1 = int(input("Masukkan Panjang : "))
    nilai2 = int(input("Masukkan Lebar : "))
    module1.persegi_panjang(nilai1,nilai2)

elif pilih == 3 :
    alas = int(input("Masukkan Alas : "))
    tinggi = int(input("Masukkan Tinggi : "))
    sisi1 = int(input("Masukkan Sisi 1 : "))
    sisi2 = int(input("Masukkan Sisi 2 : "))
    sisi3 = int(input("Masukkan Sisi 3 : "))
    module1.segitiga(alas,tinggi,sisi1,sisi2,sisi3)

elif pilih == 4 :
    jari2 = int(input("Masukkan Jari-jari : "))
    module1.lingkaran(jari2)

elif pilih == 5 :
    a = int(input("Masukkan Sisi A : "))
    b = int(input("Masukkan Sisi B : "))
    c = int(input("Masukkan Sisi C : "))
    d = int(input("Masukkan Sisi D : "))
    tinggi = int(input("Masukkan Tinggi : "))
    module1.trapesium(a,b,c,d,tinggi)

elif pilih == 6 :
    alas = int(input("Masukkan Alas : "))
    tinggi = int(input("Masukkan Tinggi : "))
    sisi1 = int(input("Masukkan Sisi 1 : "))
    sisi2 = int(input("Masukkan Sisi 2 : "))
    module1.jajargenjang(alas,tinggi,sisi1,sisi2)

elif pilih == 7 :
    d1 = int(input("Masukkan Diagonal 1 : "))
    d2 = int(input("Masukkan Diagonal 2 : "))
    sisi1 = int(input("Masukkan Sisi 1 : "))
    sisi2 = int(input("Masukkan Sisi 2 : "))
    module1.layang_layang(d1,d2,sisi1,sisi2)

else :
    print("Bilangan tidak valid")

