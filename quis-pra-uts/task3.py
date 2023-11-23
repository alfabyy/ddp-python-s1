# for loop in range(1,21):
#     if loop % 3 == 0:
#         print("STT Nurul Fikri")
#     else:
#         print(loop)    

# for angka in range(1, 31):
#     if angka % 6 == 0:
#         print("Buzz")
#     elif angka % 3 == 0:
#         print("Fizz")
#     else:
#         print(angka)

# def is_prime(num):
#     if num <= 1:
#         return False
#     if num <= 3:
#         return True
#     if num % 2 == 0 or num % 3 == 0:
#         return False
#     i = 5
#     while i * i <= num:
#         if num % i == 0 or num % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# count = 1
# for angka in range(1, 51):
#     if is_prime(angka):
#         if count % 2 == 1:
#             print("Fizz")
#         else:
#             print("Buzz")
#         count += 1
#     else:
#         print(angka)

# while True:
#     luas = int(input("Masukkan luas : ")) 

#     if luas < 3 and luas > 0:
#         print("Luas tidak memenuhi, silakan coba lagi. ketik 0 untuk berhenti")

#     elif luas == 0 :
#         break    

#     else:
#         for i in range(1, luas + 1, 2):
#             print(" " * ((luas - i) // 2) + "*" * i)

#         for i in range(luas - 2, 0, -2):
#             print(" " * ((luas - i) // 2) + "*" * i)
#         break  

