import tkinter as tk
import random

couleur = ["red", "blue", "magenta", "white", "green"]


def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

# la bordure est par défaut d'un pixel noir quand on créée un rectangle donc on change avec bordure vide

def draw_pixel(i, j, color):
    canvas.create_rectangle(i, j, i, j, fill = color, width = 0)

def ecran_aleatoire():
    for i in range(0, 257):
        for j in range(0, 257):
            r = random.randint(0, 256)
            g = random.randint(0, 256)
            b = random.randint(0, 256)
            color = get_color(r, g, b)
            print(draw_pixel(i, j, color))


racine = tk.Tk()
racine.title("Couleurs")

bouton_aleatoire = tk.Button(racine, text = "Aléatoire", bg = "white", fg = "blue", command=ecran_aleatoire)
bouton_degrade_gris = tk.Button(racine, text = "Dégradé gris", bg = "white", fg = "blue")
bouton_degrade_2d = tk.Button(racine, text = "Dégradé 2D", bg = "white", fg = "blue")

canvas = tk.Canvas(racine, bg = "black", height= 256, width = 256)

bouton_aleatoire.grid(row = 0, column = 0)
bouton_degrade_gris.grid(row = 1, column = 0)
bouton_degrade_2d.grid(row = 2, column = 0)

canvas.grid(column = 1, row = 0, rowspan = 3)

racine.mainloop()