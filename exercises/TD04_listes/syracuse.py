def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            liste.append(n)
        else:
            n = n * 3 + 1
            liste.append(n)

    return liste

#print(syracuse(3))

'''La conjecture de Collatz (ou problème de Syracuse) affirme que, quel que soit l’entier `n` que l’on
choisisse au départ, on finit toujours par arriver à 1 (ce résultat est une conjecture, c'est-à-dire
qu'il n'a pas été démontré, mais qu'il n'existe pas de contre-exemple connu).
Écrire une fonction qui, en appelant la fonction précédente, va vérifier si la conjecture est vraie pour
`n` de 1 à `n_max`, où `n_max` est un paramètre de la fonction. 

Remarque: si tout se passe bien, la fonction doit juste se terminer et renvoyer `True` par exemple.
Sinon, c’est qu’on sera entré dans une boucle infinie.'''

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    
    for i in range(1, n_max + 1):
        syracuse(i)

    return True

#print(testeConjecture(10000))


'''On appelle "temps de vol" de l’entier `n` le nombre d’étapes pour aller de `n` jusqu’à 1.
Le temps de vol de 1 est 0, le temps de vol de 3 est 7. Écrire une fonction qui, étant donné un paramètre `n`,
renvoie son temps de vol.'''

def tempsVol(n):
    """ Retourne le temps de vol de n """
    
    return len(syracuse(n)) - 1

#print("Le temps de vol de", 3, "est", tempsVol(3))


'''Ecrire une fonction qui, étant donné un paramètre `n_max` renvoie la liste des temps de vol de tous les entiers de 1 à `n_max`.
*Indication*: utiliser une liste en compréhension.'''

def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """

    liste = [tempsVol(i) for i in range(1, n_max + 1)]

    return liste
        
#print(tempsVolListe(100))


'''Déterminer quel entier entre 1 et 10000 a le plus grand temps de vol (réponse 6171 qui a le temps de vol 261).'''

liste = []

for i in range(1, 10000 + 1):
    liste.append(tempsVol(i))


vol_max = max(tempsVolListe(10000))
entier_vol_max = liste.index(max(tempsVolListe(10000))) + 1

print("L'entier qui a le plus grand temps de vol est", entier_vol_max, "avec un temps de vol égal à", vol_max)


'''L’altitude maximale de l'entier `n` est la plus grande valeur par laquelle passe `n` au cours de son vol.
Déterminer quel entier entre 1 et 10000 a la plus grande altitude maximale (réponse 27114424, atteint par l'entier 9663).
Ne pas hésiter à écrire de nouvelles fonctions pour cela.'''

def altitudeMax(n):
    """ Calcule l'altitude maximale d'un entier n """
    
    return max(syracuse(n))

print(altitudeMax(3))


def plusGrandeAltitudeMax(n_max):
    """ Détermine quel entier entre 1 et n_max a la plus grande altitude maximale """
    
    liste = []
    
    for i in range(1, n_max + 1):
        liste.append(altitudeMax(i))
    
    return "L'entier", liste.index(max(liste)) + 1, "a la plus grande altitude maximale qui est de", (max(liste))

print(plusGrandeAltitudeMax(10000))