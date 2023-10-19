#Import
import json

# cases
a2 = 0
a3 = 0
a4 = 0
b1 = 0
b2 = 0
b3 = 0
b4 = 0
b5 = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
d1 = 0
d2 = 0
d3 = 0
d4 = 0
d5 = 0
e2 = 0
e3 = 0
e4 = 0
A2 = 0

# motifs élémentaires
def AB():
    # Ouvrir le fichier en mode lecture
    with open('database.json', 'r') as fichier_json:
        donnees = json.load(fichier_json)
    
    a2 = donnees.get("a2", 0)  # Utilisez .get() pour obtenir la valeur de "a2" avec une valeur par défaut de 0 si elle n'existe pas
    print(a2)
    
    a2 = a2 + 1
    variable_a_envoyer = {"a2": a2}

    # Réouvrir le fichier en mode écriture pour mettre à jour les données
    with open('database.json', 'w') as fichier_json:
        json.dump(variable_a_envoyer, fichier_json)

def AC(a2, b1):
    a2 = a2 + 1
    b1 = b1 + 1

# Appeler AB() deux fois
AB()
AB()























