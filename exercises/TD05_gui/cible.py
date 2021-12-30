import tkinter as tk

racine = tk.Tk()
racine.title("Cible")

nombre_cercles = int(input("Combien de cercles veux-tu ? (<= 25) ")) * 10 + 1

canvas = tk.Canvas(racine, bg="black", height=500, width=500)

x1 = 0
y1 = 0
x2 = 500
y2 = 500

couleur = "blue"
for i in range(10, nombre_cercles, 10):
    if i == 10 or i == 10 + 60 or i == 10 + 2 * 60 or i == 10 + 3 * 60:
        couleur = "blue"
    if i == 20 or i == 20 + 60 or i == 20 + 2 * 60 or i == 20 + 3 * 60:
        couleur = "green"
    if i == 30 or i == 30 + 60 or i == 30 + 2 * 60 or i == 30 + 3 * 60:
        couleur = "black"
    if i == 40 or i == 40 + 60 or i == 40 + 2 * 60 or i == 40 + 3 * 60:
        couleur = "yellow"
    if i == 50 or i == 50 + 60 or i == 50 + 2 * 60 or i == 50 + 3 * 60:
        couleur = "magenta"
    if i == 60 or i == 60 + 60 or i == 60 + 2 * 60 or i == 60 + 3 * 60:
        couleur = "red"
    canvas.create_oval(x1 + i, y1 + i, x2 - i, y2 - i, fill = couleur)



canvas.grid(row = 0, column = 0)

racine.mainloop()