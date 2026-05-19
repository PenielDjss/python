import random
from pprint import pprint


print(dir(random))  # voir les fonction d'un module
pprint(dir(random)) # voir ligne par ligne 

help(random.randint) # voir l'aide de la fonction ne pas mettre les parenthèses devant la fonction sinon la fonction tentte de s'exécuter


# fonction randint
r =  random.randint(0, 200)
print(r)

# fonction uniform pareil que randint renvoi un flottant 
a = random.uniform(0, 1)
print(a)

# fonction randrange pareil que randint mais prend 0 comme début de l'interval directement
n = random.randrange(2) # valeur de fin exclusive également
print(n)

d = random.randrange(0, 101, 10) # la troisième valeur est le pas un peu comme le bon de comptage
print(d)