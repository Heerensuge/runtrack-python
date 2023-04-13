def my_long_word(n, phrase):
    mots = phrase.split()
    longs_mots = [mot for mot in mots if len(mot) > n]
    return ' '.join(longs_mots)

# Exemple d'utilisation
phrase = "La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"
longs_mots = my_long_word(3, phrase)
print(longs_mots)
