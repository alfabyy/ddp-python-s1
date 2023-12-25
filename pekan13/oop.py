class Hewan:
    def __init__(self, nama, makanan, habitat, reproduksi):
        self.nama = nama
        self.makanan = makanan
        self.habitat = habitat
        self.reproduksi = reproduksi

class Badak(Hewan):
    def __init__(self, nama, habitat):
        makanan = 'tumbuhan'
        reproduksi = 'vivipar'
        super().__init__(nama, makanan, habitat, reproduksi)
    
    def serang(self):
        return f"{self.nama} Sedang Menyerang!"

    def tidur(self):
        return f"{self.nama} Sedang Tidur!"

class Ikan(Hewan):
    def __init__(self, nama, habitat):
        makanan = 'plankton'
        reproduksi = 'ovipar'
        super().__init__(nama, makanan, habitat, reproduksi)

    def berenang(self):
        return f"{self.nama} Sedang Berenang"

    def mencari(self):
        return f"{self.nama} Sedang Mencari One Piece!"

class Ular(Hewan):
    def __init__(self, nama, habitat):
        makanan = 'mamalia kecil'
        reproduksi = 'ovovivipar'
        super().__init__(nama, makanan, habitat, reproduksi)

    def ngoding(self):
        return f"{self.nama} Sedanng belajar bahasa pemrograman python!"

    def pusing(self):
        return f"{self.nama} Sedang Pusing!"

# Contoh penggunaan:
badak = Badak("Rhino", "Padang Rumput")
print(badak.serang())
print(badak.tidur())

ikan_shanks = Ikan("Shanks", "Laut")
print(ikan_shanks.berenang())
print(ikan_shanks.mencari())

ular = Ular("Black Mamba", "Hutan")
print(ular.ngoding())
print(ular.pusing())
