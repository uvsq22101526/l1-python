# temps en seconde

def tempsEnSeconde(temps):
    """Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    seconde = temps[0] * 86400 + temps[1] * 3600 + temps [2] * 60 + temps [3]
    return seconde

temps = (3,23,1,34)
#print(type(temps))
#print(tempsEnSeconde(temps))


# seconde en temps

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    seconde = (seconde // 86400, (seconde % 86400) // 3600, ((seconde % 86400) % 3600) // 60, ((seconde % 86400) % 3600) % 60)
    return seconde
    
temps = secondeEnTemps(100000)
#print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")


# affichage du temps

def afficheTemps(temps):
    '''Fonction d'affichage du temps'''
    if temps[0] > 1:
        print(temps[0], "jours ", end="")
    elif temps[0] == 1:
        print(temps[0], "jour ", end="")
    else:
        print("", end = "")
    if temps[1] > 1:
        print(temps[1], "heures ", end="")
    elif temps[1] == 1:
        print(temps[0], "heure ", end="")
    else:
        print("", end = "")
    if temps[2] > 1:
        print(temps[2], "minutes ", end="")
    elif temps[2] == 1:
        print(temps[2], "minute ", end="")
    else:
        print("", end = "")
    if temps[3] > 1:
        print(temps[3], "secondes")
    elif temps[3] == 1:
        print(temps[3], "seconde")
    else:
        print("")
    return temps
    
#afficheTemps((1,0,14,23))


# demande du temps

def demandeTemps():
    jour = int(input("Rentre un nombre de jours "))
    heure = int(input("Rentre un nombre d'heures "))
    while heure > 23:
        heure = int(input("Rentre un nombre d'heures en-dessous de 24 "))
    minute = int(input("Rentre un nombre de minutes "))
    while minute > 59:
        minute = int(input("Rentre un nombre de minutes en-dessous de 60 "))
    seconde = int(input("Rentre un nombre de secondes "))
    while seconde > 59 :
        seconde = int(input("Rentre un nombre de secondes en-dessous de 60 "))
    return jour, heure, minute, seconde

#afficheTemps(demandeTemps())


# somme de temps

def sommeTemps(temps1,temps2):
    temps = temps1[0] + temps2[0], temps1[1] + temps2[1], temps1[2] + temps2[2], temps1[3] + temps2[3]
    temps = afficheTemps(secondeEnTemps(tempsEnSeconde(temps)))
    return temps

#sommeTemps((2,3,4,25),(5,22,57,1))


# calculer le pourcentage d'un temps

def proportionTemps(temps,proportion):
    temps = int(proportion * tempsEnSeconde(temps))
    temps = secondeEnTemps(temps)
    return temps

#afficheTemps(proportionTemps(proportion = 0.2, temps = (2,0,36,0)))


# afficher un temps sous forme de date

def tempsEnDate(temps):
    #temps = tempsEnSeconde(temps)
    temps = temps // 31536000, (temps % 31536000) // 86400, ((temps % 31536000) % 86400) // 3600, \
        (((temps % 31536000) % 86400) % 3600) // 60, ((((temps % 31536000) % 86400) % 3600) % 60) 
    return temps


def afficheDate(date = -1):
    pass
    
#temps = secondeEnTemps(1000000000)
#afficheTemps(temps)
print(tempsEnDate(1000000000))
#afficheDate(tempsEnDate(temps))
#afficheDate()