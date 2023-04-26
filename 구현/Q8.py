asdf = input()

alphabet = []
number = 0

for i in asdf:
    if i.isalpha():
        alphabet.append(i)
    else:
        number += int(i)

alphabet.sort()
print("".join(alphabet)+str(number))
