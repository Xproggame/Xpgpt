def assemblement(puissance:int, texte:list):
    return [texte[len(texte) - 1], texte[:len(texte) - 1]]

def separation(texte:str):
    texte_traite = []
    puissance = 1
    texte = texte.split()
    taille = len(texte)

    for x in range(len(texte) - 1):
        print(str((x + 1) / taille * 100) + "%")

        if x >= puissance:
            texte_traite.append(assemblement(puissance, texte[x - 1:x + 1]))

    return texte_traite

"""def enregistrement(texte_traite:list):
    fichier = open("ressource.txt", 'a+')

    for mot in texte_traite:

        for texte in mot[1]:"""
