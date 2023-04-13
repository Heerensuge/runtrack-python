def tri_croissant(liste):
    """
    Trie une liste dans l'ordre croissant.
    """
    liste_triee = sorted(liste)
    return liste_triee
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
L_triee = tri_croissant(L)
print(L_triee)
