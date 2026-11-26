def get_age():
    age_text = input("Quel âge avez-vous ? ")
    return int(age_text)

age = None

while age is None:
    try:
        age = get_age()
        print(f"Vous avez {age} ans.")
    except ValueError as ex: 
        print(ex)
        print("Veuillez entrer un nombre valide pour l'âge.")
