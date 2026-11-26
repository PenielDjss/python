a = b = ''

while not (a.isdigit() and b.isdigit()):
    a = input('Entrez le premier nombre: ')
    b = input('Entrez le deuxième nombre: ')
    if not (a.isdigit() and b.isdigit()):
        print('Veuillez entrer des nombres valides.')

print(f'Le résultat de {a} + {b} est: {int(a) + int(b)}')