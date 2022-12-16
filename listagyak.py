lista = []

#lista.append()
lista.append("MW2")
lista.append("GTA")
lista.append("PUBG")
lista.append("MINECRAFT")
lista.append("FIFA")
#1.
print(lista)

print("*********************************************")

#2.
for item in lista:
    print(item)

print("********************************************")

#len
#3.
for i in range(len(lista)):
    print(lista[i])
print("*********************************************")
#szűrés
for item in lista:
    if item == "MW2":
        print("IGEN")
    else:
        print("NEM")





















