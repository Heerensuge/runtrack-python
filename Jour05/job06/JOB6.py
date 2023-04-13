import math

def arrondir_notes(notes):
    arrondies = []
    for note in notes:
        if note < 40:
            arrondies.append(note)
        else:
            multiple_de_5 = math.ceil(note/5) * 5
            if multiple_de_5 - note < 3:
                arrondies.append(multiple_de_5)
            else:
                arrondies.append(note)
    return arrondies
notes = [78, 52, 63, 39, 91, 85]
arrondies = arrondir_notes(notes)
print(arrondies)
