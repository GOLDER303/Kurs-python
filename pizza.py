import sys

pizza_info = []

for i in range(1, len(sys.argv)):
    pizza_info.append(sys.argv[i])

def compare(price, size):
    size, price = float(size), float(price)
    pizza_field = 3.14 * (size/2)**2
    return pizza_field / price

for i in range(0, len(sys.argv) - 1, 4):
    print(f"Restauracja: {pizza_info[i]} pizza: {pizza_info[i + 1]}, size: {pizza_info[i + 2]}, price: {pizza_info[i + 3]}")

ratio_list = []

for i in range(2, len(sys.argv), 4):
    ratio_list.append(compare(pizza_info[i], pizza_info[i+1]))

best_ratio = ratio_list.index(min(ratio_list)) + 1

print(f"Najleszpy stosunek ma pizza nr. {best_ratio}")