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

'''AUTRE SOLUTION : ----------------------------------------------------------------------------------------------------------------------------------------

def affichePlurielOuNon(nombre,mot):
    if nombre > 1:
        print(nombre, mot + "s", end = " ")
    elif nombre == 1:
        print(nombre, mot, end = " ")

def afficheTemps(temps):
    affichePlurielOuNon(temps[0], "jour")
    affichePlurielOuNon(temps[1], "heure")
    affichePlurielOuNon(temps[2], "minute")
    affichePlurielOuNon(temps[3], "seconde")
    print(" ")
    
-------------------------------------------------------------------------------------------------------------------------------------------------------------'''


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
    #temps = temps // 31536000, (temps % 31536000) // 86400, ((temps % 31536000) % 86400) // 3600, \
        #(((temps % 31536000) % 86400) % 3600) // 60, ((((temps % 31536000) % 86400) % 3600) % 60) 
    an = temps[0] // 365
    temps = an, temps[0] % 365, temps[1], temps[2], temps[3]
    return temps

'''OU ALORS : -----------------------------------------------------------------------------------------------------------------------------------------------

def tempsEnDate(temps):
    annee = temps[0] // 365 + 1970
    jours_restants = temps[0] % 365
    return annee, jours_restants, temps[1], temps[2], temps[3]

def afficheDate(date = -1):
    print(date[1], date[0], date[2], ":", date[3], ":", date[4])
    
    
    if date == -1:
        print("Pas de paramètre date donné")
        return

-----------------------------------------------------------------------------------------------------------------------------------------------------------'''


#le -1 indique que si lors de l'appel de la fonction aucun temps n'est donné, il affichera -1, le paramètre n'est pas obligatoire
def afficheDate(date = -1):
    an = date[0] + 1970
    jour = date[1]
    heure = date[2]
    minute = date[3]
    seconde = date[4]
    return print("Jour", jour, "de l'année", an, "à", heure, "h", minute, "min", seconde, "s")


temps = secondeEnTemps(1000000000)
#afficheTemps(temps)
print(tempsEnDate(temps))
afficheDate(tempsEnDate(temps))
#afficheDate()


def bisextile(jour):
    annee = jour // 365 + 2020
    liste = []
    compteur = 2020
    #reste = jour % 365
    for i in range(2020, annee + 1):
        compteur += 1
        if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
            liste.append(i)
    
    return print("Les années bissextiles depuis le 1 janvier 2020 jusqu'à la fin des", jour, "jours sont :", liste)
    
#bisextile(20000)


def nombreBisextile(jour):
    annee = jour // 365 + 2020
    liste = []
    compteur = 2020
    #reste = jour % 365
    for i in range(2020, annee + 1):
        compteur += 1
        if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
            liste.append(i)
    return print("Le nombre d'années bissextiles pour", jour, "jours est", len(liste))



"""OU ALORS (erreur du sujet : à partir de 1970 et non pas 2020) : ----------------------------------------------------------------------------------------------

def nombreBisextile(jour):
    annee = 1970
    compteur = 0
    while jour >= 365:
        if annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0:
            jour = jour - 366
            compteur += 1
            annee += 1
        else:
            jour = jour - 365
            annee += 1
    
    return compteur

print(nombreBisextile(4760)) 


def tempsEnDateBisextile(temps):
    jours = temps[0]
    jours_ajuste = jours - nombreBissextile(jours)

return tempsEnDate((jours_ajuste, temps[1], temps[2], temps[3]))

afficheDate(tempsEnDateBisextile(4760, 0, 0, 0)) --------------------------------------------------------------------------------------------------------------"""





def verifie(liste_temps):

    somme_temps_semaine_1 = liste_temps[0][0] * 24 + liste_temps[0][1]
    if somme_temps_semaine_1 > 48:
        print("Le volume horaire par semaine est dépassé pour la première semaine")
    
    somme_temps_semaine_2 = liste_temps[1][0] * 24 + liste_temps[1][1]
    if somme_temps_semaine_2 > 48:
        print("Le volume horaire par semaine est dépassé pour la deuxième semaine")
    
    somme_temps_semaine_3 = liste_temps[2][0] * 24 + liste_temps[2][1]
    if somme_temps_semaine_3 > 48:
        print("Le volume horaire par semaine est dépassé pour la troisième semaine")
    
    somme_temps_semaine_4 = liste_temps[3][0] * 24 + liste_temps[3][1]
    if somme_temps_semaine_4 > 48:
        print("Le volume horaire par semaine est dépassé pour la quatrième semaine")
    
    liste_temps[0] = tempsEnSeconde(liste_temps[0])
    liste_temps[1] = tempsEnSeconde(liste_temps[1])
    liste_temps[2] = tempsEnSeconde(liste_temps[2])
    liste_temps[3] = tempsEnSeconde(liste_temps[3])

    somme_temps_mois = liste_temps[0] + liste_temps[1] + liste_temps[2] + liste_temps[3]

    if somme_temps_mois // 86400 > 48:
        print("Le volume horaire par mois est dépassé")
    
    return


#liste_temps = [[1,2,39,34],[0,1,9,4],[0,29,39,51],[0,31,13,46]]
#verifie(liste_temps)