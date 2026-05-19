import os

chemin = '/home/pniel/dev.peniel/python/modules'

dossier = os.path.join(chemin, 'dossier', 'test') # toujours utiliser join pour éviter les problèmes

print(dossier)

# makedirs pour créer les dossiers | mkdir ne permet pas de faire de créer des dossiers dans des dossiers qui n'existent pas par exemple 
if not os.path.exists(dossier):
    os.makedirs(dossier)
# ou on peut faire os.makedirs(dossier, exist_ok=True)

# removedirs pour supprimer
os.removedirs(dossier) # ici il y'a pas l'argument exists_ok toujours vérifier

print(os.name) # montre l'os sur lequel nous sommes

# print(callable(os.name))