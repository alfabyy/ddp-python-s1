def persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    print("Luas Persegi : ", luas)
    print("Keliling Persegi :", keliling)

def persegi_panjang(panjang,lebar):
    luas = panjang * lebar
    keliling = 2 * panjang + lebar
    print("Luas Persegi Panjang : ", luas)
    print("Keliling Persegi Panjang : ", keliling)

def segitiga(alas,tinggi,sisi1,sisi2,sisi3):
    luas = 0.5 * alas * tinggi
    keliling = sisi1 + sisi2 + sisi3
    print("Luas Segitiga : ", luas)
    print("Keliling Segitiga : ", keliling)

def lingkaran(jari2):
    phi = 3.14
    luas = phi * jari2 * jari2
    keliling = 2 * phi * jari2
    print("Luas Lingkaran : ", round(luas,2))
    print("Keliling Lingkaran : ", round(keliling,2))

def trapesium(a,b,c,d,tinggi):
    luas = 0.5 * a + b * tinggi
    keliling = a + b + c + d
    print("Luas Trapesium : ", luas)
    print("Keliling Trapesium : ", keliling)

def jajargenjang(alas,tinggi,sisi1,sisi2):
        luas = alas * tinggi
        keliling = 2 * sisi1 + sisi2
        print("Luas Jajargenjang : ", luas)
        print("Keliling Jajargenjang : ", keliling)

def layang_layang(d1,d2,s1,s2):
     luas = 0.5 * d1 * d2
     keliling = 2 * s1 + s2
     print("Luas Layang-layang : ", luas)
     print("Keliling Layang-layang : ", keliling)

   