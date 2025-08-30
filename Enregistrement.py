def assemblement(puissance:int, texte:list):
    index = puissance - 1
    nouv_texte = [texte[len(texte) - 1], []]

    while index != -1:
        nouv_texte[1].append(texte[index])
        index -= 1

    return nouv_texte

def separation(texte:str):
    texte_traite = []
    puissance = 3
    texte = texte.split()
    taille = len(texte)

    for x in range(len(texte) - 1):
        print(str((x + 1) / taille * 100) + "%")

        if x >= puissance:
            texte_traite.append(assemblement(puissance, texte[x - puissance:x + 1]))

    return texte_traite

def enregistrement(texte_traite:list):
    fichier = open("ressource.txt", 'a+')

    for mot in texte_traite:
        assemblement = f'{mot[0]}|'

        for texte in mot[1]:
            assemblement += f'{texte}/'

        fichier.write(f'{assemblement}\n')

    fichier.close()