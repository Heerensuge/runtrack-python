my_list = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Arrondir les nombres dans la liste
rounded_list = [round(num) for num in my_list]

# Trier la liste arrondie dans l'ordre croissant
sorted_list = sorted(rounded_list)

print(sorted_list)
