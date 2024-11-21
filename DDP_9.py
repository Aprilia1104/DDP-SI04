print('-------------celcius ke fahrenheit----------')
def celcius_ke_fahrenheit(celcius):
    print(celcius * 9/5 + 32)

celcius_ke_fahrenheit(0)
celcius_ke_fahrenheit(100)

print('------------mencari bilangan genap----------')
def is_genap (genap):
    print(genap %2 == 0)
is_genap(4)
is_genap(7)

print('-------------keterangan lulus dan tidak lulus---------')
#rata rata nilai kelulusan 70
def skor(nilai):
    if nilai >= 80:
        print('lulus')
    else:
        print('gagal')
skor(80)
skor(60)

print('----------------mencetak bilangan ganjil----------------')
def bilangan_ganjil(ganjil):
    for a in range(1, ganjil+1, 2):
        print(a, end=' ') 
bilangan_ganjil(20)


