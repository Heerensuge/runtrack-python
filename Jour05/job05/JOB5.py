def distance_toilettes(marches, hauteur):
    distance_jour = (marches * hauteur * 2) / 100  
    distance_semaine = distance_jour * 5 * 7  
    return round(distance_semaine, 2)


marches = 50
hauteur = 20
distance = distance_toilettes(marches, hauteur)
print(f"Pour {marches} marches de {hauteur} cm, le gardien parcours {distance} m par semaine.")
