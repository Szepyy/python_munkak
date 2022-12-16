# szoveg = "ez egy szöveg"
# if "v" in szoveg:
#     print("benne van")
# else: print("nincs benne")

# szoveg = "ez egy szoveg"
# beker = input("Kérem a betűt!")
# if beker in szoveg:
#     print(f"{beker} betű benne van a szövegben")
# else: print(f"{beker} betű nincs benne a szövegben")    

# szoveg = "KEDD"
# print(szoveg.lower())



hetnapjai = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]
# print(hetnapjai)
# for i in range(len(hetnapjai)):
#     hetnapjai[i] = hetnapjai[i].lower()
# hetnapjai_kisbetu = [item.upper() for item in hetnapjai]
# hetnapjai_nagybetu = [item.lower() for item in hetnapjai]

# beker = input("Kérem a napot! ").upper()

# if beker in hetnapjai_kisbetu: 
#     print(f"{beker} nap benne van a listában")
# else:
#     print(f"{beker} nap nincs benne a listában")



autok = ["Bmw","Toyota","Audi","Nissan","Volvo"]
autok_kisbetu = [item.upper() for item in autok]
autok_nagybetu = [item.lower() for item in autok]

beker = input("Kérem az autómárkát").upper()

if beker in autok_kisbetu:
    print(f"{beker} autómárka benne van a listában")
else:
    print(f"{beker} autómárka nincs benne a listában")