# Dictionnaire des cases
case = {"a2": 0, "a3": 0, "a4": 0, "b1": 0, "b2": 0, "b3": 0, "b4": 0, "b5": 0, "c1": 0, "c2": 0, "c3": 0, "c4": 0, "c5": 0, "d1": 0, "d2": 0, "d3": 0, "d4": 0, "d5": 0, "e2": 0, "e3": 0, "e4": 0}

# Motifs élémentaires
def AB():
    case["a2"] = case["a2"] + 1

def AC():
    case["a2"] = case["a2"] + 1
    case["b1"] = case["b1"] + 1

def AD():
    case["a2"] = case["a2"] + 1
    case["a3"] = case["a3"] + 1
    case["b2"] = case["b2"] + 1
    case["c1"] = case["c1"] + 1
    case["c2"] = case["c2"] + 1
    case["d1"] = case["d1"] + 1

def AE():
    case["a3"] = case["a3"] + 1
    case["b3"] = case["b3"] + 1
    case["c2"] = case["c2"] + 1
    case["c3"] = case["c3"] + 1
    case["d2"] = case["d2"] + 1
    case["e2"] = case["e2"] + 1

def AF():
    case["a3"] = case["a3"] + 1
    case["b3"] = case["b3"] + 1
    case["c3"] = case["c3"] + 1
    case["c4"] = case["c4"] + 1
    case["d4"] = case["d4"] + 1
    case["e4"] = case["e4"] + 1

def AG():
    case["a3"] = case["a3"] + 1
    case["a4"] = case["a4"] + 1
    case["b4"] = case["b4"] + 1
    case["c4"] = case["c4"] + 1
    case["c5"] = case["c5"] + 1
    case["d5"] = case["d5"] + 1

def AH():
    case["a4"] = case["a4"] + 1
    case["b5"] = case["b5"] + 1

def AI():
    case["a4"] = case["a4"] + 1

def BC():
    case["b1"] = case["b1"] + 1

def BD():
    case["b1"] = case["b1"] + 1
    case["c1"] = case["c1"] + 1
    case["d1"] = case["d1"] + 1

def BE():
    case["b1"] = case["b1"] + 1
    case["c1"] = case["c1"] + 1
    case["c2"] = case["c2"] + 1
    case["d2"] = case["d2"] + 1
    case["e2"] = case["e2"] + 1

def BF():
    case["b2"] = case["b2"] + 1
    case["c2"] = case["c2"] + 1
    case["c3"] = case["c3"] + 1
    case["d3"] = case["d3"] + 1
    case["e3"] = case["e3"] + 1
    case["e4"] = case["e4"] + 1

def BG():
    case["a2"] = case["a2"] + 1
    case["b2"] = case["b2"] + 1
    case["b3"] = case["b3"] + 1
    case["c3"] = case["c3"] + 1
    case["c4"] = case["c4"] + 1
    case["d4"] = case["d4"] + 1
    case["d5"] = case["d5"] + 1

def BH():
    case["a2"] = case["a2"] + 1
    case["a3"] = case["a3"] + 1
    case["b3"] = case["b3"] + 1
    case["b4"] = case["b4"] + 1
    case["b5"] = case["b5"] + 1

def BI():
    case["a2"] = case["a2"] + 1
    case["a3"] = case["a3"] + 1
    case["a4"] = case["a4"] + 1

# Rien pour CD

def CE():
    case["c1"] = case["c1"] + 1
    case["d1"] = case["d1"] + 1
    case["e2"] = case["e2"] + 1

def CF():
    case["c1"] = case["c1"] + 1
    case["d1"] = case["d1"] + 1
    case["d2"] = case["d2"] + 1
    case["e3"] = case["e3"] + 1
    case["e4"] = case["e4"] + 1

def CG():
    case["c1"] = case["c1"] + 1
    case["c2"] = case["c2"] + 1
    case["c3"] = case["c3"] + 1
    case["d3"] = case["d3"] + 1
    case["d4"] = case["d4"] + 1
    case["d5"] = case["d5"] + 1

def CH():
    case["b1"] = case["b1"] + 1
    case["b2"] = case["b2"] + 1
    case["b3"] = case["b3"] + 1
    case["b4"] = case["b4"] + 1
    case["b5"] = case["b5"] + 1
    case["c1"] = case["c1"] + 1
    case["c2"] = case["c2"] + 1
    case["c3"] = case["c3"] + 1
    case["c4"] = case["c4"] + 1
    case["c5"] = case["c5"] + 1

def CI():
    case["a3"] = case["a3"] + 1
    case["a4"] = case["a4"] + 1
    case["b1"] = case["b1"] + 1
    case["b2"] = case["b2"] + 1
    case["b3"] = case["b3"] + 1

def DE():
    case["e2"] = case["e2"] + 1

def DF():
    case["e2"] = case["e2"] + 1
    case["e3"] = case["e3"] + 1

def DG():
    case["d1"] = case["d1"] + 1
    case["d2"] = case["d2"] + 1
    case["d3"] = case["d3"] + 1
    case["d4"] = case["d4"] + 1
    case["d5"] = case["d5"] + 1
    case["e2"] = case["e2"] + 1
    case["e3"] = case["e3"] + 1
    case["e4"] = case["e4"] + 1

def DH():
    case["c3"] = case["c3"] + 1
    case["c4"] = case["c4"] + 1
    case["c5"] = case["c5"] + 1
    case["d1"] = case["d1"] + 1
    case["d2"] = case["d2"] + 1
    case["d3"] = case["d3"] + 1

def DI():
    case["a4"] = case["a4"] + 1
    case["b3"] = case["b3"] + 1
    case["b4"] = case["b4"] + 1
    case["c2"] = case["c2"] + 1
    case["c3"] = case["c3"] + 1
    case["d1"] = case["d1"] + 1
    case["d2"] = case["d2"] + 1

# Rien pour EF

def EG():
    case["e3"] = case["e3"] + 1
    case["e4"] = case["e4"] + 1

def EH():
    case["c5"] = case["c5"] + 1
    case["d4"] = case["d4"] + 1
    case["d5"] = case["d5"] + 1
    case["e2"] = case["e2"] + 1
    case["e3"] = case["e3"] + 1

def EI():
    case["b4"] = case["b4"] + 1
    case["c3"] = case["c3"] + 1
    case["c4"] = case["c4"] + 1
    case["d3"] = case["d3"] + 1
    case["e2"] = case["e2"] + 1
    case["e3"] = case["e3"] + 1

def FG():
    case["e4"] = case["e4"] + 1

def FH():
    case["c5"] = case["c5"] + 1
    case["d5"] = case["d5"] + 1
    case["e4"] = case["e4"] + 1

def FI():
    case["b5"] = case["b5"] + 1
    case["c4"] = case["c4"] + 1
    case["c5"] = case["c5"] + 1
    case["d4"] = case["d4"] + 1
    case["e4"] = case["e4"] + 1

# Rien pour GH

def GI():
    case["b5"] = case["b5"] + 1
    case["c5"] = case["c5"] + 1
    case["d5"] = case["d5"] + 1

def HI():
    case["b5"] = case["b5"] + 1


def END():
    case["a2"] = case["a2"]


# Annuler action motif

def rAB():
    case["a2"] = case["a2"] - 1

def rAC():
    case["a2"] = case["a2"] - 1
    case["b1"] = case["b1"] - 1

def rAD():
    case["a2"] = case["a2"] - 1
    case["a3"] = case["a3"] - 1
    case["b2"] = case["b2"] - 1
    case["c1"] = case["c1"] - 1
    case["c2"] = case["c2"] - 1
    case["d1"] = case["d1"] - 1

def rAE():
    case["a3"] = case["a3"] - 1
    case["b3"] = case["b3"] - 1
    case["c2"] = case["c2"] - 1
    case["c3"] = case["c3"] - 1
    case["d2"] = case["d2"] - 1
    case["e2"] = case["e2"] - 1

def rAF():
    case["a3"] = case["a3"] - 1
    case["b3"] = case["b3"] - 1
    case["c3"] = case["c3"] - 1
    case["c4"] = case["c4"] - 1
    case["d4"] = case["d4"] - 1
    case["e4"] = case["e4"] - 1

def rAG():
    case["a3"] = case["a3"] - 1
    case["a4"] = case["a4"] - 1
    case["b4"] = case["b4"] - 1
    case["c4"] = case["c4"] - 1
    case["c5"] = case["c5"] - 1
    case["d5"] = case["d5"] - 1

def rAH():
    case["a4"] = case["a4"] - 1
    case["b5"] = case["b5"] - 1

def rAI():
    case["a4"] = case["a4"] - 1

def rBC():
    case["b1"] = case["b1"] - 1

def rBD():
    case["b1"] = case["b1"] - 1
    case["c1"] = case["c1"] - 1
    case["d1"] = case["d1"] - 1

def rBE():
    case["b1"] = case["b1"] - 1
    case["c1"] = case["c1"] - 1
    case["c2"] = case["c2"] - 1
    case["d2"] = case["d2"] - 1
    case["e2"] = case["e2"] - 1

def rBF():
    case["b2"] = case["b2"] - 1
    case["c2"] = case["c2"] - 1
    case["c3"] = case["c3"] - 1
    case["d3"] = case["d3"] - 1
    case["e3"] = case["e3"] - 1
    case["e4"] = case["e4"] - 1

def rBG():
    case["a2"] = case["a2"] - 1
    case["b2"] = case["b2"] - 1
    case["b3"] = case["b3"] - 1
    case["c3"] = case["c3"] - 1
    case["c4"] = case["c4"] - 1
    case["d4"] = case["d4"] - 1
    case["d5"] = case["d5"] - 1

def rBH():
    case["a2"] = case["a2"] - 1
    case["a3"] = case["a3"] - 1
    case["b3"] = case["b3"] - 1
    case["b4"] = case["b4"] - 1
    case["b5"] = case["b5"] - 1

def rBI():
    case["a2"] = case["a2"] - 1
    case["a3"] = case["a3"] - 1
    case["a4"] = case["a4"] - 1

# Rien pour CD

def rCE():
    case["c1"] = case["c1"] - 1
    case["d1"] = case["d1"] - 1
    case["e2"] = case["e2"] - 1

def rCF():
    case["c1"] = case["c1"] - 1
    case["d1"] = case["d1"] - 1
    case["d2"] = case["d2"] - 1
    case["e3"] = case["e3"] - 1
    case["e4"] = case["e4"] - 1

def rCG():
    case["c1"] = case["c1"] - 1
    case["c2"] = case["c2"] - 1
    case["c3"] = case["c3"] - 1
    case["d3"] = case["d3"] - 1
    case["d4"] = case["d4"] - 1
    case["d5"] = case["d5"] - 1

def rCH():
    case["b1"] = case["b1"] - 1
    case["b2"] = case["b2"] - 1
    case["b3"] = case["b3"] - 1
    case["b4"] = case["b4"] - 1
    case["b5"] = case["b5"] - 1
    case["c1"] = case["c1"] - 1
    case["c2"] = case["c2"] - 1
    case["c3"] = case["c3"] - 1
    case["c4"] = case["c4"] - 1
    case["c5"] = case["c5"] - 1

def rCI():
    case["a3"] = case["a3"] - 1
    case["a4"] = case["a4"] - 1
    case["b1"] = case["b1"] - 1
    case["b2"] = case["b2"] - 1
    case["b3"] = case["b3"] - 1

def rDE():
    case["e2"] = case["e2"] - 1

def rDF():
    case["e2"] = case["e2"] - 1
    case["e3"] = case["e3"] - 1

def rDG():
    case["d1"] = case["d1"] - 1
    case["d2"] = case["d2"] - 1
    case["d3"] = case["d3"] - 1
    case["d4"] = case["d4"] - 1
    case["d5"] = case["d5"] - 1
    case["e2"] = case["e2"] - 1
    case["e3"] = case["e3"] - 1
    case["e4"] = case["e4"] - 1

def rDH():
    case["c3"] = case["c3"] - 1
    case["c4"] = case["c4"] - 1
    case["c5"] = case["c5"] - 1
    case["d1"] = case["d1"] - 1
    case["d2"] = case["d2"] - 1
    case["d3"] = case["d3"] - 1

def rDI():
    case["a4"] = case["a4"] - 1
    case["b3"] = case["b3"] - 1
    case["b4"] = case["b4"] - 1
    case["c2"] = case["c2"] - 1
    case["c3"] = case["c3"] - 1
    case["d1"] = case["d1"] - 1
    case["d2"] = case["d2"] - 1

# Rien pour EF

def rEG():
    case["e3"] = case["e3"] - 1
    case["e4"] = case["e4"] - 1

def rEH():
    case["c5"] = case["c5"] - 1
    case["d4"] = case["d4"] - 1
    case["d5"] = case["d5"] - 1
    case["e2"] = case["e2"] - 1
    case["e3"] = case["e3"] - 1

def rEI():
    case["b4"] = case["b4"] - 1
    case["c3"] = case["c3"] - 1
    case["c4"] = case["c4"] - 1
    case["d3"] = case["d3"] - 1
    case["e2"] = case["e2"] - 1
    case["e3"] = case["e3"] - 1

def rFG():
    case["e4"] = case["e4"] - 1

def rFH():
    case["c5"] = case["c5"] - 1
    case["d5"] = case["d5"] - 1
    case["e4"] = case["e4"] - 1

def rFI():
    case["b5"] = case["b5"] - 1
    case["c4"] = case["c4"] - 1
    case["c5"] = case["c5"] - 1
    case["d4"] = case["d4"] - 1
    case["e4"] = case["e4"] - 1

# Rien pour GH

def rGI():
    case["b5"] = case["b5"] - 1
    case["c5"] = case["c5"] - 1
    case["d5"] = case["d5"] - 1

def rHI():
    case["b5"] = case["b5"] - 1


def rEND():
    case["a2"] = case["a2"]


# Objectif final
objectif = {"oa2": 0, "oa3": 0, "oa4": 0, "ob1": 0, "ob2": 100, "ob3": 0, "ob4": 100, "ob5": 0, "oc1": 0, "oc2": 0, "oc3": 0, "oc4": 0, "oc5": 0, "od1": 0, "od2": 100, "od3": 100, "od4": 100, "od5": 0, "oe2": 0, "oe3": 0, "oe4": 0}

# Indice de choix du motif
dico_idM = {"idM": 0}

def idMotif():
    dico_idM["idM"] = abs(objectif["oa2"] - case["a2"]) + abs(objectif["oa3"] - case["a3"]) + abs(objectif["oa4"] - case["a4"]) + abs(objectif["ob1"] - case["b1"]) + abs(objectif["ob2"] - case["b2"]) + abs(objectif["ob3"] - case["b3"]) + abs(objectif["ob4"] - case["b4"]) + abs(objectif["ob5"] - case["b5"]) + abs(objectif["oc1"] - case["c1"]) + abs(objectif["oc2"] - case["c2"]) + abs(objectif["oc3"] - case["c3"]) + abs(objectif["oc4"] - case["c4"]) + abs(objectif["oc5"] - case["c5"]) + abs(objectif["od1"] - case["d1"]) + abs(objectif["od2"] - case["d2"]) + abs(objectif["od3"] - case["d3"]) + abs(objectif["od4"] - case["d4"]) + abs(objectif["od5"] - case["d5"]) + abs(objectif["oe2"] - case["e2"]) + abs(objectif["oe3"] - case["e3"]) + abs(objectif["oe4"] - case["e4"])     # x coef optionnel sur les bords car moins importants
    # print("idM : ", dico_idM["idM"])
    # print("idM de a2 : ", abs(objectif["oa2"] - case["a2"]))
    # print("idM de a3 : ", abs(objectif["oa3"] - case["a3"]))
    # print("idM de a4 : ", abs(objectif["oa4"] - case["a4"]))
    # print("idM de b1 : ", abs(objectif["ob1"] - case["b1"]))

# Définition de l'idM par motif
idM_motif = {"idAB": 0, "idAC": 0, "idAD": 0, "idAE": 0, "idAF": 0, "idAG": 0, "idAH": 0, "idAI": 0, "idBC": 0, "idBD": 0, "idBE": 0, "idBF": 0, "idBG": 0, "idBH": 0, "idBI": 0, "idCD": 1000, "idCE": 0, "idCF": 0, "idCG": 0, "idCH": 0, "idCI": 0, "idDE": 0, "idDF": 0, "idDG": 0, "idDH": 0, "idDI": 0, "idEF": 1000, "idEG": 0, "idEH": 0, "idEI": 0, "idFG": 0, "idFH": 0, "idFI": 0, "idGH": 1000, "idGI": 0, "idHI": 0, "idEND": 0}

def idM_par_motif():
    AB()
    # print("idM pour AB :")
    idMotif()
    idM_motif["idAB"] = dico_idM["idM"] + totMotif["totAB"]
    rAB()
    print("idAB : ", idM_motif["idAB"])

    AC()
    # print("idM pour AC :")
    idMotif()
    idM_motif["idAC"] = dico_idM["idM"] + totMotif["totAC"]
    rAC()
    print("idAC : ", idM_motif["idAC"])

    AD()
    idMotif()
    idM_motif["idAD"] = dico_idM["idM"] + totMotif["totAD"]
    rAD()
    print("idAD : ", idM_motif["idAD"])

    AE()
    idMotif()
    idM_motif["idAE"] = dico_idM["idM"] + totMotif["totAE"]
    rAE()
    print("idAE : ", idM_motif["idAE"])

    AF()
    idMotif()
    idM_motif["idAF"] = dico_idM["idM"] + totMotif["totAF"]
    rAF()
    print("idAF : ", idM_motif["idAF"])

    AG()
    idMotif()
    idM_motif["idAG"] = dico_idM["idM"] + totMotif["totAG"]
    rAG()
    print("idAG : ", idM_motif["idAG"])

    AH()
    idMotif()
    idM_motif["idAH"] = dico_idM["idM"] + totMotif["totAH"]
    rAH()
    print("idAH : ", idM_motif["idAH"])

    AI()
    idMotif()
    idM_motif["idAI"] = dico_idM["idM"] + totMotif["totAI"]
    rAI()
    print("idAI : ", idM_motif["idAI"])

    BC()
    idMotif()
    idM_motif["idBC"] = dico_idM["idM"] + totMotif["totBC"]
    rBC()
    print("idBC : ", idM_motif["idBC"])

    BD()
    idMotif()
    idM_motif["idBD"] = dico_idM["idM"] + totMotif["totBD"]
    rBD()
    print("idBD : ", idM_motif["idBD"])

    BE()
    idMotif()
    idM_motif["idBE"] = dico_idM["idM"] + totMotif["totBE"]
    rBE()
    print("idBE : ", idM_motif["idBE"])

    BF()
    idMotif()
    idM_motif["idBF"] = dico_idM["idM"] + totMotif["totBF"]
    rBF()
    print("idBF : ", idM_motif["idBF"])

    BG()
    idMotif()
    idM_motif["idBG"] = dico_idM["idM"] + totMotif["totBG"]
    rBG()
    print("idBG : ", idM_motif["idBG"])

    BH()
    idMotif()
    idM_motif["idBH"] = dico_idM["idM"] + totMotif["totBH"]
    rBH()
    print("idBH : ", idM_motif["idBH"])

    BI()
    idMotif()
    idM_motif["idBI"] = dico_idM["idM"] + totMotif["totBI"]
    rBI()
    print("idBI : ", idM_motif["idBI"])

    CE()
    idMotif()
    idM_motif["idCE"] = dico_idM["idM"] + totMotif["totCE"]
    rCE()
    print("idCE : ", idM_motif["idCE"])

    CF()
    idMotif()
    idM_motif["idCF"] = dico_idM["idM"] + totMotif["totCF"]
    rCF()
    print("idCF : ", idM_motif["idCF"])

    CG()
    idMotif()
    idM_motif["idCG"] = dico_idM["idM"] + totMotif["totCG"]
    rCG()
    print("idCG : ", idM_motif["idCG"])

    CH()
    idMotif()
    idM_motif["idCH"] = dico_idM["idM"] + totMotif["totCH"]
    rCH()
    print("idCH : ", idM_motif["idCH"])

    CI()
    idMotif()
    idM_motif["idCI"] = dico_idM["idM"] + totMotif["totCI"]
    rCI()
    print("idCI : ", idM_motif["idCI"])

    DE()
    idMotif()
    idM_motif["idDE"] = dico_idM["idM"] + totMotif["totDE"]
    rDE()
    print("idDE : ", idM_motif["idDE"])

    DF()
    idMotif()
    idM_motif["idDF"] = dico_idM["idM"] + totMotif["totDF"]
    rDF()
    print("idDF : ", idM_motif["idDF"])

    DG()
    idMotif()
    idM_motif["idDG"] = dico_idM["idM"] + totMotif["totDG"]
    rDG()
    print("idDG : ", idM_motif["idDG"])

    DH()
    idMotif()
    idM_motif["idDH"] = dico_idM["idM"] + totMotif["totDH"]
    rDH()
    print("idDH : ", idM_motif["idDH"])

    DI()
    idMotif()
    idM_motif["idDI"] = dico_idM["idM"] + totMotif["totDI"]
    rDI()
    print("idDI : ", idM_motif["idDI"])

    EG()
    idMotif()
    idM_motif["idEG"] = dico_idM["idM"] + totMotif["totEG"]
    rEG()
    print("idEG : ", idM_motif["idEG"])

    EH()
    idMotif()
    idM_motif["idEH"] = dico_idM["idM"] + totMotif["totEH"]
    rEH()
    print("idEH : ", idM_motif["idEH"])

    EI()
    idMotif()
    idM_motif["idEI"] = dico_idM["idM"] + totMotif["totEI"]
    rEI()
    print("idEI : ", idM_motif["idEI"])

    FG()
    idMotif()
    idM_motif["idFG"] = dico_idM["idM"] + totMotif["totFG"]
    rFG()
    print("idFG : ", idM_motif["idFG"])

    FH()
    idMotif()
    idM_motif["idFH"] = dico_idM["idM"] + totMotif["totFH"]
    rFH()
    print("idFH : ", idM_motif["idFH"])

    FI()
    idMotif()
    idM_motif["idFI"] = dico_idM["idM"] + totMotif["totFI"]
    rFI()
    print("idFI : ", idM_motif["idFI"])

    GI()
    idMotif()
    idM_motif["idGI"] = dico_idM["idM"] + totMotif["totGI"]
    rGI()
    print("idGI : ", idM_motif["idGI"])

    HI()
    idMotif()
    idM_motif["idHI"] = dico_idM["idM"] + totMotif["totHI"]
    rHI()
    print("idHI : ", idM_motif["idHI"])

    END()
    # print("idM pour END :")
    idMotif()
    idM_motif["idEND"] = dico_idM["idM"]
    rEND()
    print("idEND : ", idM_motif["idEND"])


# Nombre d'utilisation totale de chaque motif
totMotif = {"totAB": 0, "totAC": 0, "totAD": 0, "totAE": 0, "totAF": 0, "totAG": 0, "totAH": 0, "totAI": 0, "totBC": 0, "totBD": 0, "totBE": 0, "totBF": 0, "totBG": 0, "totBH": 0, "totBI": 0, "totCD": 0, "totCE": 0, "totCF": 0, "totCG": 0, "totCH": 0, "totCI": 0, "totDE": 0, "totDF": 0, "totDG": 0, "totDH": 0, "totDI": 0, "totEF": 0, "totEG": 0, "totEH": 0, "totEI": 0, "totFG": 0, "totFH": 0, "totFI": 0, "totGH": 0, "totGI": 0, "totHI": 0, "totEND": 0}

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
    if 'idAD' in str(res):
        AD()
        print("-> apply AD")
        totMotif["totAD"] = totMotif["totAD"] + 1
    if 'idAE' in str(res):
        AE()
        print("-> apply AE")
        totMotif["totAE"] = totMotif["totAE"] + 1
    if 'idAF' in str(res):
        AF()
        print("-> apply AF")
        totMotif["totAF"] = totMotif["totAF"] + 1
    if 'idAG' in str(res):
        AG()
        print("-> apply AG")
        totMotif["totAG"] = totMotif["totAG"] + 1
    if 'idAH' in str(res):
        AH()
        print("-> apply AH")
        totMotif["totAH"] = totMotif["totAH"] + 1
    if 'idAI' in str(res):
        AI()
        print("-> apply AI")
        totMotif["totAI"] = totMotif["totAI"] + 1
    if 'idBC' in str(res):
        BC()
        print("-> apply BC")
        totMotif["totBC"] = totMotif["totBC"] + 1
    if 'idBD' in str(res):
        BD()
        print("-> apply BD")
        totMotif["totBD"] = totMotif["totBD"] + 1
    if 'idBE' in str(res):
        BE()
        print("-> apply BE")
        totMotif["totBE"] = totMotif["totBE"] + 1
    if 'idBF' in str(res):
        BF()
        print("-> apply BF")
        totMotif["totBF"] = totMotif["totBF"] + 1
    if 'idBG' in str(res):
        BG()
        print("-> apply BG")
        totMotif["totBG"] = totMotif["totBG"] + 1
    if 'idBH' in str(res):
        BH()
        print("-> apply BH")
        totMotif["totBH"] = totMotif["totBH"] + 1
    if 'idBI' in str(res):
        BI()
        print("-> apply BI")
        totMotif["totBI"] = totMotif["totBI"] + 1
    if 'idCE' in str(res):
        CE()
        print("-> apply CE")
        totMotif["totCE"] = totMotif["totCE"] + 1
    if 'idCF' in str(res):
        CF()
        print("-> apply CF")
        totMotif["totCF"] = totMotif["totCF"] + 1
    if 'idCG' in str(res):
        CG()
        print("-> apply CG")
        totMotif["totCG"] = totMotif["totCG"] + 1
    if 'idCH' in str(res):
        CH()
        print("-> apply CH")
        totMotif["totCH"] = totMotif["totCH"] + 1
    if 'idCI' in str(res):
        CI()
        print("-> apply CI")
        totMotif["totCI"] = totMotif["totCI"] + 1
    if 'idDE' in str(res):
        DE()
        print("-> apply DE")
        totMotif["totDE"] = totMotif["totDE"] + 1
    if 'idDF' in str(res):
        DF()
        print("-> apply DF")
        totMotif["totDF"] = totMotif["totDF"] + 1
    if 'idDG' in str(res):
        DG()
        print("-> apply DG")
        totMotif["totDG"] = totMotif["totDG"] + 1
    if 'idDH' in str(res):
        DH()
        print("-> apply DH")
        totMotif["totDH"] = totMotif["totDH"] + 1
    if 'idDI' in str(res):
        DI()
        print("-> apply DI")
        totMotif["totDI"] = totMotif["totDI"] + 1
    if 'idEG' in str(res):
        EG()
        print("-> apply EG")
        totMotif["totEG"] = totMotif["totEG"] + 1
    if 'idEH' in str(res):
        EH()
        print("-> apply EH")
        totMotif["totEH"] = totMotif["totEH"] + 1
    if 'idEI' in str(res):
        EI()
        print("-> apply EI")
        totMotif["totEI"] = totMotif["totEI"] + 1
    if 'idFG' in str(res):
        FG()
        print("-> apply FG")
        totMotif["totFG"] = totMotif["totFG"] + 1
    if 'idFH' in str(res):
        FH()
        print("-> apply FH")
        totMotif["totFH"] = totMotif["totFH"] + 1
    if 'idFI' in str(res):
        FI()
        print("-> apply FI")
        totMotif["totFI"] = totMotif["totFI"] + 1
    if 'idGI' in str(res):
        GI()
        print("-> apply GI")
        totMotif["totGI"] = totMotif["totGI"] + 1
    if 'idHI' in str(res):
        HI()
        print("-> apply HI")
        totMotif["totHI"] = totMotif["totHI"] + 1
    if 'idEND' in str(res):
        print("-> stop")
        totMotif["totEND"] = totMotif["totEND"] + 1
        
    

print("Valeurs finales des cases :", case)
print("Nombre d'utilisations de AB : ", totMotif["totAB"])
print("Nombre d'utilisations de AC : ", totMotif["totAC"])
print("Nombre d'utilisations de AD : ", totMotif["totAD"])
print("Nombre d'utilisations de AE : ", totMotif["totAE"])
print("Nombre d'utilisations de AF : ", totMotif["totAF"])
print("Nombre d'utilisations de AG : ", totMotif["totAG"])
print("Nombre d'utilisations de AH : ", totMotif["totAH"])
print("Nombre d'utilisations de AI : ", totMotif["totAI"])
print("Nombre d'utilisations de BC : ", totMotif["totBC"])
print("Nombre d'utilisations de BD : ", totMotif["totBD"])
print("Nombre d'utilisations de BE : ", totMotif["totBE"])
print("Nombre d'utilisations de BF : ", totMotif["totBF"])
print("Nombre d'utilisations de BG : ", totMotif["totBG"])
print("Nombre d'utilisations de BH : ", totMotif["totBH"])
print("Nombre d'utilisations de BI : ", totMotif["totBI"])
print("Nombre d'utilisations de CD : ", totMotif["totCD"])
print("Nombre d'utilisations de CE : ", totMotif["totCE"])
print("Nombre d'utilisations de CF : ", totMotif["totCF"])
print("Nombre d'utilisations de CG : ", totMotif["totCG"])
print("Nombre d'utilisations de CH : ", totMotif["totCH"])
print("Nombre d'utilisations de CI : ", totMotif["totCI"])
print("Nombre d'utilisations de DE : ", totMotif["totDE"])
print("Nombre d'utilisations de DF : ", totMotif["totDF"])
print("Nombre d'utilisations de DG : ", totMotif["totDG"])
print("Nombre d'utilisations de DH : ", totMotif["totDH"])
print("Nombre d'utilisations de DI : ", totMotif["totDI"])
print("Nombre d'utilisations de EF : ", totMotif["totEF"])
print("Nombre d'utilisations de EG : ", totMotif["totEG"])
print("Nombre d'utilisations de EH : ", totMotif["totEH"])
print("Nombre d'utilisations de EI : ", totMotif["totEI"])
print("Nombre d'utilisations de FG : ", totMotif["totFG"])
print("Nombre d'utilisations de FH : ", totMotif["totFH"])
print("Nombre d'utilisations de FI : ", totMotif["totFI"])
print("Nombre d'utilisations de GH : ", totMotif["totGH"])
print("Nombre d'utilisations de GI : ", totMotif["totGI"])
print("Nombre d'utilisations de HI : ", totMotif["totHI"])
