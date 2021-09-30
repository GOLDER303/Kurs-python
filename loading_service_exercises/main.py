max_elements_count = int(input("Podaj maksymalną liczbę elementów do wysyłki: "))

sended_packs = 0
empty_kg = 0
weight_most_empty_pack = 0;
transport_weight = 0
i = 0
not_send_pack = 0
package = 0

while(i < max_elements_count):
    if(not_send_pack != 0):
        transport_weight += not_send_pack
        not_send_pack = 0

    package = int(input("Podaj ciężar paczki: "))
    if(package <= 10 and package >= 1):
        transport_weight += package
    else:
        while(package > 10 or package < 1):    
            print("Ciężar paczki musi mieścić się pomiędzy 1 a 10")
            package = int(input("Podaj ciężar paczki: "))
        transport_weight += package
        
    print("check")
    if(transport_weight > 20):
        transport_weight -= package
        not_send_pack = package
        sended_packs += 1
        empty_kg = empty_kg + (20 - package)
        transport_weight = 0

        if((20 - package) > weight_most_empty_pack):
            weight_most_empty_pack = package

    elif(transport_weight == 20):
        sended_packs += 1
        transport_weight = 0

    i += 1
    if(i == max_elements_count):
        sended_packs += 1
        empty_kg += (20 - transport_weight)
        if((20 - package) > weight_most_empty_pack):
            weight_most_empty_pack = 20 - transport_weight

sended_kg = sended_packs * 20 - empty_kg 

print(f"Wysłanych paczek: {sended_packs}")
print(f"Wysłanych pustych kilokramów: {empty_kg}")
print(f"Wysłanych kilogramów: {sended_kg}")
print(f"Największa liczba pustych kilokramów w paczce: {weight_most_empty_pack}")



'''
Liczbę paczek wysłanych
Liczbę kilogramów wysłanych
Suma "pustych" - kilogramów (brak optymalnego pakowania). 
Liczba paczek * 20 - liczba kilogramów wysłanych
Która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik
Program powinien kończyć się z błędem, gdy element dodawany ma więcej niż 10kg, lub mniej niż 1 kg i nie był dokładnie równy 0.
'''