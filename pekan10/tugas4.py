def konsonan(string):
    huruf_konsonan = ""
    huruf_vocal = 'aeiouAEIOU'

    for huruf in string:
        if 'a' <= huruf <= 'z' or 'A' <= huruf <= "Z" :
            if huruf not in huruf_vocal :
                huruf_konsonan += huruf

    return huruf_konsonan

kalimat = "Nurul Fikri"

hasil = konsonan(kalimat)
print("Hasil :", hasil)
