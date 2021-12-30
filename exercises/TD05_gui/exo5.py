import tkinter as tk
import random as rd


def dessine_disque() -> None:
    """Dessine un disque de rayon 50 pixels sur une position aléatoire du canvas
    qui est stocké dans la variable globale mon_canvas."""
    centre_x = rd.randint(50, CANVAS_WIDTH - 50)
    centre_y = rd.randint(50, CANVAS_HEIGHT - 50)
    identifiant = mon_canvas.create_oval(centre_x - 50, centre_y - 50,
                                         centre_x + 50, centre_y + 50,
                                         fill=couleur)
    objets.append(identifiant)


def dessine_carre() -> None:
    """Dessine un carré de largeur 50 pixels sur une position aléatoire du canvas
    qui est stocké dans la variable globale mon_canvas."""
    centre_x = rd.randint(50, CANVAS_WIDTH - 50)
    centre_y = rd.randint(50, CANVAS_HEIGHT - 50)
    identifiant = mon_canvas.create_rectangle(centre_x - 50, centre_y - 50,
                                              centre_x + 50, centre_y + 50,
                                              fill=couleur)
    objets.append(identifiant)


def dessine_croix() -> None:
    """Dessine une croix de largeur 50 pixels sur une position aléatoire du canvas
    qui est stocké dans la variable globale mon_canvas. La croix est constituée
    d'une ligne verticale et d'une autre horizontale."""
    centre_x = rd.randint(50, CANVAS_WIDTH - 50)
    centre_y = rd.randint(50, CANVAS_HEIGHT - 50)
    identifiant = mon_canvas.create_line(centre_x, centre_y - 50,
                                         centre_x, centre_y + 50,
                                         fill=couleur)
    objets.append(identifiant)
    identifiant = mon_canvas.create_line(centre_x - 50, centre_y,
                                         centre_x + 50, centre_y,
                                         fill=couleur)
    objets.append(identifiant)


def change_couleur() -> None:
    """Modifie le contenu de la variable globale couleur par une valeur donnée
    par l'utilisateur."""
    global couleur
    couleur = input("Donnez une couleur\n")


def undo() -> None:
    """Efface le dernier élément dessiné sur le Canvas en utilisant les 
    identifiants des dessins stockés dans la variable globale objets."""
    if len(objets) == 0:
        return
    if mon_canvas.type(objets[-1]) == "line":
        mon_canvas.delete(objets[-1])
        del objets[-1]
    mon_canvas.delete(objets[-1])
    del objets[-1]


couleur = "blue"
objets = []


racine = tk.Tk()
racine.title("Mon dessin")
bouton_cercle = tk.Button(racine, text="Cercle", command=dessine_disque)
bouton_couleur = tk.Button(racine, text="Choisir une couleur", command=change_couleur)
bouton_carre = tk.Button(racine, text="Carré", command=dessine_carre)
bouton_croix = tk.Button(racine, text="Croix", command=dessine_croix)
bouton_undo = tk.Button(racine, text="Undo", command=undo)

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 500
mon_canvas = tk.Canvas(racine, background="black", width=CANVAS_WIDTH, height=CANVAS_HEIGHT)

bouton_couleur.grid(row=0, column=1)
bouton_undo.grid(row=0, column=2)
bouton_cercle.grid(row=1, column=0)
bouton_carre.grid(row=2, column=0)
bouton_croix.grid(row=3, column=0)
mon_canvas.grid(row=1, column=1, rowspan=3, columnspan=2)


racine.mainloop()
