lista = [20,12,101,23,76,44,89,102]
print(lista)
print("***********************************")
#lista.sort() #sorbarendezes novekvo sorba
lista.sort(reverse=True) #csokkeno sorrend
print(lista)
print("************************************")
print(max(lista))
print("************************************")
print(min(lista))
print("************************************")
print(sum(lista))

szorzat = 1
for i in range(len(lista)):
    szorzat = szorzat * lista[i]
print(szorzat)