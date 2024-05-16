# Programme pour créer le programme de dessin en fonction de la taille et du nombre de clous

# Syntaxe des variables :
# clou1 : noms des clous
# 1-2 : motif entre deux clous
# 2.1 : case en coordonnées x.y

size = 5
size_px = 10 * size

nbr_clous = 9

import math


print ("import turtle")

print("# Créer une instance de la tortue")
print("tortue = turtle.Turtle()")
print("tortue.speed(0)")
print("# Dictionnaire des cases")

# Création du dictionnaire de cases
print('case = {', sep="", end="")
for x in range(size):
    for y in range(size):
        print('"', x, '.', y, '": 0, ', sep="", end="")
print('}')

# Coordonnées des clous
angle = 360 / nbr_clous
math.radians(angle)

clous = {}
for i in range(nbr_clous):
    clous[x,i] = math.cos(angle * i) * size_px
    clous[y,i] = math.sin(angle * i) * size_px


print ('clous =', clous)

# Création des fonctions des motifs élémentaires
print('# Motifs élémentaires')

for i in range(nbr_clous):
    for j in range(nbr_clous):
        if j > i:
            print ('def', sep="", end="")
            print(i, "-", j, '():', sep="", end="")