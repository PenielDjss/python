import os
import pathlib

class InvalidAgeError(Exception):
    pass


def get_age():
    age_text = input("Quel âge avez-vous ? ")
    age = int(age_text)
    if age < 0 or age > 150:
        raise InvalidAgeError("L'âge doit être compris entre 0 et 120 ans.")
    return int(age)

def get_file_content():
    print(os.getcwd())
    base_dir = pathlib.Path(__file__).resolve().parent
    file_path = base_dir / "input" / "sample.txt"
    with open(file_path, "r") as file:
        return file.read()
    

try:
    age = get_age()
    if age >= 18:
        file_content = get_file_content()
        print(file_content)
    else:
        print("Vous devez être majeur pour accéder au contenu du fichier.")
except InvalidAgeError as e:
    print(e)
    print("Votre âge doit être entre 0 et 150 ans.")
except ValueError:
    print("Veuillez entrer un nombre valide pour l'âge.")
except FileNotFoundError:
    print("Le fichier sample.txt est introuvable.")
except Exception as ex: # Le except Exception est un catch-all qui attrape toutes les exceptions qui n'ont pas été attrapées par les except précédents
    print(ex)
else :  # Le else vient toujours après le dernier except 
    print("Le programme s'est exécuté avec succès.")
finally: # Le finally vient en toute dernire position et est exécuté dans tous les cas, que l'exception soit levée ou pas
    print("Merci d'avoir utilisé notre programme.")