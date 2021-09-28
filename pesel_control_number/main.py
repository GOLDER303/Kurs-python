pesel = input("Podaj pesel: ")

result = 0
result += (int(pesel[0]) * 1) % 10
result += (int(pesel[1]) * 3) % 10
result += (int(pesel[2]) * 7) % 10
result += (int(pesel[3]) * 9) % 10
result += (int(pesel[4]) * 1) % 10
result += (int(pesel[5]) * 3) % 10
result += (int(pesel[6]) * 7) % 10
result += (int(pesel[7]) * 9) % 10
result += (int(pesel[8]) * 1) % 10
result += (int(pesel[9]) * 3) % 10

result %= 10
control_number = 10 - result

print(control_number)
