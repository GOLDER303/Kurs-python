import sys

infoOPizzy = []

for i in range(1, len(sys.argv)):
    infoOPizzy.append(sys.argv[i])

def porownaj(cena, rozmiar):
    rozmiar, cena = float(rozmiar), float(cena)
    polePizzy = 3.14 * (rozmiar/2)**2
    return polePizzy / cena


print(f"Restauracja: {infoOPizzy[0]} pizza: {infoOPizzy[1]}, rozmiar: {infoOPizzy[2]}, cena: {infoOPizzy[3]}")
print(f"Restauracja: {infoOPizzy[4]} pizza: {infoOPizzy[5]}, rozmiar: {infoOPizzy[6]}, cena: {infoOPizzy[7]}")
print(f"Restauracja: {infoOPizzy[8]} pizza: {infoOPizzy[9]}, rozmiar: {infoOPizzy[10]}, cena: {infoOPizzy[11]}")

listaStosunkow = []

for i in range(2, len(sys.argv), 4):
    listaStosunkow.append(porownaj(infoOPizzy[i], infoOPizzy[i+1]))

najlepszyStosunek = listaStosunkow.index(min(listaStosunkow)) + 1

print(f"Najleszpy stosunek ma pizza nr. {najlepszyStosunek}")