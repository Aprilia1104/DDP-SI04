from Animal import *

class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_ikan = warna_ikan
        self.jenis_ikan = jenis_ikan
        
    def cetak_ikan(self):
        super().cetak()
        print(f'Warna ikan ini adalah warna {self.warna_ikan} dan hewan ini jenisnya ikan {self.jenis_ikan}')

print('--------------------------- Objek Ikan Nemo------------------------')        
nemo = ikan('ikan nemo', 'plankton', 'air', 'bertelur', 'orange', 'air laut')
nemo.cetak_ikan()

print('------------------------ Objek Ikan Lele -----------------------')
lele = ikan('ikan lele', 'pelet', 'air', 'bertelur', 'hitam', 'air tawar')
lele.cetak_ikan()