from gempa import *

# membuat objek
gempa1 = gempa("Banten", 1.2)
gempa2 = gempa("Palu", 6.1)
gempa3 = gempa("Cianjur", 5.6)
gempa4 = gempa("Jayapura", 3.3)
gempa5 = gempa("Garut", 4.0)


# Info gempa
print("-------------Info Gempa dengan skala-----------")
print()
gempa1.dampak()

print("-------------Info Gempa dengan skala-----------")
print()
gempa2.dampak()

print("-------------Info Gempa dengan skala-----------")
print()
gempa3.dampak()

print("-------------Info Gempa dengan skala-----------")
print()
gempa4.dampak()

print("-------------Info Gempa dengan skala-----------")
print()
gempa5.dampak()

