import tkinter as tk
import random
import time
def gencarte():
    cart=[]
    for i in range(30):
        cart.append([])
        for j in range(20):
            cart[i].append(random.randrange(5))
    return cart

def create_can_carte(carte):
    """
    Creation carte version rectangle sur Canvas
    """
    k=10
    for i in range(len(carte)):
        y=10
        for j in range(len(carte[i])):
            if(carte[i][j]==1):
                can.create_rectangle(k,y,k+10,y+10,fill='black',tags='MUR')
            else:
                can.create_rectangle(k,y,k+10,y+10,fill='white',tags='LAND')
            y+=10
        k+=10

def movebot():
    """
    déplacement aléatoire du Robot
    """
    global id
    global carte
    x,y=can.coords(id)[0],can.coords(id)[1] #recup coord
    rand=random.randrange(4)                #haut bas gauche droite
    x1=0
    y1=0
    list=['H','B','G','D']
    x=int(x)//10
    y=int(y)//10
    print(x,y)
    if(list[rand]=='H' and y>1): #verif si on est pas au bord de la carte
        if(carte[x-1][y-2]!=1): #verif mur au dessus
            y1=-10
    elif(list[rand]=='D' and x<29):
        if(carte[x][y-1]!=1): #verif mur à droite
            x1=10
    elif(list[rand]=='B' and y<19): #verif mur à gauche
        if(carte[x-1][y]!=1):
            y1=10
    elif(list[rand]=='G' and x>1): #verif mur au dessous
        if(carte[x-2][y-1]!=1):
            x1=-10
    can.move(id,x1,y1)
    can.after(100,movebot())

global carte
carte=gencarte()
root=tk.Tk()
root.title("La Guerre Des Robots")
can=tk.Canvas(root,width=1080,height=720,bg='white')
can.pack()
create_can_carte(carte)
global id
id=can.create_rectangle(10,10,20,20,fill='red',tags=("Joueur1","Joueur"))
can.after(100,movebot())
root.mainloop()
