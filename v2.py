# Programme pour créer le dessin en fonction de la taille et du nombre de clous

# Syntaxe des variables :
# clou(1) : noms des clous
# 1-2 : motif entre deux clous
# (2, 1) : case en coordonnées x.y

import math
import numpy as np

clous = int(input('Nombre de Clous : '))



# Créer dico objectif en fonction de l'image
objectif = {}

from PIL import Image

image = Image.open("./test.png")
image = image.convert('L')  # Conversion en 256 nuances de gris
#   image.show()

width, height = image.size
print("width :", width)
print("height :", height)

obj = np.zeros((height,width))

for x in range(width):
    for y in range(height):
        pixel = (255 - image.getpixel((x, y)))  # // 10
        #   print(pixel)
        # objectif['o', x,y] = pixel
        obj[y,x] = pixel

# Créer matrice avec valeur actuelle des cases
cases = np.zeros((height,width))
print("cases : ", cases)
print("obj : ", obj)


# Créer dico cases
# case = {}

# for i in range(width):
#     for y in range(height):
#         case[i,y] = 0



# print("case : ", case)
# print("objectif : ", objectif)



# Coordonnées des clous
angle = 360 / clous
angle = math.radians(angle)

coorclous = {}

for i in range(clous):
    coorclous['x',i] = math.cos(angle * i)
    coorclous['y',i] = math.sin(angle * i)
    
print('coorclous : ', coorclous)


# Nombre de motifs
s = 0
for i in range(clous):
    s = i + s
print("Nb de motifs : ", s)

#test = coorclous['x',i]
#test2 = 

# Définir les motifs élémentaires
motif = {}

for i in range(clous):
    for j in range(clous):
        if i < j:
            motif[i,j] = np.zeros((height,width))
            #print("coorclous['x',i]", coorclous['x',i])
            #print("coorclous['x',j]", coorclous['x',j])
            #print("coorclous['y',i]", coorclous['y',i])
            #print("coorclous['y',j]", coorclous['y',j])
            # Définir les équations de droites
            coef_droite = (coorclous['y',j] - coorclous['y',i]) / (coorclous['x',j] - coorclous['x',i])
            #print("coef_droite=", coef_droite)
            for m in range(width):
                for n in range(height):
                    #print("m=", m, " n=", n)
                    if coorclous['x',i] < coorclous['x',j]:
                        #print("coorclous['x',i] < coorclous['x',j]")
                        if coorclous['x',i] < (((2 / width) * (m + 0.5)) - 1) < coorclous['x',j]:
                            #print("georges sand")
                            if coorclous['y',i] < coorclous['y',j]:
                                #print("georges 2")
                                #print("coorclous['y',i] =", coorclous['y',i])
                                #print("(((2 / width) - 1) * n + 0.5)", (((2 / width) * (n + 0.5)) - 1))
                                #print("coorclous['y',j]", coorclous['y',j])
                                if coorclous['y',i] < (((2 / width) * (n + 0.5)) - 1) < coorclous['y',j]:
                                    #print("georges 3")
                                    if ((((2 / width) * m) - 1) < (((((2 / width) * n) - 1) - (coorclous['y',i] - (coef_droite * coorclous['x',i]))) / coef_droite) < (((2 / width) * (m + 1)) - 1) or (((2 / width) * m) - 1) < (((((2 / width) * (n + 1)) - 1) - (coorclous['y',i] - (coef_droite * coorclous['x',i]))) / coef_droite) < (((2 / width) * (m + 1)) - 1)) and ((((2 / height) * n) - 1) < (coef_droite * (((2 / width) * m) - 1) + coorclous['y',i] - (coef_droite * coorclous['x',i])) < (((2 / height) * (n + 1)) - 1) or (((2 / height) * n) - 1) < (coef_droite * (((2 / width) * (m + 1)) - 1) + coorclous['y',i] - (coef_droite * coorclous['x',i])) < (((2 / height) * (n + 1)) - 1)):   # (2 / width) est la largeur d'une case quand la grille fait la taille du cecle trigo
                                        # case[m,n] = case[m,n] + 1
                                        motif[i,j][(m,n)] = motif[i,j][(m,n)] + 1
                                        #print("case[m,n] = case[m,n] + 1")
                        elif coorclous['x',i] < (((2 / width) * (m + 0.5)) - 1) < coorclous['x',j]:
                            if coorclous['y',i] > coorclous['y',j]:
                                if coorclous['y',i] > (((2 / width) * (n + 0.5)) - 1) > coorclous['y',j]:
                                    if ((((2 / width) * m) - 1) < (((((2 / width) * n) - 1) - (coorclous['y',i] - (coef_droite * coorclous['x',i]))) / coef_droite) < (((2 / width) * (m + 1)) - 1) or (((2 / width) * m) - 1) < (((((2 / width) * (n + 1)) - 1) - (coorclous['y',i] - (coef_droite * coorclous['x',i]))) / coef_droite) < (((2 / width) * (m + 1)) - 1)) and ((((2 / height) * n) - 1) < (coef_droite * (((2 / width) * m) - 1) + coorclous['y',i] - (coef_droite * coorclous['x',i])) < (((2 / height) * (n + 1)) - 1) or (((2 / height) * n) - 1) < (coef_droite * (((2 / width) * (m + 1)) - 1) + coorclous['y',i] - (coef_droite * coorclous['x',i])) < (((2 / height) * (n + 1)) - 1)):
                                        motif[i,j][(m,n)] = motif[i,j][(m,n)] + 1
                                        # case[m,n] = case[m,n] + 1
                                        #print("case[m,n] = case[m,n] + 1")
                    elif coorclous['x',i] > coorclous['x',j]:
                        if coorclous['x',i] > (((2 / width) * (m + 0.5)) - 1) > coorclous['x',j]:
                            ##print("coorclous['x',i]", coorclous['x',i])
                            #print("(((2 / width) * (m + 0.5)) - 1)", (((2 / width) * (m + 0.5)) - 1))
                            #print("coorclous['x',j]", coorclous['x',j])
                            #print("georges sand")
                            if coorclous['y',i] > coorclous['y',j]:
                                #print("georges 2")
                                if coorclous['y',i] > (((2 / width) * (n + 0.5)) - 1) > coorclous['y',j]:
                                    #print("coorclous['y',i]", coorclous['y',i])
                                    #print("(((2 / width) * (n + 0.5)) - 1)", (((2 / width) * (n + 0.5)) - 1))
                                    #print("coorclous['y',j]", coorclous['y',j])
                                    #print("georges 3")
                                    #print("\n Test :")
                                    #print("(((2 / width) - 1) * m)", (((2 / width) * m)) - 1)
                                    #print("((n - (coorclous['y',i] - (coef_droite * coorclous['x',i]))) / coef_droite)", ((n - (coorclous['y',i] - (coef_droite * coorclous['x',i]))) / coef_droite))
                                    #print("(((2 / width) * (m + 1)) - 1)", (((2 / width) * (m + 1)) - 1))
                                    #print("(((2 / height) * n) - 1)", (((2 / height) * n) - 1))
                                    #print("(coef_droite * m + coorclous['y',i] - (coef_droite * coorclous['x',i]))", (coef_droite * m + coorclous['y',i] - (coef_droite * coorclous['x',i])))
                                    #print("(((2 / height) * (n + 1)) - 1)", (((2 / height) * (n + 1)) - 1))
                                    #print("\n")
                                    if ((((2 / width) * m) - 1) < (((((2 / width) * n) - 1) - (coorclous['y',i] - (coef_droite * coorclous['x',i]))) / coef_droite) < (((2 / width) * (m + 1)) - 1) or (((2 / width) * m) - 1) < (((((2 / width) * (n + 1)) - 1) - (coorclous['y',i] - (coef_droite * coorclous['x',i]))) / coef_droite) < (((2 / width) * (m + 1)) - 1)) and ((((2 / height) * n) - 1) < (coef_droite * (((2 / width) * m) - 1) + coorclous['y',i] - (coef_droite * coorclous['x',i])) < (((2 / height) * (n + 1)) - 1) or (((2 / height) * n) - 1) < (coef_droite * (((2 / width) * (m + 1)) - 1) + coorclous['y',i] - (coef_droite * coorclous['x',i])) < (((2 / height) * (n + 1)) - 1)):
                                        motif[i,j][(m,n)] = motif[i,j][(m,n)] + 1
                                        # case[m,n] = case[m,n] + 1
                                        #print("case[m,n] = case[m,n] + 1")
                        elif coorclous['x',i] > (((2 / width) * (m + 0.5)) - 1) > coorclous['x',j]:
                            #print("ageorges sand")
                            if coorclous['y',i] < coorclous['y',j]:
                                #print("ageorges 2")
                                if coorclous['y',i] < (((2 / width) * (n + 0.5)) - 1) < coorclous['y',j]:
                                    #print("ageorges 3")
                                    if ((((2 / width) * m) - 1) < (((((2 / width) * n) - 1) - (coorclous['y',i] - (coef_droite * coorclous['x',i]))) / coef_droite) < (((2 / width) * (m + 1)) - 1) or (((2 / width) * m) - 1) < (((((2 / width) * (n + 1)) - 1) - (coorclous['y',i] - (coef_droite * coorclous['x',i]))) / coef_droite) < (((2 / width) * (m + 1)) - 1)) and ((((2 / height) * n) - 1) < (coef_droite * (((2 / width) * m) - 1) + coorclous['y',i] - (coef_droite * coorclous['x',i])) < (((2 / height) * (n + 1)) - 1) or (((2 / height) * n) - 1) < (coef_droite * (((2 / width) * (m + 1)) - 1) + coorclous['y',i] - (coef_droite * coorclous['x',i])) < (((2 / height) * (n + 1)) - 1)):
                                        motif[i,j][(m,n)] = motif[i,j][(m,n)] + 1
                                        # case[m,n] = case[m,n] + 1
                                        #print("case[m,n] = case[m,n] + 1")


motif["end"] = np.zeros((height,width))
for m in range(width):
    for n in range(height):
        motif["end"][(m,n)] = 0



# Indice de choix du motif
dico_idM = {"idM": 0}

def idMotif():
    dico_idM["idM"] = 0
    for m in range(width):
        for n in range(height):
            dico_idM["idM"] = dico_idM["idM"] + abs(obj[(m,n)] - cases[(m,n)])

idM_motif = {}



def idM_par_motif(cases):
    for i in range(clous):
        for j in range(clous):
            if i < j:
            #    print(cases)
            #    print(motif[i,j])
            #    for m in range(width):
            #        for n in range(height):
            #            cases[i,j][(m,n)] = cases[i,j][(m,n)] + motif[i,j][(m,n)]
            #    cases[i,j] = np.add(cases[i,j],motif[i,j])
                cases = cases + motif[i,j]
                idMotif()
                idM_motif[i,j] = dico_idM["idM"]
                cases = cases - motif[i,j]


# Nombre d'utilisation totale de chaque motif
totMotif = {}
totMotif["totEND"] = 0

# Choix du motif et application
print("Valeurs initiales des cases :", cases)

#while totMotif["totEND"] == 0:
for i in range(10):
    idM_par_motif(cases)   # Définir l'indice de choix du motif

    res =  [key for key in idM_motif if     # Choisir le motif qui a le plus faible idM
        all(idM_motif[temp] >= idM_motif[key]
        for temp in idM_motif)]
    print("Keys with minimum values are : " + str(res))

#    for i in range(clous):
#        for j in range(clous):
#            if i < j:
                #if 'idAB' in str(res):
                    #AB()
                    #print("-> apply AB")
                    #totMotif["totAB"] = totMotif["totAB"] + 1










print("idM_motif", idM_motif)

#motif(2,5)
print("obj = ", obj)
idMotif()
print("dico_idM[idM]", dico_idM["idM"])

print("motif[2,5]", motif[2,5])
print("cases = ", cases)
idMotif()
print("dico_idM[idM]", dico_idM["idM"])

print("cases = ", cases)
idMotif()
print("dico_idM[idM]", dico_idM["idM"])

print("motif[3,7]", motif[3,7])
print("cases = ", cases)
idMotif()
print("dico_idM[idM]", dico_idM["idM"])


# Pour autant de loop que de motifs
#for i in range(clous):
#    for j in range(clous):
#        if j > i:

# Equation de droite :
# n = (coef_droite * m + coorclous['y',i] - (coef_droite * coorclous['x',i]))
# m = ((n - (coorclous['y',i] - (coef_droite * coorclous['x',i]))) / coef_droite)

#Utiliser des matrices python à la place de listes.