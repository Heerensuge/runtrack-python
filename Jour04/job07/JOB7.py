L = [9, 24, 48, 2, 16]
count = 0

for x in L:
    if x % 3 == 0:
        count += 1

print("Le nombre de multiples de 3 dans la liste L est :", count)
