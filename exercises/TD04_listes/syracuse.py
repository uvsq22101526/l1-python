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

print(syracuse(3))

'''La conjecture de Collatz (ou problème de Syracuse) affirme que, quel que soit l’entier `n` que l’on
choisisse au départ, on finit toujours par arriver à 1 (ce résultat est une conjecture, c'est-à-dire
qu'il n'a pas été démontré, mais qu'il n'existe pas de contre-exemple connu).
Écrire une fonction qui, en appelant la fonction précédente, va vérifier si la conjecture est vraie pour
`n` de 1 à `n_max`, où `n_max` est un paramètre de la fonction. 

Remarque: si tout se passe bien, la fonction doit juste se terminer et renvoyer `True` par exemple.
Sinon, c’est qu’on sera entré dans une boucle infinie.'''

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    
    for i in range(2, n_max + 2):
        syracuse(n_max)

    return True

print(testeConjecture(10000))