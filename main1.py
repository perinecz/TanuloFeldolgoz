#0
print("Tanulok feldolgozása.")

#1
tanulok = []
while True:
    print("\nKérem a tanuló adatait:")
    nev = input("Tanuló neve: ")
    szId = input("Születési ideje: ")
    magassag = int(input("Magasság: "))

    tanulo =(nev, szId, magassag)
    tanulok.append(tanulo)

    valasz = input("További tanulo (igen/nem): ")
    if valasz.lower() != 'igen':
        break

#2


#3 Hozzáférés listaelem segítségével.
print("\nTanulók listája\n")
for item in tanulok:
    print(f"Név: {item[0]}, születési ideje: {item[1]}, magasság: {item[2]}")