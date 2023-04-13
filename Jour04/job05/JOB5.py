def remplacer_valeur(L):
    L[3] = L[2] + L[4]

L = [1, 2, 3, 4, 5]

# Afficher la valeur de L[1]
print(L[1])

# Remplacer L[3] par la somme des cases voisines L[2] et L[4]
remplacer_valeur(L)

# Afficher la valeur du dernier terme de la liste
print(L[-1])
