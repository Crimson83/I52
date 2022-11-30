import tkinter as tk
from tkinter import filedialog
def Nouveau(event=0):
    can.delete("all")

def Ouvrir(event=0):
    filedialog.askopenfilename()

def Sauver(event=0):
    Save=tk.Toplevel(can) #creation fenetre sauvegarde
    frame=tk.Frame(Save,height=100,width=100) #texte
    lab=tk.Label(Save,text="Voulez vous sauvegarder ?")
    ButtonOk=tk.Button(frame,text="Oui") #bouton oui
    ButtonNo=tk.Button(frame,text="Non",command=lambda:Save.destroy()) #bouton non
    ButtonOk.pack(side="left")
    lab.pack(side='top')
    frame.pack()
    ButtonNo.pack(side="right")

def Quitter(event=0):
    root.quit()


root=tk.Tk() #fenetre root
root.title("Photoshop")
fenetre=tk.Frame(root,height=10) #frame
fenetre2=tk.Label(root,bg='cyan') #creation label cyan en dessous du canvas
can=tk.Canvas(height=720,width=1080,bg='white') #creation canvas
FichierBut=tk.Menubutton(fenetre,text="Fichier") #bouton fichier
MenuFichier=tk.Menu(FichierBut,tearoff=False) #bouton menu
'''
ajout des commandes
'''
MenuFichier.add_command(label="Nouveau",accelerator="Ctrl+n",command=lambda:Nouveau())
MenuFichier.add_command(label="Ouvrir",accelerator="Ctrl+o",command=lambda:Ouvrir())
MenuFichier.add_command(label="Sauver",state='disable',accelerator="Ctrl+s",command=lambda:Sauver())
MenuFichier.add_command(label="Quitter",accelerator="Ctrl+c",command=lambda:Quitter())
FichierBut["menu"]=MenuFichier
root.bind_all("<Control-n>",Nouveau)
root.bind_all("<Control-o>",Ouvrir)
root.bind_all("<Control-s>",Sauver)
root.bind_all("<Control-c>",Quitter)
AideBut=tk.Button(fenetre,text="Aide") #bouton Aide

fenetre.pack(fill='x')
fenetre2.pack(fill='x',side='bottom')
can.pack(side='bottom',fill='both')
FichierBut.pack(side='left')
FichierBut.pack()
AideBut.pack(side='right')


root.mainloop()
