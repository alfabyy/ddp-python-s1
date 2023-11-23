nama = input("Masukkan Nama Pembeli : ")
no_hp = input("Masukkan No Hp Pembeli : ")
jenis_pesanan = input("Pesan Menu Apa? (Makanan atau Minuman) : ")

menu_makanan = {
    "Nasi Goreng": 15000,
    "Mie Goreng": 12000,
    "Ayam Geprek": 18000
}

menu_minuman = {
    "Aneka Jus": 15000,
    "Soft Drink": 10000,
    "Sweet Ice Tea": 5000
}

jenis_pesanan = jenis_pesanan.lower() 

if jenis_pesanan == "makanan":
    menu = menu_makanan
elif jenis_pesanan == "minuman":
    menu = menu_minuman
else:
    print("Jenis pesanan tidak tersedia")
    exit()

print("Menu yang Tersedia:")
for item, harga in menu.items():
    print(f"{item} - Rp. {harga}")

pesanan = input("Masukkan pesanan: ").title() 
jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))

harga_pesanan = menu.get(pesanan)
if harga_pesanan is not None:
    total_harga = harga_pesanan * jumlah_pesanan

    print("================================ Struk Pembelian ===============================")
    print("Nama Pembeli\t :", nama)
    print("No Hp Pembeli\t :", no_hp)
    print("Menu yang di Pesan :", pesanan)
    print("Jumlah Pesanan\t :", jumlah_pesanan)
    print("Harga yang harus dibayarkan : Rp.", total_harga)
    print("================================================================================")
else:
    print("Menu tidak tersedia")

