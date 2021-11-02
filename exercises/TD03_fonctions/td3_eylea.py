def tempsEnSeconde(temps):
    '''Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde'''
    temps = temps[0] * 86400 + temps[1] * 3600 + temps[2] * 60 + temps[3]
    return temps


temps = (3, 23, 1, 34)
print(type(temps))
print(tempsEnSeconde(temps))