import random
import random

aleatoire = random.Random()

def statistique(texte:list, puissance:int):

    if len(texte) <= puissance:
        fichier = open("ressource.txt", 'r+')
        list_mots = []

        for ligne in fichier:
            ligne = ligne.replace('\n', '')
            ligne_traite = ligne.split('|')
            ligne_traite[1] = ligne_traite[1].split('/')
            point_def = 0

            for point in range(len(ligne_traite[1]) - 1):

                if point + 1 != puissance:

                    if ligne_traite[1][0] == texte[0]:

                        if ligne_traite[1][point] != texte[point]:
                            point_def = point
                            break

                    else:
                        break

                else:
                    point_def = point
                    break

            list_mots.append([ligne_traite[0], point_def])

        fichier.close()
        list_mots_def = []
        poids = []

        for mot in list_mots:

            list_mots_def.append(mot[0])
            poids.append(mot[1])

        mot_final = aleatoire.choices(list_mots_def, weights = poids, k = 1)