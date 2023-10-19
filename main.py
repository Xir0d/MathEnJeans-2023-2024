import turtle
from turtle import screensize

# Créer une instance de la tortue
tortue = turtle.Turtle()
tortue.speed(50)

# Définir la taille de la grille (nombre de lignes et de colonnes)
nombre_lignes = 5
nombre_colonnes = 5

# Définir la taille de chaque cellule dans la grille
taille_cellule = 100  # Changer selon tes besoins

# Fonction pour déplacer la tortue à une cellule spécifique
def deplacer_a_cellule(ligne, colonne):
    x = colonne * taille_cellule
    y = ligne * taille_cellule
    tortue.penup()
    tortue.goto(x, y)
    tortue.pendown()

# Dessiner la grille
# Déplacer la tortue au centre de la fenêtre
for ligne in range(nombre_lignes + 1):
    deplacer_a_cellule(ligne, 0)
    tortue.forward(taille_cellule * nombre_colonnes)

for colonne in range(nombre_colonnes + 1):
    deplacer_a_cellule(0, colonne)
    tortue.setheading(90)  # Changer la direction vers le haut
    tortue.forward(taille_cellule * nombre_lignes)
    tortue.setheading(0)  # Revenir à la direction vers la droite

# Fermer la fenêtre lors d'un clic
turtle.exitonclick()
