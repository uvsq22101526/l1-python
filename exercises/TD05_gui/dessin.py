import tkinter as tk
from tkinter.constants import GROOVE, RAISED, SUNKEN
import random

racine = tk.Tk() # Création de la fenêtre racine
racine.title("Mon dessin") # ajoute un titre


def cercle(canvas):
    """ Fonction qui affiche un disque de diamètre 100 en bleu à un endroit choisi au hasard du canevas """
    
    x1 = random.randint(1, 400)
    x2 = x1 + 100
    y1 = random.randint(1, 400)
    y2 = y1 + 100
    global oval
    oval = canvas.create_oval(x1, y1, x2, y2, fill="blue")

    print(canvas)

def carre(canvas):
    """ Fonction qui affiche un carré de côté 100 en rouge à un endroit choisi au hasard du canevas """

    x1 = random.randint(1, 400)
    x2 = x1 + 100
    y1 = random.randint(1, 400)
    y2 = y1 + 100
    global rectangle
    rectangle = canvas.create_rectangle(x1, y1, x2, y2, fill="red")

    print(canvas)

def croix(canvas):
    """ Fonction qui affiche une croix jaune inscrite dans un carré de côté 100 à un endroit choisi au hasard du canevas """
    x1 = random.randint(1, 400)
    x2 = x1 + 100
    y1 = random.randint(1, 400)
    y2 = y1 + 100
    global ligne_1
    global ligne_2
    ligne_1 = canvas.create_line(x1, y1, x2, y2, width = 5, fill= "yellow")
    ligne_2 = canvas.create_line(x2, y1, x1, y2, width = 5, fill = "yellow")
    
    print(canvas1)

"""def couleur():
    
    global couleur
    couleur = str(input("Choisis une couleur "))

    ligne_1.itemconfigure(fill = couleur)
    ligne_2.itemconfigure(fill = couleur)
    oval.itemconfigure(fill = couleur)
    rectangle.itemconfig(fill = couleur)"""


button1 = tk.Button(racine, text="Choisir une couleur", font=("helvetica", "20")) #command = couleur
button2 = tk.Button(racine, text="Cercle", font=("helvetica", "20"), command = lambda : cercle(canvas1))
button3 = tk.Button(racine, text="Carré", font=("helvetica", "20"), command = lambda : carre(canvas1))
button4 = tk.Button(racine, text="Croix", font=("helvetica", "20"), command = lambda : croix(canvas1))

canvas1 = tk.Canvas(racine, bg="black", height=500, width=500, selectborderwidth=10, relief=SUNKEN)

button1.grid(row = 0, column = 1) # positionnement du widget
button2.grid(row = 4, column = 0)
button3.grid(row = 10, column = 0)
button4.grid(row = 16, column = 0)
canvas1.grid(row = 2, column = 1, rowspan=20)


racine.mainloop() # Lancement de la boucle principale