import time

def tempsEnSeconde(temps):
    jour = temps[0]
    heure = temps[1]
    minute = temps[2]
    seconde = temps[3]
    seconde = seconde + (jour*86400) + (heure*3600) + (minute*60)
    return seconde

#temps = (3,23,1,34)
#print(type(temps))
#print(tempsEnSeconde(temps))   

#faire celle ci
def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    seconde = (seconde // 86400, (seconde % 86400) // 3600, ((seconde % 86400) % 3600) // 60, ((seconde % 86400) % 3600) % 60)
    return seconde 

#temps = secondeEnTemps(100000)
#print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")

def accord(liste):
    if liste == 1:
        print(" ", end="")
    else:
        print("s ", end="")

def afficheTemps(temps):
    jour = temps[0]
    if jour == 0:
        print("", end="")
    else:
        print(jour, "jour", end="")
        accord(jour)
    heure = temps[1]
    if heure == 0:
        print("", end="")
    else:
        print(heure, "heure", end="")
        accord(heure)
    minute = temps[2]
    if minute == 0:
        print("", end="")
    else:
        print(minute, "minute", end="")
        accord(minute)
    seconde = temps[3]
    if seconde == 0:
        print("", end="")
    else:
        print(seconde, "seconde", end="")
        accord(seconde)
    
#afficheTemps((1,0,14,23))  

def demandeTemps():
    jour = int(input("Rentre un nombre de jours"))
    heure = int(input("Rentre un nombre d'heures"))
    while heure > 23:
        heure = int(input("Rentre un nombre d'heures en-dessous de 24"))
    minute = int(input("Rentre un nombre de minutes"))
    while minute > 59:
        minute = int(input("Rentre un nombre de minutes en-dessous de 60"))
    seconde = int(input("Rentre un nombre de secondes"))
    while seconde > 59 :
        seconde = int(input("Rentre un nombre de secondes en-dessous de 60"))
    return jour, heure, minute, seconde

#afficheTemps(demandeTemps())

def sommeTemps(temps1,temps2):
    return temps1[0] + temps2[0], temps1[1] + temps2[1], temps1[2] + temps2[2], temps1[3] + temps2[3]

#afficheTemps(sommeTemps((2,3,4,25),(5,22,57,1)))

def proportionTemps(temps,proportion):
    temps = int(proportion * tempsEnSeconde(temps))
    temps = secondeEnTemps(temps)
    return temps

#afficheTemps(proportionTemps(proportion = 0.2, temps = (2,0,36,0)))

#afficher un temps sous forme de date

def tempsEnDate(temps):
    jour = temps[0]
    heure = temps[1]
    minute = temps[2]
    seconde = temps[3]
    an = jour // 365 
    jour = jour % 365
    affichage = (an, jour, heure, minute, seconde)
    return affichage

def afficheDate(affichage):
    an = affichage[0]
    jour = affichage[1]
    heure = affichage[2]
    minute = affichage[3]
    seconde = affichage[4]
    an = an + 1970
    print( jour, an, "à", heure, ":", minute, ":", seconde)
    
#temps = secondeEnTemps(1000000000)
#afficheTemps(temps)
#tempsEnDate(temps)
#afficheDate(tempsEnDate(temps))


