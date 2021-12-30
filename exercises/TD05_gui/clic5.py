import tkinter as tk

nb_clic = 0
cercles = []


def gerer_cercle(event) -> None:
    """Dessine un cercle rouge de rayon 50 pixels centré sur les coordonnées
    données par le paramètre event et stocke l'identifiant du cercle dans la
    variable globale cercles. Compte également le nombre de fois où cette
    fonction a été appelée en incrémentant la variable globale nb_clic.
    Après 9 appels, modifie la couleur des cercles déjà dessinés en jaune.
    Après 10 appels, efface tous les cercles et réinitialise nb_clic."""
    global nb_clic, cercles
    nb_clic += 1
    if nb_clic < 9:
        id = mon_canvas.create_oval(event.x - 50, event.y - 50,
                                    event.x + 50, event.y + 50,
                                    fill="red")
        cercles.append(id)
    elif nb_clic == 9:
        for identifiant in cercles:
            mon_canvas.itemconfigure(identifiant, fill="yellow")
    else:
        for identifiant in cercles:
            mon_canvas.delete(identifiant)
        cercles = []
        nb_clic = 0


racine = tk.Tk()
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
mon_canvas = tk.Canvas(racine, background="black", width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
mon_canvas.grid()
mon_canvas.bind("<Button-1>", gerer_cercle)


racine.mainloop()
