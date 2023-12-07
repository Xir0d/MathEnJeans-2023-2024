# Programme pour créer le dessin en fonction de la taille et du nombre de clous

# Syntaxe des variables :
# clou(1) : noms des clous
# 1-2 : motif entre deux clous
# (2, 1) : case en coordonnées x.y

import math

clous = input('Nombre de Clous : ')


# Créer dico objectif en fonction de l'image
objectif = {}

from PIL import Image

image = Image.open("./test.png")
image = image.convert('L')  # Conversion en 256 nuances de gris
#   image.show()

width, height = image.size

for x in range(width):
    for y in range(height):
        pixel = (255 - image.getpixel((x, y)))  # // 10
        #   print(pixel)
        objectif['o', x,y] = pixel



# Créer dico cases
case = {}

for i in range(width):
    for y in range(height):
        case[i,y] = 0



print("case : ", case)
print("objectif : ", objectif)



# Coordonnées des clous
angle = 360 / clous
math.radians(angle)

coorclous = {}

for i in range(clous):
    coorclous['x',i] = math.cos(angle * i)
    coorclous['y',i] = math.sin(angle * i)
    
print('coorclous : ', coorclous)


# Nombre de motifs
s = 0
for i in range(clous):
    s = i + s
print("s : ", s)



# Définir les motifs élémentaires
def motif(i,j):
    # Définir les équations de droites
    coef_droite = (coorclous['y',j] - coorclous['y',i]) / (coorclous['x',j] - coorclous['x',i])
    print("coef_droite=", coef_droite)
    for m in range(width):
        for n in range(height):
            if (((2 / width) - 1) * m) < (coef_droite * m + coorclous['y',i] - (coef_droite * coorclous['x',i])) < (((2 / width) - 1) * (m + 1)) and (((2 / height) - 1) * n) < (coef_droite * m + coorclous['y',i] - (coef_droite * coorclous['x',i])) < (((2 / height) - 1) * (n + 1)):   # ((2 / width) - 1) est la largeur d'une case quand la grille fait la taille du cecle trigo
                case[m,n] = case[m,n] + 1
#            print(droite(2))
#            def motif(i,j):
#                for a in range(width):
#                    for b in range(height):
#                        if (((2 / width) - 1) * a) < droite(a - 1) < (((2 / width) - 1) * (a + 1)) and (((2 / height) - 1) * b) < droite(a - 1) < (((2 / height) - 1) * (b + 1)):   # ((2 / width) - 1) est la largeur d'une case quand la grille fait la taille du cecle trigo
#                            case[a,b] = case[a,b] + 1
#            def r_motif(i,j):
#                for a in range(width):
#                    for b in range(height):
#                        if (((2 / width) - 1) * a) < droite(a - 1) < (((2 / width) - 1) * (a + 1)) and (((2 / height) - 1) * b) < droite(a - 1) < (((2 / height) - 1) * (b + 1)):   # ((2 / width) - 1) est la largeur d'une case quand la grille fait la taille du cecle trigo
#                            case[a,b] = case[a,b] - 1



#motif(2,5)
#print(case)

# Pour autant de loop que de motifs
#for i in range(clous):
#    for j in range(clous):
#        if j > i: