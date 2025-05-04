# Area Calculator

print("---------------")
print("Area Calculator")
print("---------------")

print("Vous voulez calculer l'aire de quelle figure?")
name = str(input("Nom de la figure: "))

area = None

if name == "Rectangle":
    longueur = float(input("Longueur: "))
    largeur = float(input("Largeur: "))
    area = longueur * largeur
    print(f'Aire: {area}')
elif name == "Carré":
    cote = float(input("Côté: "))
    area = cote ** 2
    print(f'Aire: {area}')
elif name == "Cercle":
    rayon = float(input("Rayon: "))
    area = 3.14 * rayon ** 2
    print(f'Aire: {area}')
elif name == "Triangle":
    base = float(input("Base: "))
    hauteur = float(input("Hauteur: "))
    area = (base * hauteur) / 2
    print(f'Aire: {area}')
elif name == "Parallelogramme":
    base = float(input("Base: "))
    hauteur = float(input("Hauteur: "))
    area = base * hauteur
    print(f'Aire: {area}')
elif name == "Trapeze":
    base_1 = float(input("Base 1: "))
    base_2 = float(input("Base 2: ")) 
    hauteur = float(input("Hauteur: "))
    area = ((base_1 + base_2) * hauteur) / 2
    print(f'Aire: {area}')
elif name == "Losange":
    diag_1 = float(input("Diagonale 1: "))
    diag_2 = float(input("Diagonale 2: "))
    area = (diag_1 * diag_2) / 2
    print(f'Aire: {area}')
else:
    print("Nous n'avons pas ajouté cette forme géométrique.")