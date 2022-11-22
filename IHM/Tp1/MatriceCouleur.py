import tkinter as tk
import math
import Tp1


def affichcouleur():
    Haut=720
    Larg=720
    nbrc=len(Index)
    nbrc_ligne=math.sqrt(nbrc)
    '''
    fonction qui crée des carrés de couleur dans le Canvas
    '''
    i,j=5,5
    for couleur in dic : #pour chaque couleur (clé) du dico
        hexcode='#' #début d'un code couleur en hexa
        tmp=''
        for h in range(3): #on passe dans chaque nombre du tuple
            tmp=hex(int(dic[couleur][h]))[2:]
            if len(tmp)<2: #si le code hex est composé que d'un caractère
                tmp='0'+tmp #on rajoute 0 au début
            hexcode+=tmp
        #print(hexcode)
        can.create_rectangle(i,j,i+10,j+10,fill=hexcode,tags=(couleur,'Carré')) #on ajoute un carré de cette couleur
        can.pack()
        i+=15
        if(i>(nbrc_ligne*15)): #saut de ligne
            i=5
            j+=15

chemin="/etc/X11/rgb.txt"
option=str(input("Option d'ouverture du fichier :"))
dic={}
dic=Tp1.parser(chemin,option)
Index=[]
Index=Tp1.convers(dic)
root=tk.Tk() #fenetre mère
root.title("Fenêtre Mère") #nom de la fenetre mère
tns=tk.Toplevel(root) #creation de fenetre fille
tns.title("Fenêtre Fille")
titre=tk.Label(tns,text="Matrice de Couleur") #titre dans la fenetre fille
titre.pack()
can=tk.Canvas(tns,width=500,height=500,bg="white") #fenetre taille 500*500 fond blanc
can.pack()

affichcouleur()
root.mainloop()
