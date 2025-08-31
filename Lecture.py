def statistique(texte:str, puissance:int):

    if len(texte) <= puissance:
        fichier = open("ressource.txt", 'r+')

        for ligne in fichier.read():
            ligne_traite = ligne.split('|')
            ligne_traite[1] = ligne_traite[1].split('/')
            pass