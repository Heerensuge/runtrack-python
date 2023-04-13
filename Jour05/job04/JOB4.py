def chiffrement_cesar(message, decalage):
    """
    Chiffre un message en décalant chaque lettre de 'decalage' rangs dans l'alphabet.
    Gère le dépassement de 'z' vers 'a' et de 'a' vers 'z'.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message_chiffre = ''
    for lettre in message:
        if lettre.lower() in alphabet:
            
            index = (alphabet.index(lettre.lower()) + decalage) % len(alphabet)
            
            if lettre.isupper():
                message_chiffre += alphabet[index].upper()
            else:
                message_chiffre += alphabet[index]
        else:
            message_chiffre += lettre
    return message_chiffre
message = "Je suis trop nul à python !"
decalage = 3
message_chiffre = chiffrement_cesar(message, decalage)
print(message_chiffre)  
