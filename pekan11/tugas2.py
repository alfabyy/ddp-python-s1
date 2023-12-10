import module2

print("""
Keterangan Jenis Aritmatika

1. Tambah = +
2. Kurang = -
3. Kali = *
4. Bagi = /
5. Pangkat = **
6. Modulus = %
7. Pembagian Bulat = //
""")

pilih = int(input("Masukkan Jenis Aritmatika : "))

if pilih == 1 :
    bil1 = int(input("Masukkan Bilangan 1 : "))
    bil2 = int(input("Masukkan Bilangan 2 : "))
    print(bil1, "+" , bil2 , "=" ,module2.tambah(bil1,bil2))

elif pilih == 2 :
    bil1 = int(input("Masukkan Bilangan 1 : "))
    bil2 = int(input("Masukkan Bilangan 2 : "))
    print(bil1, "-" , bil2 , "=" ,module2.kurang(bil1,bil2))


elif pilih == 3 :
    bil1 = int(input("Masukkan Bilangan 1 : "))
    bil2 = int(input("Masukkan Bilangan 2 : "))
    print(bil1, "*" , bil2 , "=" ,module2.kali(bil1,bil2))


elif pilih == 4 :
    bil1 = int(input("Masukkan Bilangan 1 : "))
    bil2 = int(input("Masukkan Bilangan 2 : "))
    print(bil1, "/" , bil2 , "=" ,module2.bagi(bil1,bil2))

elif pilih == 5 :
    bil1 = int(input("Masukkan Bilangan : "))
    bil2 = int(input("Masukkan Pangkat : "))
    print(bil1, "**" , bil2 , "=" ,module2.pangkat(bil1,bil2))

elif pilih == 6 :
    bil1 = int(input("Masukkan Bilangan 1 : "))
    bil2 = int(input("Masukkan Bilangan 2 : "))
    print(bil1, "%" , bil2 , "=" ,module2.modulus(bil1,bil2))

elif pilih == 7 :
    bil1 = int(input("Masukkan Bilangan 1 : "))
    bil2 = int(input("Masukkan Bilangan 2 : "))
    print(bil1, "//" , bil2 , "=" ,module2.pembagian_bulat(bil1,bil2))

elif pilih == 8 :
    sudut = float(input("Masukkan nilai sudut dalam derajat : "))
    hasil = module2.sin(sudut)
    print("Nilai sin",sudut,"adalah : ",round(hasil,4))

elif pilih == 9 :
    sudut = float(input("Masukkan nilai sudut dalam derajat : "))
    hasil = module2.cos(sudut)
    print("Nilai sin",sudut,"adalah : ",round(hasil,4))

elif pilih == 10 :
    sudut = float(input("Masukkan nilai sudut dalam derajat : "))
    hasil = module2.tan(sudut)
    print("Nilai sin",sudut,"adalah : ",round(hasil,4))