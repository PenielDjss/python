# for
liste = [1, 2, 3]


# on peut aussi l'utilser avec range pour répéter une action un certain nombre de fois
for i in liste:
    print(i)

# faire attention aux boucles infinies
i = 0
while i < 1000:
    print('Bonjour')
    i += 1

second_list = ["1", "4", "25", "Paul", "3", "Pierre"]

# Lorsque la condition est vérifiée continue passe à la prochaine itération sans exécuter le reste du code
for element in second_list:
    if element.isdigit():
        continue
    print(element)

# Lorsque la condition est vérifiée break arrête les itérations et sort de la boucle directement
for element in second_list:
    if element.isdigit():
        break
    print(element)


# List comprehension
tirth_list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

nombres_positifs = [i for i in tirth_list if i > 0]
print(nombres_positifs)