first_list = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_paires = [i for i in first_list if i % 2 == 0]
print(nombres_paires)

second_list = range(-10, 10)
nombres_positifs = [i for i in second_list if i >= 0]
print(nombres_positifs)

tirth_list = range(5)
nombre_doubles = [i*2 for i in tirth_list]
print(nombre_doubles)


# Quand on a un else la condition vient au début
furth_list=range(10)
nombres_inverses = [i if i % 2 == 0 else -i for i in furth_list]
print(nombres_inverses)

for i in range(10):
    print(f'Utilisateur {i + 1}')

mot = "Python"
for i in reversed(mot):
    print(i)

continuer = "o"
while continuer == "o":
    print("On continue !")
    continuer = input("Voulez-vous continuer ? o/n ")
