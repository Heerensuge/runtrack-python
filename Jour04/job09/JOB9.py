L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

min_value = L[0]
max_value = L[0]

for x in L:
    if x < min_value:
        min_value = x
    if x > max_value:
        max_value = x

print("Le minimum de la liste L est :", min_value)
print("Le maximum de la liste L est :", max_value)
