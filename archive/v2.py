# Programme pour créer le dessin en fonction de la taille et du nombre de clous


import math
import numpy as np
import turtle


clous = int(input('Nombre de Clous : '))



# Créer dico objectif en fonction de l'image
objectif = {}

from PIL import Image

image = Image.open("./spirale.png")
image = image.convert('L')  # Conversion en 256 nuances de gris
#   image.show()


# Taille de l'image
width, height = image.size
print("width :", width)
print("height :", height)


# Matrice objectif
obj = np.zeros((height,width))

for x in range(width):
    for y in range(height):
        pixel = (255 - image.getpixel((x, y)))  # // 10
        obj[y,x] = pixel


# Créer matrice avec valeur actuelle des cases
cases = np.zeros((height,width))


print("cases : ", cases)
print("obj : ", obj)


# Coordonnées des clous
angle = 360 / clous
angle = math.radians(angle)

coorclous = {}

for i in range(clous):
    coorclous['x',i] = math.cos(angle * i + (math.pi / 2))
    coorclous['y',i] = math.sin(angle * i + (math.pi / 2))
    
print('coorclous : ', coorclous)


# Nombre de motifs
s = 0
for i in range(clous):
    s = i + s
print("Nb de motifs : ", s)


# Définir les motifs élémentaires
motif = {}

# pour chaque paire de clous
for i in range(clous):
    for j in range(clous):
        if i < j:

            # créer la matrice du motif
            motif[i,j] = np.zeros((height,width))


            # Définir les équations de droites
            if (coorclous['x',j] - coorclous['x',i]) == 0:
                coef_droite = (coorclous['y',j] - coorclous['y',i]) / 0.0000000000000001            # pour éviter division par 0
            else:
                coef_droite = (coorclous['y',j] - coorclous['y',i]) / (coorclous['x',j] - coorclous['x',i])
            

            # pour chaque case de la matrice
            for m in range(width):
                for n in range(height):

                    if coorclous['x',i] < coorclous['x',j]:

                        #if coorclous['x',i] < (((2 / width) * (m + 0.5)) - 1) < coorclous['x',j]:

                            if coorclous['y',i] < coorclous['y',j]:

                                #if coorclous['y',i] < (((2 / width) * (n + 0.5)) - 1) < coorclous['y',j]:

                                    if ((((2 / width) * m) - 1) < (((((2 / width) * (height-n)) - 1) - (coorclous['y',i] - (coef_droite * coorclous['x',i]))) / coef_droite) < (((2 / width) * (m + 1)) - 1) or (((2 / width) * m) - 1) < (((((2 / width) * ((height-n) + 1)) - 1) - (coorclous['y',i] - (coef_droite * coorclous['x',i]))) / coef_droite) < (((2 / width) * (m + 1)) - 1)) or ((((2 / height) * (height-n)) - 1) < (coef_droite * (((2 / width) * m) - 1) + coorclous['y',i] - (coef_droite * coorclous['x',i])) < (((2 / height) * ((height-n) + 1)) - 1) or (((2 / height) * (height-n)) - 1) < (coef_droite * (((2 / width) * (m + 1)) - 1) + coorclous['y',i] - (coef_droite * coorclous['x',i])) < (((2 / height) * ((height-n) + 1)) - 1)):   # (2 / width) est la largeur d'une case quand la grille fait la taille du cecle trigo

                                        # mettre la valeur de la case (m,n) à 1
                                        motif[i,j][(m,n)] = motif[i,j][(m,n)] + 1

                        #elif coorclous['x',i] < (((2 / width) * (m + 0.5)) - 1) < coorclous['x',j]:

                            if coorclous['y',i] > coorclous['y',j]:

                                #if coorclous['y',i] > (((2 / width) * (n + 0.5)) - 1) > coorclous['y',j]:

                                    if ((((2 / width) * m) - 1) < (((((2 / width) * (height-n)) - 1) - (coorclous['y',i] - (coef_droite * coorclous['x',i]))) / coef_droite) < (((2 / width) * (m + 1)) - 1) or (((2 / width) * m) - 1) < (((((2 / width) * ((height-n) + 1)) - 1) - (coorclous['y',i] - (coef_droite * coorclous['x',i]))) / coef_droite) < (((2 / width) * (m + 1)) - 1)) or ((((2 / height) * (height-n)) - 1) < (coef_droite * (((2 / width) * m) - 1) + coorclous['y',i] - (coef_droite * coorclous['x',i])) < (((2 / height) * ((height-n) + 1)) - 1) or (((2 / height) * (height-n)) - 1) < (coef_droite * (((2 / width) * (m + 1)) - 1) + coorclous['y',i] - (coef_droite * coorclous['x',i])) < (((2 / height) * ((height-n) + 1)) - 1)):
                                        
                                        # mettre la valeur de la case (m,n) à 1
                                        motif[i,j][(m,n)] = motif[i,j][(m,n)] + 1

                    elif coorclous['x',i] > coorclous['x',j]:

                        #if coorclous['x',i] > (((2 / width) * (m + 0.5)) - 1) > coorclous['x',j]:

                            if coorclous['y',i] > coorclous['y',j]:

                                #if coorclous['y',i] > (((2 / width) * (n + 0.5)) - 1) > coorclous['y',j]:

                                    if ((((2 / width) * m) - 1) < (((((2 / width) * (height-n)) - 1) - (coorclous['y',i] - (coef_droite * coorclous['x',i]))) / coef_droite) < (((2 / width) * (m + 1)) - 1) or (((2 / width) * m) - 1) < (((((2 / width) * ((height-n) + 1)) - 1) - (coorclous['y',i] - (coef_droite * coorclous['x',i]))) / coef_droite) < (((2 / width) * (m + 1)) - 1)) or ((((2 / height) * (height-n)) - 1) < (coef_droite * (((2 / width) * m) - 1) + coorclous['y',i] - (coef_droite * coorclous['x',i])) < (((2 / height) * ((height-n) + 1)) - 1) or (((2 / height) * (height-n)) - 1) < (coef_droite * (((2 / width) * (m + 1)) - 1) + coorclous['y',i] - (coef_droite * coorclous['x',i])) < (((2 / height) * ((height-n) + 1)) - 1)):
                                        
                                        # mettre la valeur de la case (m,n) à 1
                                        motif[i,j][(m,n)] = motif[i,j][(m,n)] + 1

                        #elif coorclous['x',i] > (((2 / width) * (m + 0.5)) - 1) > coorclous['x',j]:

                            if coorclous['y',i] < coorclous['y',j]:

                                #if coorclous['y',i] < (((2 / width) * (n + 0.5)) - 1) < coorclous['y',j]:

                                    if ((((2 / width) * m) - 1) < (((((2 / width) * (height-n)) - 1) - (coorclous['y',i] - (coef_droite * coorclous['x',i]))) / coef_droite) < (((2 / width) * (m + 1)) - 1) or (((2 / width) * m) - 1) < (((((2 / width) * ((height-n) + 1)) - 1) - (coorclous['y',i] - (coef_droite * coorclous['x',i]))) / coef_droite) < (((2 / width) * (m + 1)) - 1)) or ((((2 / height) * (height-n)) - 1) < (coef_droite * (((2 / width) * m) - 1) + coorclous['y',i] - (coef_droite * coorclous['x',i])) < (((2 / height) * ((height-n) + 1)) - 1) or (((2 / height) * (height-n)) - 1) < (coef_droite * (((2 / width) * (m + 1)) - 1) + coorclous['y',i] - (coef_droite * coorclous['x',i])) < (((2 / height) * ((height-n) + 1)) - 1)):
                                        
                                        # mettre la valeur de la case (m,n) à 1
                                        motif[i,j][(m,n)] = motif[i,j][(m,n)] + 1


# motif end pour déterminer la fin
motif["end"] = np.zeros((height,width))
for m in range(width):
    for n in range(height):
        motif["end"][(m,n)] = 0


# Indice de choix du motif
dico_idM = {"idM": 0}

def idMotif(cases):
    dico_idM["idM"] = 0
    #print("cases idMotif : ", cases)
    for m in range(width):
        for n in range(height):
            dico_idM["idM"] = dico_idM["idM"] + abs(obj[(m,n)] - cases[(m,n)])


# idMotif pour chaque motif
idM_motif = {}

def idM_par_motif(cases):
    for i in range(clous):
        for j in range(clous):
            if i < j:
                cases = cases + motif[i,j]
                idMotif(cases)
                idM_motif[i,j] = dico_idM["idM"]
                cases = cases - motif[i,j]
    idMotif(cases)
    idM_motif["end"] = dico_idM["idM"]


# Nombre d'utilisation totale de chaque motif
totMotif = {}

totMotif["end"] = 0

for i in range(clous):
    for j in range(clous):
        if i < j:
            totMotif[i,j] = 0

print("totMotif : ", totMotif)


# Choix du motif et application
print("Valeurs initiales des cases :", cases)

while totMotif["end"] == 0:
    idM_par_motif(cases)   # Définir l'indice de choix du motif

    res =  [key for key in idM_motif if     # Choisir le motif qui a le plus faible idM
        all(idM_motif[temp] >= idM_motif[key]
        for temp in idM_motif)]

    print("Keys with minimum values are : ", res)

    for i in range(clous):
        for j in range(clous):
            if i < j:

                if ('end') in res:
                    totMotif['end'] = totMotif['end'] + 1
                    break

                elif (i, j) in res:
                    totMotif[i,j] = totMotif[i,j] + 1
                    for m in range(width):
                        for n in range(height):
                            for l in range(len(res)):

                                if res[l][0] != "e":
                                    a=res[l][0]
                                    b=res[l][1]

                                    cases[m,n] = cases[m,n] + motif[a,b][m,n]
                
    print("cases + res : ", cases)



print("idM_motif", idM_motif)

print("cases = ", cases)

# Total d'utilisation de chaque motif
print("totMotif : ", totMotif)


print("obj : ", obj)


# Print tous les motifs
def printMotif():
    for i in range(clous):
        for j in range(clous):
            if i < j:
                print("motif[",i,",",j,"]")
                print(motif[i,j])

printMotif()


# Dessin des fils avec Turtle

# Créer une instance de la tortue
tortue = turtle.Turtle()
tortue.speed(0)

# Dessiner le cercle
turtle.up()
turtle.goto(0, -100)
turtle.down()
turtle.circle(100, 360)
turtle.up()
for i in range(clous):
    turtle.goto(100*coorclous['x',i], 100*coorclous['y',i])
    turtle.down()
    turtle.goto(110*coorclous['x',i], 110*coorclous['y',i])
    turtle.up()

# Tracer les fils
for i in range(clous):
    for j in range(clous):
        if i < j:
            if totMotif[i,j] != 0:
                print("totMotif[",i,",",j,"] : ", totMotif[i,j])
                turtle.pensize(1+math.log(totMotif[i,j]))
                turtle.goto(100*coorclous['x',i], 100*coorclous['y',i])
                turtle.down()
                turtle.goto(100*coorclous['x',j], 100*coorclous['y',j])
                turtle.up()

# Fermer la fenêtre lors d'un clic
turtle.exitonclick()



#    for i in range(clous):
#        for j in range(clous):
#            if i < j:
                #if 'idAB' in str(res):
                    #AB()
                    #print("-> apply AB")
                    #totMotif["totAB"] = totMotif["totAB"] + 1