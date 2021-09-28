pesel = input("Podaj pesel: ")

numbers_for_multipicatoin = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
result = 0

for i in range(len(pesel)):
    result += (int(pesel[i]) * numbers_for_multipicatoin[i]) % 10

result %= 10
control_number = 10 - result

print(control_number)
