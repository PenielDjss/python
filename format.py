prenom= "Péniel"
age = 21

print("Je m'appelle", prenom, "et j'ai", age, 'ans') # il met les espaces de séparation automatiquement

print("Je m'appelle" + str(prenom) + "et j'ai" + str(age) + 'ans')  # il ne met pas d'espace il joint direct

# f-string un peu comme raw string la plus utilisée mais parfois format est le plus approprié
print(f"J'ai {age}")

# format avec système d'identifiant
print("J'ai {age} ans".format(age = age))

# format avec système d'indice
print("Je m'appelle {1} et j'ai {0} ans".format(age, prenom))

# format avec système d'indice et acollades vide il injecte dans l'ordre
print("Je m'appelle {} et j'ai {} ans".format(prenom, age))

