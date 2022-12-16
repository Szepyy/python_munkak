import random


lista = []

#feltoltjuk a listat random szamokkal
for i in range(10): #10 db szamlesz a listaban
    lista.append(random.randint(1,100))
#print(lista)

#irjuk ki a 10nel nagyobb szamokat
for i in range(len(lista)):
    if lista[i] >= 10:
        print(lista[i])

for i in  range(len(lista)):
    if lista[i] <= 10:
        print(lista[i])































