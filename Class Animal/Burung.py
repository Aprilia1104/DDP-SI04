from Animal import *

class Burung(Animal):
   def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
       super().__init__(nama, makanan, hidup, berkembang_biak)
       self.jenis_bulu = jenis_bulu
       self.bunyi = bunyi
       
   def cetak_burung(self):
       super().cetak()
       print(f'Hewan ini berbulu {self.jenis_bulu} dan hewan ini berbunyi {self.bunyi}')
 
print('-------------------- Objek Burung Beo-----------------------')      
beo = Burung('Burung Beo', 'biji-bijian', 'udara', 'bertelur' ,'blue and orange', 'kamu jelek')
beo.cetak_burung()

print('------------------ Objek Burung Kaka Tua ----------------------')
kakaTua = Burung('Burung Kaka Tua', 'Buah-buahan', 'udara', 'Bertelur', 'white', 'ngak ngak ngak')
kakaTua.cetak_burung()
