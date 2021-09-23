import sys

pizza_info = []

for j in range(0, int(len(sys.argv) / 4)):
    for i in range(1, len(sys.argv)):
        print(j, i)
        pizza_info[j].append(sys.argv[i])

def compare(price, size):
    size, price = float(size), float(price)
    pizza_field = 3.14 * (size/2)**2
    return pizza_field / price



print(f"Restauracja: {pizza_info[0]} pizza: {pizza_info[1]}, size: {pizza_info[2]}, price: {pizza_info[3]}")
print(f"Restauracja: {pizza_info[4]} pizza: {pizza_info[5]}, size: {pizza_info[6]}, price: {pizza_info[7]}")
print(f"Restauracja: {pizza_info[8]} pizza: {pizza_info[9]}, size: {pizza_info[10]}, price: {pizza_info[11]}")

ratio_list = []

for i in range(2, len(sys.argv), 4):
    ratio_list.append(compare(pizza_info[i], pizza_info[i+1]))

best_ratio = ratio_list.index(min(ratio_list)) + 1

print(f"Najleszpy stosunek ma pizza nr. {best_ratio}")