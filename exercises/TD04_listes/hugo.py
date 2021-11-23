'''Créer une liste à deux dimensions affectée à  la variable `carre_mag` contenant ce carré magique.'''

carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]

#carre_pas_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 7, 13]]
carre_pas_mag = [list(i) for i in carre_mag]
carre_pas_mag[3][2] = 7

def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    
    return print(carre[0]), print(carre[1]), print(carre[2]), print(carre[3])

afficheCarre(carre_mag)
#afficheCarre(carre_pas_mag)


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    
    somme_0 = carre[0][0] + carre[0][1] + carre[0][2] + carre[0][3]
    somme_1 = carre[1][0] + carre[1][1] + carre[1][2] + carre[1][3]
    somme_2 = carre[2][0] + carre[2][1] + carre[2][2] + carre[2][3]
    somme_3 = carre[3][0] + carre[3][1] + carre[3][2] + carre[3][3]
    
    if somme_0 == somme_1 and somme_1 == somme_2 and somme_2 == somme_3:
        return somme_1
    else:
        return -1

#print(testLignesEgales(carre_mag))
#print(testLignesEgales(carre_pas_mag))

def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    
    somme_0 = carre[0][0] + carre[1][0] + carre[2][0] + carre[3][0]
    somme_1 = carre[0][1] + carre[1][1] + carre[2][1] + carre[3][1]
    somme_2 = carre[0][2] + carre[1][2] + carre[2][2] + carre[3][2]
    somme_3 = carre[0][3] + carre[1][3] + carre[2][3] + carre[3][3]
    
    if somme_0 == somme_1 and somme_1 == somme_2 and somme_2 == somme_3:
        return somme_1
    else:
        return -1

#print(testColonnesEgales(carre_mag))
#print(testColonnesEgales(carre_pas_mag))

def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    
    somme_1 = carre[0][0] + carre[1][1] + carre[2][2] + carre[3][3]
    somme_2 = carre[0][3] + carre[1][2] + carre[2][1] + carre[3][0]

    if somme_1 == somme_2:
        return somme_1
    else:
        return -1
    
#print(testDiagonalesEgales(carre_mag))
#print(testDiagonalesEgales(carre_pas_mag))


def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    if testLignesEgales(carre) == testColonnesEgales(carre) and testColonnesEgales(carre) == testDiagonalesEgales(carre):
        return True
    
    else:
        return False

#print(estCarreMagique(carre_mag))
#print(estCarreMagique(carre_pas_mag))


'''def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille du carré, et False sinon """
    somme = 0
    
    for i in range(1, 4 * 4 + 1):
        if i in carre[0]:
            somme += 1
            
        if i in carre[1]:
            somme += 1
        
        if i in carre[2]:
            somme += 1
            
        if i in carre[3]:
            somme += 1
            
    if somme == 4 * 4:
        return True
    
    else:
        return False'''


def estNormal(carre):
    array = []
    array_bis = []
    
    for i in range(4):
        for j in range(4):
            array.append(carre[i][j])
            
    array_bis = sorted(array)
    valide = [i for i in range(1, 16 + 1)]   
    if valide == array_bis:
        return True
    else :
        return False 
            
print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))