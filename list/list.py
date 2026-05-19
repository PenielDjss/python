liste = [
    "User_1",
    "User_2",
    "User_3",
    "User_4",
    "User_5",
    "User_6",
    "User_3",
]

# Pour ajouter des valeurs à une liste on utiliser append ou extend | extend peut prendre plusieurs élément dans une liste
# remove pour supprimer un élément
# pop pour retirer un élément en précisant sont index
# clear pour supprimer tous les éléments de la liste
# in et not in pour vérifir si un élément est dans une liste ou pas

print(liste[:]) # slice
print(liste[::2]) # le pas

resultat = liste.index('User_3')
resultat = liste.count('User_3')
liste.sort() # avec cette méthode on n'a pas besoin de réassigner  
liste.reverse # renverser tout simplement

print(liste)