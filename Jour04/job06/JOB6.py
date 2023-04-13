def echanger_premier_dernier(L):
    if len(L) >= 2:
        L[0], L[-1] = L[-1], L[0]

L = [1, 2, 3, 4, 5]

# Avant échange
print("Avant échange : ", L)

# Échanger les valeurs de la première et de la dernière case de la liste
echanger_premier_dernier(L)

# Après échange
print("Après échange : ", L)
