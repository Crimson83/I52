import tkinter as tk

root=tk.Tk()
root.title("Fenetre de test")
tns=tk.Toplevel(root)
titre=tk.Label(tns,"Test","sunken")
titre.pack()
can=tk.Canvas(tns,width=500,height=500,bg="white")
can.pack()
