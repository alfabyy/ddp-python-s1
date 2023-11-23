print("""
Kalkulator Sederhana
      
Keterangan Operator :
1. + : Ditambah
2. - : Dibagi
3. * : Dikali
4. / : Dibagi
5. ** : Pangkat
""")

bil1 = int(input("Masukkan bilangan 1 : "))
bil2 = int(input("Masukkan bilangan 2 : "))
operator = input("Masukkan Operator : ")

if operator == "+" or operator.lower() == "tambah" :
    hasil = bil1 + bil2
    print(bil1, "+" , bil2 , "=" , int(hasil))

elif operator == "-" or operator.lower() == "kurang" :
    hasil = bil1 - bil2
    print(bil1, "-" , bil2 , "=" , int(hasil))

elif operator == "*" or operator.lower() == "kali" :
    hasil = bil1 * bil2
    print(bil1, "*" , bil2 , "=" , int(hasil))

elif operator == "/" or operator.lower() == "bagi" :
    hasil = bil1 / bil2
    print(bil1, "/" , bil2 , "=" , round(hasil, 2))

elif operator == "**" or operator.lower() == "pangkat" :
    hasil = bil1 ** bil2
    print(bil1, "**" , bil2 , "=" , round(hasil))    

else :
    print("Operator tidak diketahui")
