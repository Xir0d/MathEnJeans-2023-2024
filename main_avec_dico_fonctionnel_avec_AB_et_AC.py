# Dictionnaire des cases
case = {"a2": 0, "a3": 0, "a4": 0, "b1": 0, "b2": 0, "b3": 0, "b4": 0, "b5": 0, "c1": 0, "c2": 0, "c3": 0, "c4": 0, "c5": 0, "d1": 0, "d2": 0, "d3": 0, "d4": 0, "d5": 0, "e2": 0, "e3": 0, "e4": 0}

# Motifs élémentaires
def AB():
    case["a2"] = case["a2"] + 1

def AC():
    case["a2"] = case["a2"] + 1
    case["b1"] = case["b1"] + 1

def END():
    case["a2"] = case["a2"]

# Annuler action motif
def rAB():
    case["a2"] = case["a2"] - 1

def rAC():
    case["a2"] = case["a2"] - 1
    case["b1"] = case["b1"] - 1

def rEND():
    case["a2"] = case["a2"]

# Objectif final
objectif = {"oa2": 2, "oa3": 0, "oa4": 0, "ob1": 1, "ob2": 0, "ob3": 0, "ob4": 0, "ob5": 0, "oc1": 0, "oc2": 0, "oc3": 0, "oc4": 0, "oc5": 0, "od1": 0, "od2": 0, "od3": 0, "od4": 0, "od5": 0, "oe2": 0, "oe3": 0, "oe4": 0}

# Indice de choix du motif
dico_idM = {"idM": 0}

def idMotif():
    dico_idM["idM"] = abs(objectif["oa2"] - case["a2"]) + abs(objectif["oa3"] - case["a3"]) + abs(objectif["oa4"] - case["a4"]) + abs(objectif["ob1"] - case["b1"]) + abs(objectif["ob2"] - case["b2"]) + abs(objectif["ob3"] - case["b3"]) + abs(objectif["ob4"] - case["b4"]) + abs(objectif["ob5"] - case["b5"]) + abs(objectif["oc1"] - case["c1"]) + abs(objectif["oc2"] - case["c2"]) + abs(objectif["oc3"] - case["c3"]) + abs(objectif["oc4"] - case["c4"]) + abs(objectif["oc5"] - case["c5"]) + abs(objectif["od1"] - case["d1"]) + abs(objectif["od2"] - case["d2"]) + abs(objectif["od3"] - case["d3"]) + abs(objectif["od4"] - case["d4"]) + abs(objectif["od5"] - case["d5"]) + abs(objectif["oe2"] - case["e2"]) + abs(objectif["oe3"] - case["e3"]) + abs(objectif["oe4"] - case["e4"])
    # print("idM : ", dico_idM["idM"])
    # print("idM de a2 : ", abs(objectif["oa2"] - case["a2"]))
    # print("idM de a3 : ", abs(objectif["oa3"] - case["a3"]))
    # print("idM de a4 : ", abs(objectif["oa4"] - case["a4"]))
    # print("idM de b1 : ", abs(objectif["ob1"] - case["b1"]))

# Définition de l'idM par motif
idM_motif = {"idAB": 0, "idAC": 0, "idEND": 0}

def idM_par_motif():
    AB()
    # print("idM pour AB :")
    idMotif()
    idM_motif["idAB"] = dico_idM["idM"]
    rAB()
    print("idAB : ", idM_motif["idAB"])

    AC()
    # print("idM pour AC :")
    idMotif()
    idM_motif["idAC"] = dico_idM["idM"]
    rAC()
    print("idAC : ", idM_motif["idAC"])

    END()
    # print("idM pour END :")
    idMotif()
    idM_motif["idEND"] = dico_idM["idM"]
    rEND()
    print("idEND : ", idM_motif["idEND"])



# Nombre d'utilisation totale de chaque motif
totMotif = {"totAB": 0, "totAC": 0, "totEND": 0}

# Choix du motif et application
print("Valeurs initiales des cases :", case)

while totMotif["totEND"] == 0:
    dico_idM["ancient_idM"] = dico_idM["idM"]

    idM_par_motif()   # Définir l'indice de choix du motif
    # print("idMotif : " + str(idM_motif))
    res =  [key for key in idM_motif if     # Choisir le motif qui a le plus faible idM
        all(idM_motif[temp] >= idM_motif[key]
        for temp in idM_motif)]
    print("Keys with minimum values are : " + str(res))


    if 'idAB' in str(res):
        AB()
        print("-> apply AB")
        totMotif["totAB"] = totMotif["totAB"] + 1
    if 'idAC' in str(res):
        AC()
        print("-> apply AC")
        totMotif["totAC"] = totMotif["totAC"] + 1
    if 'idEND' in str(res):
        print("-> stop")
        totMotif["totEND"] = totMotif["totEND"] + 1
        
    

print("Valeurs finales des cases :", case)
print("Nombre d'utilisations de AB : ", totMotif["totAB"])
print("Nombre d'utilisations de AC : ", totMotif["totAC"])