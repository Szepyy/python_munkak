
lista = [10, 3, 6, 5, 3, 10, 9]

db = 0
for i in range(len(lista)):
    if lista[i] == 3:
        db = db + 1 #egyesevel megszamoljuk a listat tartalmat (csaka 3as)
print(db)

#osszegzes tetele
osszeg = 0
for i in range(len(lista)):                                            
    osszeg =osszeg + lista[i]
print(osszeg)

#szorzas tetele

szorzat = 1
for i in range(len(lista)):                                            
    szorzat = szorzat + lista[i]
print(szorzat)

print(max(lista))
print(min(lista))















