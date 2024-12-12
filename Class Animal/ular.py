from Animal import *

class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_ular, warna_ular):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_ular = jenis_ular
        self.warna_ular = warna_ular
        
        
    def cetak_ular(self):
        super().cetak()
        print(f'jenis ular ini adalah ular {self.jenis_ular} dan ular ini berwarna {self.warna_ular}')
        
print('--------------------------- Objek ular sanca ------------------------')        
sanca = ular('ular sanca', 'hewan kecil', 'darat', 'bertelur', ' tidak berbisa', 'cokelat')
sanca.cetak_ular()

print('------------------------ Objek ular cobra -----------------------')
cobra = ular('ular cobra', 'daging', 'darat', 'bertelur', 'berbisa', 'hitam')
cobra.cetak_ular()