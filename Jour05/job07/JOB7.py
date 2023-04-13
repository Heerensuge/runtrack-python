def changer_mot(mot):
    if not mot.isalpha() or not mot.islower():
        print("Le mot doit contenir uniquement des lettres minuscules de l'alphabet.")
        return

    liste_lettres = list(mot)

    index_deplacable = None
    for i in range(len(liste_lettres) - 1, 0, -1):
        if liste_lettres[i] > liste_lettres[i - 1]:
            index_deplacable = i - 1
            break

   
    if index_deplacable is None:
        print("Le mot est déjà le plus grand possible.")
        return

    
    index_echange = None
    for i in range(len(liste_lettres) - 1, index_deplacable, -1):
        if liste_lettres[i] > liste_lettres[index_deplacable]:
            index_echange = i
            break

    
    liste_lettres[index_deplacable], liste_lettres[index_echange] = liste_lettres[index_echange], liste_lettres[index_deplacable]

   
    liste_lettres[index_deplacable + 1:] = sorted(liste_lettres[index_deplacable + 1:])

    
    nouveau_mot = ''.join(liste_lettres)
    print(f"Le nouveau mot est : {nouveau_mot}")


mot = input("Entrez un mot : ")
changer_mot(mot)
