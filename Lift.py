print("2.feladat")
utasok_tomege=[72,85,64,91,58,103,77,69,88,95,60,81]
ossztomeg=0
sorsz=0
van=False
teherb=int(input("A lift teherbírása (kg): "))
for i in range(len(utasok_tomege)):
    sorsz+=1
    ossztomeg+=utasok_tomege[i]
    if 100<utasok_tomege[i]:
        print(f"Az első 100 kg feletti utas: {sorsz}. ({utasok_tomege[i]} kg)")
        van=True
if van==False:
        print("Nincs 100 kg feletti utas")
if ossztomeg<=teherb:
    print("Mindenki elfér.")
else:
    print(f"Az összes tömeg {ossztomeg} kg. Nem fér el mindenki.")

