class Gempa:
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
    
    def dampak(self):
        if self.skala < 2:
            print("Dampak Gempa : Tidak terasa di wilayah", self.lokasi)
        elif 2 <= self.skala < 4:
            print("Dampak Gempa : Bangunan retak-retak di wilayah", self.lokasi)
        elif 4 <= self.skala < 6:
            print("Dampak Gempa : Bangunan roboh di wilayah", self.lokasi)
        else:
            print("Dampak Gempa : Bangunan roboh dan berpotensi tsunami di wilayah", self.lokasi)
