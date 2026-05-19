age = 20

if age >= 18:                           # si
    print('Vous êtes majeur !')     
elif age < 18:                          # sinon si
    print('Vous êtes mineur !')
else:                                   # sinon (sans condition il prend ce qui n'est pas par if et else)
    print("Genre tu n'as d'âge ??")

# Opérateurs ternaires
majeur: bool
majeur = True if age >= 18 else False   # condition if action_1 else action_2

# Opérateurs logiques
user : str = 'admin'
if not (user == 'admin') and majeur == True or age >= 18:
    print('Accès refusey !')