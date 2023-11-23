import random

angka_maksimal = 10
angka_minimal = 1

print("Pikirkan angka antara", angka_minimal, "dan", angka_maksimal)
input("Tekan Enter ketika Anda siap untuk bermain...")

while True:

    print(f"Apakah angka yang anda pikirkan <= 10?")
    jawaban = input("Jawab (y/t): ")
    if jawaban.lower() == 'y':

        print(f"Apakah angka yang anda pikirkan <= 5?")
        jawaban = input("Jawab (y/t): ")

        if jawaban.lower() == 'y':
            print("Apakah angka yang anda pikirkan bersifat ganjil?")
            jawaban = input("Jawab (y/t): ")

            if jawaban.lower() == 'y' :
                print("Apakah angka yang anda pikirkan adalah bilangan ganjil terkecil dari 1-5?")
                jawaban = input("Jawab (y/t): ")
                if jawaban.lower() == 'y' :
                    print("Angka yang anda pilih adalah 1")
                    break

                elif jawaban.lower() == 't' :
                    print("Apakah angka yang anda pikirkan adalah bilangan ganjil terbesar dari 1-5?")
                    jawaban = input("Jawab (y/t): ")
                    if jawaban.lower() == 'y' :
                        print("Angka yang anda pilih adalah 5") 
                        break
                    elif jawaban.lower() == 't' :
                        print("Angka yang anda pilih adalah 3")
                        break

            elif jawaban.lower() == 't' :
                print("Apakah angka yang anda pikirkan adalah bilangan genap terkecil dari 1-5?")
                jawaban = input("Jawab (y/t): ")
                if jawaban.lower() == 'y' :
                    print("Angka yang anda pilih adalah 2") 
                    break
                elif jawaban.lower() == 't' :
                    print("Angka yang anda pilih adalah 4")
                    break


        elif jawaban.lower() == 't':
            print("Apakah angka yang anda pikirkan bersifat genap?")
            jawaban = input("Jawab (y/t): ")
            if jawaban.lower() == 'y' :
                print("Apakah angka yang anda pikirkan adalah bilangan genap terkecil dari 6-10?")
                jawaban = input("Jawab (y/t): ")
                if jawaban.lower() == 'y' :
                    print("Angka yang anda pilih adalah 6")
                    break

                elif jawaban.lower() == 't' :
                    print("Apakah angka yang anda pikirkan adalah bilangan ganjil terbesar dari 6-10?")
                    jawaban = input("Jawab (y/t): ")
                    if jawaban.lower() == 'y' :
                        print("Angka yang anda pilih adalah 10") 
                        break

                    elif jawaban.lower() == 't' :
                        print("Angka yang anda pilih adalah 8")
                        break

            elif jawaban.lower() == 't' :
                print("Apakah angka yang anda pikirkan adalah bilangan ganjil terkecil dari 6-10?")
                jawaban = input("Jawab (y/t): ")
                if jawaban.lower() == 'y' :
                    print("Angka yang anda pilih adalah 7") 
                    break
                
                elif jawaban.lower() == 't' :
                    print("Angka yang anda pilih adalah 9") 
                    break    

    elif jawaban.lower() == 't' :
        print("Apakah angka yang anda pikirkan => 16?")
        jawaban = input("Jawab (y/t): ")
        if jawaban.lower() == 'y' :
            print("Apakah angka yang anda pikirkan adalah bilangan genap terkecil dari 16-20?")
            jawaban = input("Jawab (y/t): ")


