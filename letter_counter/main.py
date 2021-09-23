import collections

text = input()

text = text.lower()
text = text.replace(" ", "")
text = text.replace(".", "")
text = text.replace(",", "")
text = text.replace("!", "")

# letter_counter = {
#     'a' : 0,
#     'b' : 0,
#     'c' : 0,
#     'd' : 0,
#     'e' : 0,
#     'f' : 0,
#     'g' : 0,
#     'h' : 0,
#     'i' : 0,
#     'j' : 0,
#     'k' : 0,
#     'l' : 0,
#     'm' : 0,
#     'n' : 0,
#     'o' : 0,
#     'p' : 0,
#     'q' : 0,
#     'r' : 0,
#     's' : 0,
#     't' : 0,
#     'u' : 0,
#     'v' : 0,
#     '2' : 0,
#     'x' : 0,
#     'y' : 0,
#     'z' : 0,
# }

# for i in text:
#     letter_counter[i] += 1

# print(letter_counter)


dict = {} 

for i in range(len(text)):
     if text[i] in dict.keys():
         continue
     else:
         dict[text[i]] = [] 

for i in dict:
    dict[i] = 0
for i in text:
    dict[i] += 1

dict = sorted(dict.items())

print(dict)