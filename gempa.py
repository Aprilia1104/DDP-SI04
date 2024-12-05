class gempa:
    lokasi = ""
    skala = ""
    #konstruktor inisialisasi atribut
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
        
    # method penentu skala gempa
    def dampak(self):
        #logika/statement
        if self.skala < 2:
            print("Gempa Tidak Berasa")
        elif 2 >= self.skala <= 4:
            print("Gempa Berdampak Bangunan Retak")
        elif 4 >= self.skala <= 6:
            print("Gempa Berdampak Bangunan Rubuh")
        elif self.skala > 6:
            print("Gampa Besar Berpotensi Tsunami")
        
    # Menampilkan Lokasi skala gempa
        print(f"Lokasi Gempa: {self.lokasi}")
        print(f"Lokasi Gempa: {self.skala}")