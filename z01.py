import math

a = float(input("Podaj a:"))
b = float(input("Podaj b:"))
c = float(input("Podaj c:"))

delta = b**2 - 4*a*c 

if delta > 0:
    x1 = (-b + math.sqrt(delta))/2*a
    x2 = (-b - math.sqrt(delta))/2*a
    print(f"X1: {x1}\nX2: {x2}")
    print('X1: ' + x1 + '\nX2: ' + x2)

elif delta == 0:
    x0 = -b/2*a
    print(f"X0: {x0}")
    
elif delta < 0:
    print("Brak rozwiązania w zbiorze liczb rzeczywistych")