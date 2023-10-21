# Dictionnaire des cases
case = {"a2": 0, "a3": 0, "a4": 0, "b1": 0}

# Motifs élémentaires
def AB():
    case["a2"] = case["a2"] + 1

def AC():
    case["a2"] = case["a2"] + 1
    case["b1"] = case["b1"] + 1

# Annuler action motif
def rAB():
    case["a2"] = case["a2"] - 1

def rAC():
    case["a2"] = case["a2"] - 1
    case["b1"] = case["b1"] - 1

# Objectif final
objectif = {"oa2": 2, "oa3": 0, "oa4": 0, "ob1": 1}

# Indice de choix du motif
dico_idM = {"idM": 0}

def idMotif():
    dico_idM["idM"] = abs(objectif["oa2"] - case["a2"]) + abs(objectif["oa3"] - case["a3"]) + abs(objectif["oa4"] - case["a4"]) + abs(objectif["ob1"] - case["b1"])
    print("idM : ", dico_idM["idM"])
    print("idM de a2 : ", abs(objectif["oa2"] - case["a2"]))
    print("idM de a3 : ", abs(objectif["oa3"] - case["a3"]))
    print("idM de a4 : ", abs(objectif["oa4"] - case["a4"]))
    print("idM de b1 : ", abs(objectif["ob1"] - case["b1"]))

# Définition de l'idM par motif
idM_motif = {"idAB": 0, "idAC": 0}

def idM_par_motif():
    AB()
    print("idM pour AB :")
    idMotif()
    idM_motif["idAB"] = dico_idM["idM"]
    rAB()
    print("idM pour AB :", dico_idM["idM"])
    print("idAB : ", idM_motif["idAB"])

    AC()
    print("idM pour AC :")
    idMotif()
    idM_motif["idAC"] = dico_idM["idM"]
    rAC()
    print("idAC : ", idM_motif["idAC"])

# Nombre d'utilisation totale de chaque motif
totMotif = {"totAB": 0, "totAC": 0}

# Choix du motif et application
print(case)

for i in range(3):
    idM_par_motif()   # Définir l'indice de choix du motif
    print("idMotif : " + str(idM_motif))
    res =  [key for key in idM_motif if     # Choisir le motif qui a le plus faible idM (et qui n'est pas déjà utilisé si il y en a plusieurs avec la même valeur)
        all(idM_motif[temp] >= idM_motif[key]
        for temp in idM_motif)]
    print("Keys with minimum values are : " + str(res))
    