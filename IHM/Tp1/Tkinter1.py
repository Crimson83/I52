import tkinter as tk

root=tk.Tk() #fenetre mère
root.title("Fenetre de test") #titre de la fenetre mère
tns=tk.Toplevel(root) #creation de fenetre fille
titre=tk.Label(tns,text="Test") #titre fenetre fille
titre.pack()
can=tk.Canvas(tns,width=500,height=500,bg="white") #fenetre taille 500*500 fond blanc
can.pack()
frame=tk.Frame(tns,width=250,height=10)  #creation frame 250*10 (carré blanc dans la fenetre)
frame.pack()
Button1=tk.Button(frame,text="OK")  #Premier Boutton "OK"
Button1.pack()
Button2=tk.Button(frame,text="ANNULER") #Second Boutton "ANNULER"
Button2.pack()

root.mainloop()
